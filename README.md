# 🧹 Limpador de Sistema Windows

Um utilitário portátil em Python desenvolvido para automatizar e facilitar manutenções básicas em computadores com sistema operacional Windows. 

---

## 📌 Sobre o Projeto

Este é um **projeto pessoal de código aberto**, criado originalmente para otimizar e automatizar a rotina de manutenção nos computadores de casa. Em vez de executar comandos manualmente pelo prompt ou navegar por várias telas do sistema, a aplicação reúne as principais ferramentas de diagnóstico e limpeza em uma interface gráfica moderna e intuitiva.

## 🚀 Funcionalidades

* **Otimização e Limpeza:** Remoção automática de arquivos temporários e esvaziamento da Lixeira.
* **Diagnóstico de Integridade:** Execução simplificada do utilitário `sfc /scannow` com elevação de privilégios para reparar arquivos corrompidos do sistema.
* **Rede:** Renovação de IP e limpeza de cache DNS (`ipconfig /flushdns`).
* **Interface Moderna:** Desenvolvida em Tkinter com estilo Dark Glassmorphism, mantendo o uso leve de recursos.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica:** Tkinter
* **Integração com o Sistema:** Módulos nativos `subprocess` e `ctypes`

---

## 📥 Como Usar / Executar

### Opção 1: Executável Portátil (Sem necessidade de Python)
Você pode baixar a versão compilada diretamente na seção de **[Releases](https://github.com/surfista264/Limpador-do-Sistema-/releases)** do repositório.

1. Baixe o arquivo `LimpadorDoSistema.exe`.
2. Clique com o botão direito no executável e selecione **"Executar como Administrador"** (necessário para que os comandos de sistema funcionem corretamente).

### Opção 2: Rodando o Código Fonte
Caso queira executar via terminal:

```bash
# Clone o repositório
git clone [https://github.com/surfista264/Limpador-do-Sistema-.git](https://github.com/surfista264/Limpador-do-Sistema-.git)

# Acesse a pasta do projeto
cd Limpador-do-Sistema-

# Execute a aplicação
python main.py