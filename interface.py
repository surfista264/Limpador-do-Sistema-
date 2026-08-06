import tkinter as tk
from tkinter import font as tkfont
import tarefas as tarefas


def iniciar_interface():
    # 1. Cria a janela principal
    janela = tk.Tk()
    janela.title("Limpador do Sistema")
    janela.geometry("400x450")

    # --- PALETA MINIMALISTA / EFEITO VIDRO ESCURO ---
    bg_janela = "#11111b"  # Fundo principal bem escuro (Base)
    bg_card = "#1e1e2e"  # Placa principal estilo vidro escuro (Surface)
    btn_bg = "#313244"  # Cor dos botões comuns (Overlay)
    btn_hover = "#45475a"  # Cor ao passar o mouse
    btn_destaque = "#f38ba8"  # Mantida a cor do seu botão 'Limpar Tudo'
    text_color = "#cdd6f4"  # Texto claro
    text_dark = "#11111b"  # Texto escuro para botões destacados

    janela.config(bg=bg_janela)

    # Fonte moderna nativa
    fonte_titulo = tkfont.Font(family="Segoe UI", size=14, weight="bold")
    fonte_botoes = tkfont.Font(family="Segoe UI", size=10)

    # 2. Título / Texto na tela
    titulo = tk.Label(
        janela,
        text="O que deseja limpar no seu PC?",
        font=fonte_titulo,
        fg=text_color,
        bg=bg_janela,
    )
    titulo.pack(pady=(20, 10))

    # 3. Estrutura de Scrollbar (Canvas + Frame) — MANTIDA DO SEU CÓDIGO
    container = tk.Frame(janela, bg=bg_janela)
    container.pack(fill="both", expand=True, padx=15, pady=5)

    canvas = tk.Canvas(container, bg=bg_janela, highlightthickness=0, bd=0)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

    # Frame rolável onde os botões serão colocados
    frame_botoes = tk.Frame(canvas, bg=bg_janela)

    frame_botoes.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
    )

    canvas.create_window((200, 0), window=frame_botoes, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Efeito visual para passar o mouse nos botões (Hover)
    def ao_entrar(e):
        if e.widget["bg"] != btn_destaque:
            e.widget["bg"] = btn_hover

    def ao_sair(e):
        if e.widget["bg"] != btn_destaque:
            e.widget["bg"] = btn_bg

    # Helper para criar os botões com padrão minimalista mantendo seus dados
    def criar_btn(texto, comando, destaque=False):
        btn = tk.Button(
            frame_botoes,
            text=texto,
            font=fonte_botoes,
            bg=btn_destaque if destaque else btn_bg,
            fg=text_dark if destaque else text_color,
            activebackground=btn_hover,
            activeforeground=text_color,
            width=30,
            height=2,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=comando,
        )
        btn.bind("<Enter>", ao_entrar)
        btn.bind("<Leave>", ao_sair)
        btn.pack(pady=6)
        return btn

    # 4. Botões Visuals (Criados dentro de 'frame_botoes') — TODOS OS SEUS CAMINHOS
    criar_btn("1. Limpar Arquivos Temporários", tarefas.limpar_temp)
    criar_btn("2. Esvaziar Lixeira", tarefas.limpar_lixeira)
    criar_btn("3. Limpar DNS", tarefas.limpar_dns)
    criar_btn("4. Limpar de Disco", tarefas.limpar_disco)
    criar_btn("5. Relatório de Desempenho", tarefas.gerar_relatorio)
    criar_btn("6. Verificar Arquivos de Sistema", tarefas.verificar_arquivos_sistema)

    # Botão de destaque final
    criar_btn("7. Executar Limpeza Completa", tarefas.limpar_tudo, destaque=True)

    # 5. Mantém a janela aberta
    janela.mainloop()