import xlrd
import os
import re

def buscaArquivosEmPasta(caminho, extensao):
    arquivos = os.listdir(caminho)
    lista_arquivos = []

    for arquivo in arquivos:
        if arquivo.endswith(extensao):
            lista_arquivos.append(caminho+"\\"+arquivo)

    return lista_arquivos

def leXls_Xlsx(arquivos,saida="C:\\programming\\conv-dominio\\arquivos\\teste.csv"):
    saida = open(saida, "w")
    lista_dados = []
    for arquivo in arquivos:
        arquivo = xlrd.open_workbook(arquivo)

        # guarda todas as planilhas que tem dentro do arquivo excel
        planilhas = arquivo.sheet_names()

        # lê cada planilha
        for p in planilhas:

            # pega o nome da planilha
            planilha = arquivo.sheet_by_name(p)

            # pega a quantidade de linha que a planilha tem
            max_row = planilha.nrows
            # pega a quantidade de colunca que a planilha tem
            max_column = planilha.ncols

            # lê cada linha e coluna da planilha e imprime
            for i in range(0, max_row):

                # ignora linhas em branco
                valor_linha = planilha.row_values(rowx=i)
                if valor_linha.count("") == max_column:
                    continue

                lista_dados.append(valor_linha)

                # lê as colunas
                #for j in range(0, max_column):
                    # pega o valor da célula
                    #cell_obj = planilha.cell_value(rowx=i, colx=j)
                    # gera o resultado num arquivo
                    #resultado = str(cell_obj) + ';'
                    #resultado = resultado.replace('None', '')
                    #saida.write(resultado)

                # faz uma quebra de linha para passar pra nova linha
                #saida.write('\n')
        # fecha o arquivo
    #saida.close()
    return lista_dados