import time
import sys
import os
import tools.leArquivos as leArquivos

def FileExists(filepath):
    return os.path.isfile(filepath)

def PDFToText(arquivos=leArquivos.buscaArquivosEmPasta(caminho="C:\\_temp\\teste-ler-pdf", extensao=(".pdf")), mode = "simples"):
    for arquivo in arquivos:
        print(os.path.abspath(os.path.dirname(__file__)))
        saida = str(arquivo) + ".txt"
        try:
            #comando = "{}\\pdftotext.exe -{} \"{}\" \"{}\"".format(os.path.abspath(os.path.dirname(__file__)), mode, arquivo, saida)
            comando = "C:\\_temp\\teste-ler-pdf\\pdftotext.exe \"{}\" \"{}\"".format( arquivo, saida)
            resultado = os.system(comando)
        except Exception as ex:
            print(f"Nao foi possivel transformar o arquivo \"{saida}\". O erro é: {str(ex)}")

PDFToText()