
import subprocess
import os
import sys

def criar_barra(porcentagem, largura=30):
    preenchido = int(largura * porcentagem / 100)
    vazio = largura - preenchido

    return "[" + "█" * preenchido + "░" * vazio + "]"


print("===== YT DOWNLOADER =====")

link = input("\nDigite o link do video: ")

print("\n1 - Somente audio (MP3)")
print("2 - Somente video (MP4)")

opcao = input("\nEscolha: ")

if opcao not in ["1", "2"]:
    print("Opcao invalida!")
    sys.exit()

# Localiza o script PowerShell
if getattr(sys, "frozen", False):
    caminho = os.path.join(sys._MEIPASS, "baixar.ps1")
else:
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "yt.ps1"
    )

print("\nIniciando processo...\n")

processo = subprocess.Popen(
    [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", caminho,
        "-link", link,
        "-opcao", opcao
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

try:
    for linha in processo.stdout:

        linha = linha.strip()

        if linha.startswith("PROGRESSO|"):

            dados = linha.split("|")

            porcentagem = dados[1].replace("%", "").strip()
            velocidade = dados[2].strip()
            baixado = dados[3].strip()
            total = dados[4].strip()
            restante = dados[5].strip()

            try:
                porcentagem = float(porcentagem)
            except ValueError:
                continue

            barra = criar_barra(porcentagem)

            print(
                f"\r{barra} {porcentagem:5.1f}% "
                f"| {velocidade} "
                f"| {baixado}/{total} "
                f"| ETA: {restante}   ",
                end="",
                flush=True
            )

        elif linha == "DOWNLOAD_CONCLUIDO":
            print("\n\nDownload concluido com sucesso!")

        elif linha == "DOWNLOAD_ERRO":
            print("\n\nErro durante o download!")

        elif linha:
            print("\n" + linha)

    codigo = processo.wait()

    if codigo != 0:
        print(f"\nProcesso encerrado com codigo: {codigo}")

except KeyboardInterrupt:
    print("\n\nCancelando download...")
    processo.terminate()
    processo.wait()

except Exception as erro:
    print(f"\nErro: {erro}")

input("\nPressione ENTER para sair...")
