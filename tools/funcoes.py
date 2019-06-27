import unicodedata
import re
import datetime

def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra).encode('ASCII', 'ignore').decode('ASCII')
    palavraTratada = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com valores corretos
    return re.sub('[^a-zA-Z0-9.!+)(/*,\- \\\]', '', palavraTratada)

def trataCampoTexto(valor_campo):
    valor_campo = str(valor_campo)
    return removerAcentosECaracteresEspeciais(valor_campo.strip().upper())

def trataCampoNumero(valor_campo):
    return re.sub('[^0-9\\\]', '', valor_campo)

def trataCampoDecimal(valor_campo, qtd_casa_decimais=2):
    valor_campo = str(valor_campo)
    valor_campo = re.sub('[^0-9.,\\\]', '', valor_campo)
    contador = 0
    ja_passou_por_um_ponto = 0
    if valor_campo.count('.') > 1:
        valor_campo = valor_campo.replace('.', '')
        valor_campo = valor_campo.replace(',', '.')
    else:
        for char in valor_campo:
            if ja_passou_por_um_ponto == 1:
                contador += 1
                if contador >= 3:
                    valor_campo = valor_campo.replace('.', '')
                    valor_campo = valor_campo.replace(',', '.')
                    break
            if char == ".":
                ja_passou_por_um_ponto = 1
        if contador < 3:
            valor_campo = valor_campo.replace(',', '.')

    valor_campo = float(valor_campo)

    return f"{valor_campo:.{qtd_casa_decimais}f}"

def retornaCampoComoData(valor_campo, formato_data=1):
    """
    :param valor_campo: Informar o campo string que será transformado para DATA
    :param formato_data: 1 = 'DD/MM/YYYY' ; 2 = 'YYYY/MM/DD'
    :return: retorna como uma data. Caso não seja uma data válida irá retornar um campo vazio
    """
    valor_campo = str(valor_campo).strip()

    if formato_data == 1:
        formato_data_str = "%d/%m/%Y"
    elif formato_data == 2:
        formato_data_str = "%Y/%m/%d"

    try:
        return datetime.datetime.strptime(valor_campo, formato_data_str).date()
    except ValueError:
        #print("Data no formato inválido.")
        return ""

def transformaCampoDataParaFormatoBrasileiro(valor_campo):
    """
    :param valor_campo: informe o campo data, deve buscar da função retornaCampoComoData()
    :return: traz a data no formato brasileiro (dd/mm/yyyy)
    """
    try:
        return valor_campo.strftime("%d/%m/%Y")
    except AttributeError:
        return ""

def transformaBancoNumeroPraTexto(valor_campo):
    valor_campo = int(trataCampoNumero(valor_campo))
    if valor_campo == 104:
        valor_campo = "CAIXA"
    elif valor_campo == 1:
        valor_campo = "BB"
    elif valor_campo == 341:
        valor_campo = "ITAU"
    elif valor_campo == 756:
        valor_campo = "SICOOB"
    elif valor_campo == 748:
        valor_campo = "SICRED"
    elif valor_campo == 422:
        valor_campo = "SAFRA"
    else:
        valor_campo = str(valor_campo) + " - FAZER CORRELACAO"

    return valor_campo

#print(removerAcentosECaracteresEspeciais("~`´abáóõ  ab!+-"))
#print(trataCampoNumero("~adb123     "))
#print(transformaCampoDataParaFormatoBrasileiro(retornaCampoComoData("01/01/18")))
