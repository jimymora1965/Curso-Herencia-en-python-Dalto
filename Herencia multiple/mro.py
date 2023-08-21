""" mro = method resolution order:
    es la forma en que python lee los archivos si por ejemplo 
    varias clases tiene los mismos metodos, las mismas  
    propiedades. define el orden de lectura cuando se ejecuta 
    el codigo. Es la forma en que python busca métodos y atributos """
    
""" class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
class C(A) :
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar() #lee el codigo desde la clase D """

""" class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
class C(A) :
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    pass #con pass la prioridad la tiene la clase B, sin pass la clase D
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

print(D.mro()) me muestra el orden en que seran llamadas las clases por python """

""" class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class F(A) :
    def hablar(self):
        print("Hola desde F")


class C(F) :
    def hablar(self):
        print("Hola desde C")

        
class D(B,C):
   # pass #con pass la prioridad la tiene la clase B, sin pass la clase D
    def hablar(self):
        print("Hola desde D")
        
d = D()
d.hablar()

print(D.mro())
 """
 
 
#para llamar una clase anterior a la ultima que leera python lo hago así:
class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class F(A) :
    def hablar(self):
        print("Hola desde F")

class C(F) :
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):   
    def hablar(self):
        print("Hola desde D")

#d = D() #este es el objeto de la clase
B.hablar(F)# utilizo el objeto para llamar la clase que deseo.