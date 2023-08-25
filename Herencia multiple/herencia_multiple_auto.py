class Concesionario:
    def __init__(self, marca, modelo, año):
        self.m = marca
        self.mod = modelo
        self.a = año
        
class TipoAuto:
    def __init__(self, automovil, camioneta):
        self.auto = automovil
        self.cam = camioneta
        
class Concesionario_TipoAuto(Concesionario,TipoAuto):
    def __init__(self,marca,modelo,año,automovil,camioneta,precio,color):
        Concesionario.__init__(self,marca,modelo,año)
        TipoAuto.__init__(self,automovil,camioneta)
        self.pre = precio
        self.col = color
        
aveo = Concesionario_TipoAuto("Chevrolet","Aveo",2009,"automovil","camioneta",10000000,"Verde Bretaña")
print(aveo.m,aveo.a, aveo.pre,aveo.col)

fortuner = Concesionario_TipoAuto("Toyota","Fortuner",2019,"automovil","camioneta",70000000,"Gris")
print(fortuner.m,fortuner.a,fortuner.pre)        
        