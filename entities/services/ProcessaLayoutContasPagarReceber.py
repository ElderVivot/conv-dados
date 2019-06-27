import entities.models.LayoutContasPagarReceber as mcpr
import tools.funcoes as tf
import tools.leArquivos as tLerArq

caminho_teste = "C:\\Users\\Elder Vivot Dias\\Downloads\\ARQUIVOS TESTE FRANCESINHA\\BANCO BRADESCO GOLDMAQ"
#caminho_teste = "D:\\temp"

col_nota = -1
for linha in tLerArq.leXls_Xlsx(tLerArq.buscaArquivosEmPasta(caminho_teste, "xls")):
    # este for vai pegar o cabeçalho pelo nome das colunas
    for k, value in enumerate(linha):
        value = tf.trataCampoTexto(value)
        if value == tf.trataCampoTexto("Seu Número"):
            col_nota = k

    print(mcpr.trataNota(linha[col_nota]))