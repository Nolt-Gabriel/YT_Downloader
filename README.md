# 🎬 YT Downloader

<p align="center">
  Um aplicativo desktop simples e intuitivo para baixar vídeos e músicas do YouTube!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CustomTkinter-2B2B2B?style=for-the-badge" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
</p>

---

## ✨ Sobre o projeto

O **YT Downloader** é um aplicativo desenvolvido em Python que permite baixar vídeos e extrair áudios de maneira prática, através de uma interface gráfica. Criado com auxílio de Inteligência Artificial.

Utilizando o poder do [yt-dlp](https://github.com/yt-dlp/yt-dlp) e do [FFmpeg](https://ffmpeg.org/), o programa oferece uma experiência simples, sem a necessidade de utilizar comandos no terminal durante os downloads.

## 🚀 Funcionalidades

- 🎵 **Download de áudio:** extração e conversão para MP3.
- 🎥 **Download de vídeo:** download e conversão para MP4.
- 📊 **Progresso em tempo real:** acompanhe a porcentagem do download.
- ⚡ **Informações detalhadas:** velocidade, tamanho baixado e tempo restante.
- 📂 **Acesso rápido:** abra diretamente a pasta onde os arquivos foram salvos.
- 🖥️ **Interface gráfica:** visual moderno e intuitivo com CustomTkinter.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem principal |
| 🎨 CustomTkinter | Interface gráfica |
| ⚙️ PowerShell | Execução dos comandos de download |
| 📥 yt-dlp | Download de vídeos e áudios |
| 🎞️ FFmpeg | Conversão e processamento de mídia |
| 📦 PyInstaller | Geração do executável |

## 📋 Requisitos

Antes de utilizar o aplicativo, é necessário instalar:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases)
- [FFmpeg](https://ffmpeg.org/download.html)

> ⚠️ **Atenção:** o yt-dlp e o FFmpeg não acompanham o aplicativo. Eles precisam ser instalados separadamente e adicionados à variável de ambiente `PATH` do Windows.

### 🔎 Verificando a instalação

Abra o PowerShell e execute:

```powershell
where.exe yt-dlp
where.exe ffmpeg
where.exe ffprobe
```

Se os comandos retornarem os caminhos dos executáveis, está tudo pronto!

## 📥 Como utilizar

1. Instale o yt-dlp e o FFmpeg.
2. Verifique se os programas estão disponíveis no `PATH`.
3. Execute o arquivo `YT Downloader.exe`.
4. Cole o link do vídeo desejado.
5. Escolha o formato: MP3 ou MP4.
6. Clique em **INICIAR DOWNLOAD** e acompanhe o progresso!

### 📁 Onde os arquivos ficam salvos?

Os downloads são organizados automaticamente:

| Tipo | Pasta de destino |
|---|---|
| 🎵 Áudios | `Música/yt-dlp` |
| 🎥 Vídeos | `Vídeos/yt-dlp` |

## 💻 Executando pelo código-fonte

Se deseja executar ou modificar o projeto, siga os passos abaixo.

**1. Clone o repositório:**

```bash
git clone https://github.com/Nolt-Gabriel/YT_Downloader.git
```

**2. Entre na pasta do projeto:**

```bash
cd Baixador
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Execute o aplicativo:**

```bash
python main.py
```

> 💡 Não esqueça de instalar o yt-dlp e o FFmpeg e adicioná-los ao `PATH`, mesmo executando pelo código-fonte.

## 📦 Gerando o executável

Para gerar seu próprio executável, instale o PyInstaller:

```bash
pip install pyinstaller
```

Depois, execute:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name "YT Downloader" --collect-all customtkinter --add-data "yt.ps1;." main.py
```

O arquivo será gerado na pasta `dist`.

## 📜 Licença

Este projeto está sob a licença [MIT](LICENSE).

O **yt-dlp** e o **FFmpeg** são ferramentas de terceiros, distribuídas sob suas próprias licenças.

---

<p align="center">
  Feito com 🐍 Python e ☕ dedicação por Nolt.
</p>
