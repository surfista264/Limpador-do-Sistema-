import os
import shutil
import subprocess
import time


def limpar_temp():
    """Apaga os arquivos das pastas Temp (%temp% e Temp do Windows)."""
    pastas_temp = [os.environ.get("TEMP"), r"C:\Windows\Temp"]

    for pasta in pastas_temp:
        if pasta and os.path.exists(pasta):
            for item in os.listdir(pasta):
                caminho_item = os.path.join(pasta, item)
                try:
                    if os.path.isfile(caminho_item) or os.path.islink(
                        caminho_item
                    ):
                        os.unlink(caminho_item)
                    elif os.path.isdir(caminho_item):
                        shutil.rmtree(caminho_item)
                except Exception:
                    # Ignora arquivos que estão atualmente em uso pelo Windows/programas
                    pass


def limpar_lixeira():
    """Esvazia a Lixeira do Windows em segundo plano sem exibir confirmação."""
    try:
        # Usa o PowerShell com o cmdlet Clear-RecycleBin
        comando = "powershell.exe -Command Clear-RecycleBin -Force -ErrorAction SilentlyContinue"
        subprocess.run(comando, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        print(f"Erro ao esvaziar lixeira: {e}")


def limpar_dns():
    """Executa o flushdns para limpar o cache de DNS."""
    try:
        subprocess.run(
            "ipconfig /flushdns",
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    except Exception as e:
        print(f"Erro ao limpar DNS: {e}")


def limpar_disco():
    """Abre a ferramenta nativa de Limpeza de Disco do Windows (cleanmgr)."""
    try:
        subprocess.Popen("cleanmgr.exe")
    except Exception as e:
        print(f"Erro ao abrir Limpeza de Disco: {e}")


def gerar_relatorio():
    """Abre o perfmon /report em modo Administrador."""
    try:
        # Usamos aspas simples por fora e aspas duplas no ArgumentList
        comando = 'powershell -Command "Start-Process cmd -ArgumentList \'/c perfmon /report\' -Verb RunAs"'
        subprocess.Popen(comando, shell=True)
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")

def verificar_arquivos_sistema():
    """Abre o sfc /scannow no CMD em modo Administrador."""
    try:
        comando = 'powershell -Command "Start-Process cmd -ArgumentList \'/k sfc /scannow\' -Verb RunAs"'
        subprocess.Popen(comando, shell=True)
    except Exception as e:
        print(f"Erro ao verificar arquivos do sistema: {e}")
        
def limpar_tudo():
    """Executa todas as rotinas de limpeza em sequência."""
    limpar_temp()
    limpar_lixeira()
    limpar_dns()
    limpar_disco()