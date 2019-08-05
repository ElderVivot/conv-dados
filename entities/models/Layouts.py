from entities.models.CamposLayouts import CamposLayouts
from entities.enuns.TipoCampo import TipoCampo

class Layouts():

    def __init__(self, id, name, separadorCampos='', informacoesNecessariasMesmaLinha='S', vinculoComFiscal='N'):
        self._id = id
        self._name = name
        self._separadorCampos = separadorCampos
        self._informacoesNecessariasMesmaLinha = informacoesNecessariasMesmaLinha
        self._vinculoComFiscal = vinculoComFiscal
        self._camposLayouts = []

    def getId(self):
        return self._id
    
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setSeparadorCampos(self, separadorCampos):
        self._separadorCampos = separadorCampos

    def getSeparadorCampos(self):
        return self._separadorCampos

    def setInformacoesNecessariasMesmaLinha(self, informacoesNecessariasMesmaLinha):
        self._informacoesNecessariasMesmaLinha = informacoesNecessariasMesmaLinha

    def getInformacoesNecessariasMesmaLinha(self):
        return self._informacoesNecessariasMesmaLinha

    def setVinculoComFiscal(self, vinculoComFiscal):
        self._vinculoComFiscal = vinculoComFiscal

    def getVinculoComFiscal(self):
        return self._vinculoComFiscal

    def getCamposLayouts(self, id):
        return self._camposLayouts[id-1]

    def adiocionaCampoLayouts(self, id, name, tipoCampo=TipoCampo.TEXTO, formatoData='dd/mm/aaaa', campoNaLinhaPrincipal='S', \
        campoInicialLinha=0, campoFinalLinha=0, tipoComparacaoLinha=1, buscaDadoPor=1, nomeColuna='', \
        posicaoInicial=0, posicaoFinal=0, campoComMaisDeUmaInformacao='N', \
        caracteresDelimitadoresDasDemaisInformacoes='', posicaoOndeOCampoEsta=0):

        self._campoLayout = CamposLayouts(id, name, tipoCampo, formatoData, campoNaLinhaPrincipal, campoInicialLinha, \
                                    campoFinalLinha, tipoComparacaoLinha, buscaDadoPor, nomeColuna, posicaoInicial, \
                                    posicaoFinal, campoComMaisDeUmaInformacao, caracteresDelimitadoresDasDemaisInformacoes, \
                                    posicaoOndeOCampoEsta)

        self._camposLayouts.append(self._campoLayout)

    #def __str__(self):
    #    for value in self._camposLayouts:
