import unittest
class MenorEdadException(Exception):
    pass

class Persona:
    def __init__ (self, nombre, apellido, edad):
        if edad < 18:
            raise MenorEdadException(" La persona es menor de edad")
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

if __name__ == '__init__':
    unittest.main()