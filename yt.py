import customtkinter as ctk
import subprocess
import threading
import queue
import os
import sys


# Configurações visuais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Baixador:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("YT Downloader")
        self.janela.geometry("750x650")
        self.janela.minsize(False, False)
        self.pasta_destino = None

        self.centralizar_janela(

            self.janela,
            750,
            650
        )

        # Fila para comunicação entre a thread e a interface
        self.fila = queue.Queue()

        # Localiza o arquivo PowerShell
        if getattr(sys, "frozen", False):
            self.caminho = os.path.join(
                sys._MEIPASS, "yt.ps1"
            )
        else:
            self.caminho = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "yt.ps1"
            )

        self.criar_interface()

        # Verifica periodicamente se chegaram novas mensagens
        self.janela.after(100, self.processar_fila)

    def criar_interface(self):

        # Container principal
        self.container = ctk.CTkFrame(
            self.janela,
            corner_radius=15
        )
        self.container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        # Título
        self.titulo = ctk.CTkLabel(
            self.container,
            text="YT DOWNLOADER",
            font=("Arial", 28, "bold")
        )
        self.titulo.pack(pady=(30, 5))

        self.subtitulo = ctk.CTkLabel(
            self.container,
            text="Baixe vídeos e músicas com facilidade",
            text_color="gray"
        )
        self.subtitulo.pack(pady=(0, 30))

        # Campo de URL
        self.url = ctk.CTkEntry(
            self.container,
            placeholder_text="Cole o link do vídeo aqui...",
            width=450,
            height=40
        )
        self.url.pack(pady=10)

        # Seleção do formato
        self.formato = ctk.StringVar(value="2")

        self.opcoes = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )
        self.opcoes.pack(pady=15)

        ctk.CTkRadioButton(
            self.opcoes,
            text="Áudio MP3",
            variable=self.formato,
            value="1"
        ).pack(side="left", padx=20)

        ctk.CTkRadioButton(
            self.opcoes,
            text="Vídeo MP4",
            variable=self.formato,
            value="2"
        ).pack(side="left", padx=20)

        # Botão de download
        self.botao = ctk.CTkButton(
            self.container,
            text="INICIAR DOWNLOAD",
            width=220,
            height=42,
            font=("Arial", 14, "bold"),
            command=self.iniciar_download
        )
        self.botao.pack(pady=15)

        self.botao_pasta = ctk.CTkButton(
            self.container,
            text="ABRIR PASTA DE DOWNLOADS",
            width=220,
            height=35,
            fg_color="transparent",
            border_width=1,
            text_color=("gray10", "white"),
            command=self.abrir_pasta,
            state="disabled"
        )

        self.botao_pasta.pack(pady=5)

        # Barra de progresso
        self.barra = ctk.CTkProgressBar(
            self.container,
            width=450,
            height=15
        )
        self.barra.pack(pady=(25, 5))
        self.barra.set(0)

        self.porcentagem = ctk.CTkLabel(
            self.container,
            text="0%"
        )
        self.porcentagem.pack()

        # Informações do download
        self.info = ctk.CTkLabel(
            self.container,
            text="Velocidade: -- | Baixado: --/-- | ETA: --",
            text_color="gray"
        )
        self.info.pack(pady=10)

        # Status
        self.status = ctk.CTkLabel(
            self.container,
            text="Aguardando link...",
            text_color="gray"
        )
        self.status.pack(pady=10)

    def centralizar_janela(self, janela, largura, altura):

        janela.update_idletasks()

        # Obtém as dimensões da tela
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        # Calcula a posição central
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        # Define tamanho e posição
        janela.geometry(
            f"{largura}x{altura}+{x}+{y}"
        )

    def iniciar_download(self):

        link = self.url.get().strip()
        opcao = self.formato.get()

        if not link:
            self.status.configure(
                text="Insira um link antes de continuar!",
                text_color="#F87171"
            )
            return

        if not os.path.isfile(self.caminho):
            self.status.configure(
                text="Arquivo yt.ps1 não encontrado!",
                text_color="#F87171"
            )
            return

        # Reinicia as informações visuais
        self.barra.set(0)
        self.porcentagem.configure(text="0%")
        self.info.configure(
            text="Velocidade: -- | Baixado: --/-- | ETA: --"
        )
        self.status.configure(
            text="Preparando download...",
            text_color="gray"
        )

        self.botao.configure(
            state="disabled",
            text="BAIXANDO..."
        )

        # Inicia o download em outra thread
        thread = threading.Thread(
            target=self.executar_download,
            args=(link, opcao),
            daemon=True
        )
        thread.start()

    def executar_download(self, link, opcao):

        try:
            processo = subprocess.Popen(
                [
                    "powershell",
                    "-NoProfile",
                    "-ExecutionPolicy", "Bypass",
                    "-File", self.caminho,
                    "-link", link,
                    "-opcao", opcao
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Lê as mensagens enviadas pelo PowerShell
            for linha in processo.stdout:
                self.fila.put(("linha", linha.strip()))

            codigo = processo.wait()
            self.fila.put(("fim", codigo))

        except Exception as erro:
            self.fila.put(("erro", str(erro)))

    def processar_fila(self):

        while not self.fila.empty():

            tipo, conteudo = self.fila.get()

            if tipo == "linha":
                self.tratar_linha(conteudo)

            elif tipo == "fim":
                self.finalizar_download(conteudo)

            elif tipo == "erro":
                self.status.configure(
                    text=f"Erro: {conteudo}",
                    text_color="#F87171"
                )
                self.liberar_botao()

        # Continua verificando a fila
        self.janela.after(100, self.processar_fila)

    def tratar_linha(self, linha):

        if linha.startswith("PROGRESSO|"):

            dados = linha.split("|")

            if len(dados) < 6:
                return

            try:
                porcentagem = float(
                    dados[1].replace("%", "").strip()
                )
            except ValueError:
                return

            velocidade = dados[2].strip()
            baixado = dados[3].strip()
            total = dados[4].strip()
            restante = dados[5].strip()

            # Atualiza a barra e as informações
            self.barra.set(porcentagem / 100)

            self.porcentagem.configure(
                text=f"{porcentagem:.1f}%"
            )

            self.info.configure(
                text=(
                    f"Velocidade: {velocidade} | "
                    f"Baixado: {baixado}/{total} | "
                    f"ETA: {restante}"
                )
            )

        elif linha == "BAIXANDO_AUDIO":
            self.status.configure(text="Baixando áudio...")

        elif linha == "BAIXANDO_VIDEO":
            self.status.configure(text="Baixando vídeo...")

        elif linha == "DOWNLOAD_CONCLUIDO":
                
            self.barra.set(1)
            self.porcentagem.configure(text="100%")

            self.status.configure(
                    text="Download concluído com sucesso!",
                    text_color="#4ADE80"
                )

            self.mostrar_popup(
                    "Download concluído!",
                    "Seu arquivo foi baixado com sucesso.",
                    sucesso=True
                )

        elif linha == "DOWNLOAD_ERRO":

            self.status.configure(
                text="Ocorreu um erro no download.",
                text_color="#F87171"
                )

            self.mostrar_popup(
                "Erro no download!",
                "Não foi possível concluir o download.",
                sucesso=False
            )


        elif linha.startswith("PASTA_DESTINO|"):

            self.pasta_destino = linha.split("|", 1)[1]

            self.botao_pasta.configure(
                state="normal"
            )

        elif linha and linha not in [
                    "INICIANDO"
                ]:
                    self.status.configure(text=linha[:100])

    def finalizar_download(self, codigo):

        if codigo != 0:
            self.status.configure(
                text=f"Download encerrado com erro (código {codigo}).",
                text_color="#F87171"
            )

        self.liberar_botao()

    def liberar_botao(self):

        self.botao.configure(
            state="normal",
            text="INICIAR DOWNLOAD"
        )


    def mostrar_popup(self, titulo, mensagem, sucesso=True):

        popup = ctk.CTkToplevel(self.janela)

        popup.title(titulo)
        popup.geometry("350x220")
        popup.resizable(False, False)

        # Mantém o pop-up vinculado à janela principal
        popup.transient(self.janela)
        popup.grab_set()

        # Ícone e cor conforme o resultado
        if sucesso:
            icone = "✓"
            cor = "#4ADE80"
        else:
            icone = "✕"
            cor = "#F87171"

        ctk.CTkLabel(
            popup,
            text=icone,
            font=("Arial", 42, "bold"),
            text_color=cor
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            popup,
            text=titulo,
            font=("Arial", 20, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(
            popup,
            text=mensagem,
            font=("Arial", 13),
            wraplength=300
        ).pack(pady=5)

        ctk.CTkButton(
            popup,
            text="OK",
            width=120,
            command=popup.destroy
        ).pack(pady=15)

        def posicionar_popup():

            popup.update_idletasks()
            self.janela.update_idletasks()

            # Dimensões e posição da janela principal
            x_janela = self.janela.winfo_rootx()
            y_janela = self.janela.winfo_rooty()

            largura_janela = self.janela.winfo_width()
            altura_janela = self.janela.winfo_height()

            # Dimensões reais do pop-up
            largura_popup = popup.winfo_width()
            altura_popup = popup.winfo_height()

            # Calcula o centro da janela principal
            x = x_janela + (largura_janela - largura_popup) // 2
            y = y_janela + (altura_janela - altura_popup) // 2

            popup.geometry(f"+{x}+{y}")

            popup.focus_force()


        popup.after(100, posicionar_popup)

        
    def abrir_pasta(self):

        if self.pasta_destino and os.path.isdir(self.pasta_destino):
            os.startfile(self.pasta_destino)

        else:
            self.status.configure(
                text="Pasta de destino não encontrada!",
                text_color="#F87171"
            )

# Inicialização do programa
janela = ctk.CTk()
app = Baixador(janela)

janela.mainloop()
