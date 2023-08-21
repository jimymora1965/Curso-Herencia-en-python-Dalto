class Persona:
    def __init__(self):
        self.n = input("Ingrese el nombre:\n")
        self.e = input("Ingrese la edad:\n")
        self.sueldo = float(input("Ingresa el Salario:\n" ))
        
    def nombreEdad(self):
        print("Nombre: ", self.n)        
        print("Edad: ", self.e)
        
    def imprimirNombreEdad(self):
        print(f"Hola {self.n} tienes {self.e} años")
      
    def salarioDevengado(self):
        print("Salario mensual devengado: $",self.sueldo)
        
    def pagaImpuestos(self):
        if self.sueldo < 1000000:
            print(f"'NO' debe pagar impuestos")
        else:
            print("'SI' debe pagar impuestos")
            
    def valorImpuestos(self):
        if self.sueldo >= 1000000 and self.sueldo < 5000000:
            total = self.sueldo * 0.1
            print(f"El trabajador {self.n} debe pagar en impuestos: $",total)
        elif self.sueldo >= 5000000 and self.sueldo <= 10000000:
            total = self.sueldo * 0.15
            print(f"El trabajador {self.n} debe pagar en impuestos: $",total)
        elif self.sueldo > 10000000:
            total = self.sueldo * 0.2
            print(f"El trabajador {self.n} debe pagar en impuestos: $",total)
        else:
            print("Ingrese un valor válido")    
                    
persona1 = Persona() 
persona1.nombreEdad()   
persona1.imprimirNombreEdad()
persona1.salarioDevengado()
persona1.pagaImpuestos()
persona1.valorImpuestos()
print(persona1)

