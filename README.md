# 🎵 YT Downloader

Um aplicativo desktop para baixar vídeos e áudios do YouTube, com uma interface gráfica simples e intuitiva.

O projeto utiliza Python, CustomTkinter, PowerShell e yt-dlp para realizar os downloads, permitindo escolher entre os formatos MP3 e MP4.

## ✨ Funcionalidades

- 🎧 Download de áudio no formato MP3.
- 🎬 Download de vídeo no formato MP4.
- 📊 Barra de progresso durante o download.
- ⚡ Exibição da velocidade e do tempo estimado de download.
- 📂 Acesso rápido à pasta onde os arquivos foram salvos.
- 🔔 Notificações de sucesso e erro.
- 🌙 Interface gráfica com tema escuro.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **CustomTkinter:** criação da interface gráfica.
- **yt-dlp:** ferramenta responsável pelos downloads.
- **FFmpeg:** processamento e conversão de áudio e vídeo.
- **PowerShell:** execução dos processos de download.
- **PyInstaller:** geração do executável para Windows.

## 🚀 Como utilizar

1. Baixe o executável na seção [Releases](../../releases).
2. Execute o arquivo `YT Downloader.exe`.
3. Cole o link do vídeo do YouTube.
4. Escolha entre MP3 ou MP4.
5. Clique em baixar.
6. Aguarde a conclusão do download.

## 💻 Executar o projeto pelo código-fonte

Caso queira executar o projeto utilizando Python:

**1. Clone o repositório:**

```bash
git clone https://github.com/Nolt-Gabriel/Baixador_videoaudio_ytdlp.git
```

**2. Entre na pasta do projeto:**

```bash
cd YT-Downloader
```

**3. Crie e ative um ambiente virtual:**

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Instale as dependências:**

```bash
python -m pip install -r requirements.txt
```

**5. Execute o programa:**

```bash
python yt.py
```

> Para executar a versão pelo código-fonte, também é necessário ter o PowerShell, yt-dlp e FFmpeg corretamente configurados.

## 📁 Estrutura do projeto

```text
YT-Downloader/
│
├── yt.py
├── yt.ps1
├── tools/
│   ├── yt-dlp.exe
│   ├── ffmpeg.exe
│   └── ffprobe.exe
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 📌 Observações

- Aplicativo desenvolvido para Windows.
- É necessário ter conexão com a internet para realizar downloads.
- Os arquivos são salvos nas pastas de destino configuradas pelo programa.
- O projeto utiliza ferramentas de terceiros, cada uma sujeita aos seus respectivos termos e licenças.

## 📄 Licenças

## 📄 Licenças

O código original do YT Downloader é distribuído sob a licença MIT.
Consulte o arquivo [LICENSE](LICENSE) para conhecer os termos completos.

O projeto também utiliza ferramentas de terceiros, que mantêm suas
próprias licenças:

- yt-dlp
- FFmpeg e FFprobe
- CustomTkinter
- PyInstaller e demais dependências Python

Os avisos de direitos autorais e as licenças dessas ferramentas
estão documentados na pasta `licenses/`.

A licença MIT do projeto não substitui nem altera as licenças
dos componentes de terceiros.
---

Desenvolvido como projeto pessoal de estudo e prática de programação.
