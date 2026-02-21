import discord
from discord.ext import commands
from logic import quiz_questions
# Tugas 7 - impor perintah defaultdict
from collections import defaultdict
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_responses = {}
# Tugas 8 - buat kamus titik untuk menyimpan titik pengguna
points = defaultdict(int)

async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]
    buttons = question.gen_buttons()
    view = discord.ui.View()
    for button in buttons:
        view.add_item(button)

    embed = discord.Embed(title="Quiz Time!", description=question.text)
    if hasattr(question, "image_url") and question.image_url:
        embed.set_image(url=question.image_url)
    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.event
async def on_ready():
    print(f'Login baru: {bot.user}!')


@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        await interaction.response.send_message("Silakan mulai quiz dengan mengetikkan perintah !start")
        return

    custom_id = interaction.data["custom_id"]
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Jawaban benar!")
        await interaction.response.edit(view=None)
        # Tugas 9 - tambahkan titik ke pengguna untuk jawaban yang benar
        points[user_id] += 1
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Jawaban salah!")

    # Tugas 5 - implementasi penghitung pertanyaan
    user_responses[user_id] += 1
    # Tugas 6 - kirim pesan ke pengguna tentang hasil quiz jika mereka menjawab semua pertanyaan. Jika tidak, kirim pertanyaan berikutnya
    if user_responses[user_id] > len(quiz_questions) - 1:
        await interaction.followup.send(f"Kuis selesai! Point kamu {points[user_id]}")
        del user_responses[user_id]
    else:
        await send_question(interaction, user_id)

@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id not in user_responses:
        user_responses[user_id] = 0
        points[user_id]=0
        await ctx.send ("Kuis telah di restart")
        await send_question(ctx, user_id)

bot.run(token)

