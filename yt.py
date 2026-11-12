
import subprocess
import os

print("===== BAIXADOR YT-DLP =====")

link = input("\nDigite o link do video: ")

print("\nO que deseja baixar?")
print("1 - Somente audio (MP3)")
print("2 - Somente video (MP4)")

opcao = input("\nEscolha: ")

if opcao not in ["1", "2"]:
    print("Opcao invalida!")
    exit()

# Caminho do script PowerShell
caminho = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "yt.ps1"
)

# Executa o PowerShell enviando o link e a opcao
resultado = subprocess.run(
    [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", caminho,
        "-link", link,
        "-opcao", opcao
    ],
    capture_output=True,
    text=True
)

print("\n===== RESULTADO =====")

print(resultado.stdout)

if resultado.returncode != 0:
    print("Ocorreu um erro:")
    print(resultado.stderr)

input("\nPressione ENTER para sair...")
