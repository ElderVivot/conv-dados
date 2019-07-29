from entities.models.Layouts import Layouts

class Aplicattion:
    l = Layouts(1, "Teste Layout")

    l.adiocionaCampoLayouts(1, "teste")
    print(l.__str__())

a = Aplicattion()