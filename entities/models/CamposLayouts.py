class CamposLayouts(object):

    def __init__(self, id, name, tipoCampo, formatoData='dd/mm/aaaa', campoNaLinhaPrincipal='S', \
        posicaoInicialLinha=0, posicaoFinalLinha=0, tipoComparacaoLinha=1, buscaDadoPor=1, nomeColuna='', \
        posicaoInicial=0, posicaoFinal=0, campoComMaisDeUmaInformacao='N', \
        caracteresDelimitadoresDasDemaisInformacoes='', posicaoOndeOCampoEsta=0):
        
        self._id = id
        self._name = name
        self._tipoCampo = tipoCampo
        self._formatoData = formatoData
        self._campoNaLinhaPrincipal = campoNaLinhaPrincipal
        self._posicaoInicialLinha = posicaoInicialLinha
        self._posicaoFinalLinha = posicaoFinalLinha
        self._tipoComparacaoLinha = tipoComparacaoLinha
        self._buscaDadoPor = buscaDadoPor
        self._nomeColuna = nomeColuna
        self._posicaoInicial = posicaoInicial
        self._posicaoFinal = posicaoFinal
        self._campoComMaisDeUmaInformacao = campoComMaisDeUmaInformacao
        self._caracteresDelimitadoresDasDemaisInformacoes = caracteresDelimitadoresDasDemaisInformacoes
        self._posicaoOndeOCampoEsta = posicaoOndeOCampoEsta
        self.camposLayout = []

    def getId(self):
        return self._id
    
    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name

    def setTipoCampo(self, tipoCampo):
        self._tipoCampo = tipoCampo

    def getTipoCampo(self):
        return self._tipoCampo

    def setFormatoData(self, formatoData):
        self._formatoData = formatoData

    def getFormatoData(self):
        return self._formatoData

    def setCampoNaLinhaPrincipal(self, campoNaLinhaPrincipal):
        self._campoNaLinhaPrincipal = campoNaLinhaPrincipal

    def getCampoNaLinhaPrincipal(self):
        return self._campoNaLinhaPrincipal

    def setPosicaoInicialLinha(self, posicaoInicialLinha):
        self._posicaoInicialLinha = posicaoInicialLinha

    def getPosicaoInicialLinha(self):
        return self._posicaoInicialLinha

    def setPosicaoFinalLinha(self, posicaoFinalLinha):
        self._posicaoFinalLinha = posicaoFinalLinha

    def getPosicaoFinalLinha(self):
        return self._campoFinalLinha

    def setTipoComparacaoLinha(self, tipoComparacaoLinha):
        self._tipoComparacaoLinha = tipoComparacaoLinha

    def getTipoComparacaoLinha(self):
        return self._tipoComparacaoLinha

    def setBuscaDadoPor(self, buscaDadoPor):
        self._buscaDadoPor = buscaDadoPor

    def getBuscaDadoPor(self):
        return self._buscaDadoPor

    def setNomeColuna(self, nomeColuna):
        self._nomeColuna = nomeColuna

    def getNomeColuna(self):
        return self._nomeColuna

    def setPosicaoInicial(self, posicaoInicial):
        self._posicaoInicial = posicaoInicial

    def getPosicaoInicial(self):
        return self._posicaoInicial

    def setPosicaoFinal(self, posicaoFinal):
        self._posicaoFinal = posicaoFinal

    def getPosicaoFinal(self):
        return self._posicaoFinal

    def setCampoComMaisDeUmaInformacao(self, campoComMaisDeUmaInformacao):
        self._campoComMaisDeUmaInformacao = campoComMaisDeUmaInformacao

    def getCampoComMaisDeUmaInformacao(self):
        return self._campoComMaisDeUmaInformacao

    def setCaracteresDelimitadoresDasDemaisInformacoes(self, caracteresDelimitadoresDasDemaisInformacoes):
        self._caracteresDelimitadoresDasDemaisInformacoes = caracteresDelimitadoresDasDemaisInformacoes

    def getCaracteresDelimitadoresDasDemaisInformacoes(self):
        return self._caracteresDelimitadoresDasDemaisInformacoes

    def setPosicaoOndeOCampoEsta(self, posicaoOndeOCampoEsta):
        self._posicaoOndeOCampoEsta = posicaoOndeOCampoEsta

    def getPosicaoOndeOCampoEsta(self):
        return self._posicaoOndeOCampoEsta