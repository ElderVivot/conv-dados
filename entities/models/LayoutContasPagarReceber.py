import entities.models.Empresas as emp

class LayoutContasPagarReceber:
    def __init__(self, codi_emp, nome="Contas a Pagar e Receber", ):

import tools.funcoes as tf

def trataFornecedorCliente(fornecedor_cliente):
    return tf.trataCampoTexto(fornecedor_cliente)

def trataCNPJFornecedorCliente(cnpj_forn_cli):
    return tf.trataCampoNumero(cnpj_forn_cli)

def trataNota(nota, lista_char=["-","/"]):
    nota = tf.trataCampoTexto(nota)
    for char in lista_char:
        if nota.count(char) > 0:
            nota = nota.split(char)
            nota = nota[0]
            break
    print(nota)
    return tf.trataCampoNumero(nota)

def trataDocumento(documento):
    """
    :param documento: coloque o mesmo campo que é da Nota, pois este será utilizado para montar o histórico
    :return: retorna o campo original tratado
    """
    return tf.trataCampoTexto(documento)

def trataEmissao(emissao):
    return tf.transformaCampoDataParaFormatoBrasileiro(tf.retornaCampoComoData(emissao))

def trataVencimento(vencimento):
    return tf.transformaCampoDataParaFormatoBrasileiro(tf.retornaCampoComoData(vencimento))

def trataBaixa(baixa):
    return tf.transformaCampoDataParaFormatoBrasileiro(tf.retornaCampoComoData(baixa))

def trataBancoPlanilha(banco_planilha):
    return tf.trataCampoTexto(banco_planilha)

def trataBancoExtrato(numero_banco, conta):
    return tf.transformaBancoNumeroPraTexto(numero_banco) + "-" + conta

def trataBaixaExtrato(baixa_extrato):
    return tf.transformaCampoDataParaFormatoBrasileiro(tf.retornaCampoComoData(baixa_extrato))

def trataValorOriginal(valor_original):
    return tf.trataCampoDecimal(valor_original)

def trataValorPago(valor_pago):
    return tf.trataCampoDecimal(valor_pago)

def trataValorRecebido(valor_recebido):
    return tf.trataCampoDecimal(valor_recebido)

def trataValorDesconto(valor_desconto):
    return tf.trataCampoDecimal(valor_desconto)

def trataValorJuros(valor_juros):
    return tf.trataCampoDecimal(valor_juros)

def trataValorMulta(valor_multa):
    return tf.trataCampoDecimal(valor_multa)

def trataOBS(obs):
    return tf.trataCampoTexto(obs)

def trataTipoPagto(tipo_pagto):
    return tf.trataCampoTexto(tipo_pagto)

def trataCategoria(categoria):
    return tf.trataCampoTexto(categoria)