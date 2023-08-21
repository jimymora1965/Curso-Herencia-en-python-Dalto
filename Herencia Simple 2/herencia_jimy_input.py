class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el Nombre:\n ")
        self.edad = int(input("Ingresa la edad:\n "))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

persona1 = Persona()#se crea el objeto
persona1.imprimir()#sse imprime las propiedades del objeto


   

    

        