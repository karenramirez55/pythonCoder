class Alumno:

    def __init__(self,nombre,nota):
        self.__nombre=nombre
        self.__nota=nota
    
    def __str__(self):
        return f'El alumno es {self.__nombre} y la nota es {self.__nota}'
        