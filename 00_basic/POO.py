class Perro:
    
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        print("Llamando getter")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        print("Llamando setter")
        self._nombre = nombre_nuevo

    @nombre.deleter
    def nombre(self):
        print("Llamando deleter")
        del self._nombre
        
        