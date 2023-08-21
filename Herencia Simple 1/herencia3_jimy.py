class Farmacos:
    def __init__(self,nombre, tipo_medicamento, valor):
        self.n= nombre
        self.tm = tipo_medicamento
        self.val = valor

class Medicamentos(Farmacos):
    def __init__(self, nombre, tipo_medicamento, valor, presentacion):
        super().__init__(nombre, tipo_medicamento, valor)
        self.p = presentacion

dolor = Medicamentos("Acetaminofen\n","Analgesico_Antipiretico\n", "Caja x 10 tabletas\n",3000)
beta= Medicamentos("Propranolol\n","Betabloqueador\n","Caja por 30 tabletas de 40mgs\n", 10500)


print(dolor.n,dolor.tm,dolor.val,dolor.p)

print("*********************************")
print("*********************************")

print(beta.n,beta.tm,beta.val,beta.p)