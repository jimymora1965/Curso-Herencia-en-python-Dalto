class Clinica:
    def __init__(self, nombre, apellido, especialidad):
      self.n = nombre 
      self.a = apellido 
      self.esp = especialidad
      
    
class Sede:
    def __init__(self, departamento, ciudad):
       self.d = departamento
       self.e = ciudad
class Universidad: 
    def __init__(self,javeriana, nacional, antioquia):
       self.j = javeriana 
       self.nal = nacional 
       self.ant = antioquia 
class Galeno(Clinica,Sede,Universidad):
    def __init__(self,nombre,apellido,especialidad,departamento,ciudad,javeriana,nacional,antioquia, salario):
       Clinica.__init__(self,nombre,apellido,especialidad)
       Sede.__init__(self,departamento,ciudad)
       Universidad.__init__(self,javeriana,nacional,antioquia)
       self.sal = salario
   
  
ginecologo = Galeno("Felipe","Petro","Ginecologo","Antioquia","Medellin","Javeriana","Nacional","Antioquia",10000000)


print(ginecologo.n,ginecologo.a,ginecologo.j,ginecologo.esp)




