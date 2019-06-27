class Empresas():
    def __init__(self, codi_emp, nome_emp, tins_emp, cgce_emp, status_emp):
        self._codi_emp = codi_emp
        self._nome_emp = nome_emp
        self._tins_emp = tins_emp
        self._cgce_emp = cgce_emp
        self._status_emp = status_emp

    def setCodiEmp(self, codi_emp):
        self._codi_emp = codi_emp

    def getCodiEmp(self):
        return self._codi_emp

    def setNomeEmp(self, nome_emp):
        self._nome_emp = nome_emp

    def getNomeEmp(self):
        return self._nome_emp

    def setTinsEmp(self, tins_emp):
        self._tins_emp = tins_emp

    def getTinsEmp(self):
        return self._tins_emp

    def setCgceEmp(self, cgce_emp):
        self._cgce_emp = cgce_emp

    def getCgceEmp(self):
        return self._cgce_emp

    def setStatusEmp(self, status_emp):
        self._status_emp = status_emp

    def getStatusEmp(self):
        return self._status_emp

emp1 = Empresas(1, "SOMA", 1, "123456789", "A")
print(emp1.getCodiEmp())