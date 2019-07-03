import pytesseract as ocr
import tools.leArquivos as leArquivos

from PIL import Image

def imageToText(arquivos=leArquivos.buscaArquivosEmPasta(caminho="D:\\programming\\conv-dominio\\imgs-teste\\webcon", extensao=(".jpg", ".jpeg"))):
    print(arquivos)
    for arquivo in arquivos:
        nome_arquivo_saida = str(arquivo) + ".txt"
        saida = open(nome_arquivo_saida, "w", encoding='utf-8')
        phrase = ocr.image_to_string(Image.open(arquivo), lang='por')
        print(phrase)
        saida.write(phrase)
        saida.close()

imageToText()

