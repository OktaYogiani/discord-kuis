# Tugas 2 - Import semua yang Anda butuhkan
from discord import ui 
from discord import ButtonStyle

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        # Tugas 3 - Buat metode untuk menghasilkan Inline keyboard
        tombol = []
        for indeks, jawaban in enumerate(self.options):
            if indeks == self.__answer_id:
                tombol.append(ui.Button(label= jawaban, style=ButtonStyle.primary, custom_id=f'correct_{indeks}'))
            else:
                tombol.append(ui.Button(label= jawaban, style=ButtonStyle.primary, custom_id=f'wrong_{indeks}'))
        return tombol

# Tugas 4 - Isi list dengan pertanyaan Anda
quiz_questions = [
    Question("Apa yang kucing lakukan ketika tidak ada yang melihat mereka?", 1, "Tidur", "Menulis meme"),
    Question("Bagaimana kucing menunjukkan cinta?", 0, "Purring keras", "Foto cinta", "Menggonggong"),
    Question("Buku apa yang kucing suka membaca?", 3, "Buku bantuan diri sendiri", "Manajemen waktu: bagaimana tidur 18 jam sehari", "101 cara untuk tidur 5 menit lebih awal dari pemilik Anda", "Panduan manajemen manusia"),
    Question("Kenapa ikan rasanya asin?", 1, "Karena minum air laut", "Karena kelamaan berendam di laut", "Karena takut dimasak"),
    Question("Apa yang selalu jatuh tapi tidak pernah naik?", 1, "Harga diri", "Hujan", "Mantan"),
    Question("Hewan apa yang kalau dibolak-balik tetap sama?", 0, "katak", "sapi", "ayam"),
    Question("Kecil pagi, besar siang, hilang malam?", 2, "Balon", "Balita", "Bayangan")
]

