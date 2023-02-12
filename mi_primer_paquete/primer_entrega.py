#Crear un programa que permita emular el registro y almacenamiento de 
#usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, 
#diccionarios, bucles y condicionales.

#El formato de registro es: Nombre de usuario y Contraseña.
#Utilizar una función para almacenar la información y otra función para mostrar la información.
#Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
#Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
import json


ruta= './'

#ingrese nombre de usuario  y contraseña
def registro(mi_data):
    usuario=input("Ingrese usuario ")
    password=input("Ingrese contraseña ")
    mi_data.update({usuario:password}) #update agrega un nuevo dict o uno si es q no habia nada
    return mi_data

def leer_data(mi_data):
#la info almacenada en la DB es: PROFE 12345 ALUMNO: 123 TUTOR 567
    print("La info almacenada en la base de datos es:")
    for key in mi_data.keys(): #keys itera dict (clave valor)
        print("El usuario es ",key)
        print("La contraseña es",mi_data[key]) #MI_DATA ES LA CLAVE MADRE
#NO SE COMO HACER PARA QUE EN EL PRINT FINAL SE ME LEA LA CONTRASEÑA COMO VALUE TOMA EL NOMBRE

def guardar_archivo(mi_data):
    
    with open(ruta+"primer_ENTREGA.json", "w") as json_file:
            json.dump(mi_data, json_file, indent=4)

#NO ME IMPORTA EL JSON NO SE DE QUE MANERA LLAMARLO
def login(mi_data):
    nombre=input("ingrese su usuario ")
    clave = input("Ingrese su contraseña: ")
    if nombre in mi_data.keys() and clave==mi_data[nombre]:
        return "iniciaste sesion"
    else:
        return "datos incorrectos."

# almacenamiento={}

# print("Registrando...")
# almacenamiento=registro(almacenamiento)
# leer_data(almacenamiento)

# print("iniciando sesion...")
# resultado=login(almacenamiento)
# print(resultado)
# guardar_archivo(almacenamiento)