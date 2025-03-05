import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

print(lista_arquivos)

locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Pdfs": [".pdf"],
    "Textos": [".txt", ".docx", ".odt", ".rtf"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Audios": [".mp3", ".wav", ".ogg", ".flac"],
    "Codigos Python": [".py", ".ipynb"],
    "Programas": [".exe"],
    "Log": [".log"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
