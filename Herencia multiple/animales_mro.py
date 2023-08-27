class Animal:
    def mamifero(self):
        print("Los mamiferos toman leche")
        
class Ave:
    def olar(self):
        print("Las Aves vuelan")
        
class Pez():
    def nadar(self):
        print("Los peces nadan")
        
class Carnivoro:
    def carnivoro(self):
        print("Los carnivoros comen carne")
        
class Perro(Animal,Carnivoro):
    pass

lobo = Perro()
lobo.mamifero()
lobo.carnivoro()
print(lobo)

print(Perro.mro())