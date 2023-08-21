class Persona:
    def __init__(self):
        self. n = input("Nombre del empleado: ")
        self.a = input("Apellidos: ")
        self.s = input("Sede: ")
        self.sal = float(input("Salario devengado: "))
        
    def imprimirDatos(self):
        print(f"Nombre: {self.n} {self.a}")        
        print(f"Sede permanente: {self.s}")
        print(f"{self.n} devenga {self.sal}")
        
        if self.sal < 1000000:
            print("No debe pagar impuestos")
        elif self.sal >= 1000000 and self.sal < 5000000:
            total = self.sal * 0.05
            print("Debes pagar en impuesto: ", total )
        elif self.sal >= 5000000 and self.sal < 10000000:
            total = self.sal * 0.1
            print("Debes pagar en impuesto: ", total)
        elif self.sal >= 10000000 and self.sal < 20000000:
            total = self.sal * 0.15
            print("Debes pagar en impuesto: ", total)
        elif self.sal >= 20000000:
            total = self.sal * 0.2
            print("Debes pagar en impuesto: ", total)
        else:
            print("Ingresa un valor valido")    
           
           
        
cajero1 = Persona()
cajero1.imprimirDatos()

        
        
        