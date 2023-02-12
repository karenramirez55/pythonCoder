
class Cliente:

    def __init__(self,nombre,apellido,dni,mail,lugar,preferencias):

        self.__nombre=nombre #
        self.__apellido=apellido #
        self.__dni=dni #
        self.mail=mail #
        self.lugar=lugar
        self.preferencias=preferencias


    def correo(self):
        #character="@"
            if "@" in self.mail: #IN DEVUELVE TRUE SI UN ELEMENTO SE ENCUENTRA DENTRO DE OTRO       
                return self.mail
            else:
                return "Mail invalido falta @"

    def get_correo(self):
        return self.mail

    def set_correo(self,mail):
        self.mail=mail

          
    def data(self):
                
        if type(self.__nombre)==str: #SIEMPRE PYTHON QUIERE EL TIPO DE DATO para poder validar
            return (f'Nombre: {self.__nombre}')   #RECORDAR EL RETURN        
        else:
            return "Escriba el nombre correctamente"
    
    def get_data(self):
        return self.__nombre
    
    def set_data(self,nombre):
        self.__nombre=nombre

             
        # Otra manera de validar con isinstance()
    def last_name(self):
        if isinstance(self.__apellido,str): #no funciona
            return (f'Apellido: {self.__apellido}')                       
        else:
            return "Escriba el apellido correctamente" 
            

    def get_last_name(self):
        return self.__apellido
    
    def set_last_name(self,apellido):
        self.__apellido=apellido

    def lugar_de_compra(self):
        return f'lugar de compra: {self.lugar}'


    def interes(self):
        return self.preferencias #sera unn array porque pueden ser varias

    
    def id(self):
        if len(str(self.__dni)) >= 9 or  len(str(self.__dni)) < 1:
            return "Longitud erronea"
        else:
            return self.__dni
        
    def get_id(self):   
        return self.__dni

    def set_id(self,dni):
        self.__dni=dni
    
    def __str__(self):
        return f'Nombre: {self.__nombre} Apellido: {self.__apellido} Dni: {self.__dni} Mail: {self.mail} Lugar de compras: {self.lugar} preferencias: {self.preferencias}'



