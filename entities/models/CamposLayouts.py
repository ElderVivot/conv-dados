class CamposLayouts:

    def __init__(self, id, name, tipoCampo, formatoData='dd/mm/aaaa', campoNaLinhaPrincipal='S', \
        campoInicialLinha=0, campoFinalLinha=0, tipoComparacaoLinha=1, buscaDadoPor=1, nomeColuna='', \
        posicaoInicial=0, posicaoFinal=0, campoComMaisDeUmaInformacao='N', \
        caracteresDelimitadoresDasDemaisInformacoes='', posicaoOndeOCampoEsta=0):
        
        self._id = id
        self._name = name
        self._tipoCampo = tipoCampo
        self._formatoData = formatoData
        self._campoNaLinhaPrincipal = campoNaLinhaPrincipal
        self._campoInicialLinha = campoInicialLinha
        self._campoFinalLinha = campoFinalLinha
        self._tipoComparacaoLinha = tipoComparacaoLinha
        self._buscaDadoPor = buscaDadoPor
        self._nomeColuna = nomeColuna
        self._posicaoInicial = posicaoInicial
        self._posicaoFinal = posicaoFinal
        self._campoComMaisDeUmaInformacao = campoComMaisDeUmaInformacao
        self._caracteresDelimitadoresDasDemaisInformacoes = caracteresDelimitadoresDasDemaisInformacoes
        self._posicaoOndeOCampoEsta = posicaoOndeOCampoEsta

    def getId(self):
        return self._id
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name

    