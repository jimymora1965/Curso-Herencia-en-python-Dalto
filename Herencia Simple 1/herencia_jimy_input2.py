class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el Nombre:\n ")
        self.edad = int(input("Ingresa la edad:\n "))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        
persona1 = Persona()
persona1.imprimir()

class Empleado(Persona):
    def __init__(self):
        super().__init__()#este hace que se repita el nombre porque es clase hija
        self.sueldo = float(input("Ingresa el Salario:\n" ))

    def imprimir(self):
        super().imprimir

    def pagaImpuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No para impuestos")
   
empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagaImpuestos()

         
# Tareas: mejorar  el codigo que no se repita el nombre ni la edad y que alhacer print incluya
# el nombre del empleado

