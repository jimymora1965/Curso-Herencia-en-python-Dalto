class Clinica:
    def __init__(self,nombre,apellido,especialidad):
        self.n = nombre
        self.a = apellido
        self.esp = especialidad
        
class TipoVinculacion:
    def __init__(self, vinculado, prestacion_de_servicios):
        self.vin = vinculado
        self.ps = prestacion_de_servicios 
        
class Sede:
    def __init__(self, departamento, ciudad):
        self.dpto = departamento
        self.ciu = ciudad
        
class Especialidad:
    def __init__(self, anestesiologo,cirujano, ortopedia):
        self.anes = anestesiologo
        self.cx = cirujano
        self.ort = ortopedia
        
class Galeno(Clinica,TipoVinculacion,Sede,Especialidad):
    def __init__(self,nombre, apellido,especialidad,vinculado, prestacion_de_servicios,departamento,ciudad,anestesiologo,cirujano,ortopedia,salario):
        Clinica.__init__(self,nombre,apellido,especialidad)
        TipoVinculacion.__init__(self,vinculado, prestacion_de_servicios)
        Sede.__init__(self,departamento,ciudad)
        Especialidad.__init__(self,anestesiologo,cirujano,ortopedia)
        self.sal = salario
        

especialista = Galeno("Jimy","Mora","Anestesiologo","Vinculado","Prestador_Servicios","Antioquia","Medellin","Anestesiologo","cirujano","ortopedista",10000)
print(especialista.n,especialista.esp,especialista.ps)
        
        