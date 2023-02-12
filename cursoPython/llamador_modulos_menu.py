from mi_primer_paquete  import primer_entrega,segunda_entrega # No se lee por consola
#aca tengo que llamar desde la carpeta que se encuentre, tengo que seguir la ruta de donde estan
#guardados los modulos
#PACKAGE = paquete
#los package redistribuibles son los que bajamos de INTERNET de codigo abierto

 #No me deja ver el metodo por consola
cliente1=segunda_entrega.Cliente("KA","Ramirez",37314382,"karg@mail.com","fravega",["electronica,deportes"])
print(cliente1) 
print(cliente1.lugar_de_compra())#NO SE LEE POR CONSOLA.
print(cliente1.data())
print(cliente1.id())
print(cliente1.last_name())
print(cliente1.correo())


cliente1.set_data="pepe"
print(cliente1.set_data) #DE ESTA MANERA SETEO EL NOMBRE SIN MODIFICAR EL MODULO ORIGINAL
#si o si va acompañado primero del Get

almacenamiento={}
print("Registrando...")
almacenamiento=primer_entrega.registro(almacenamiento)
primer_entrega.leer_data(almacenamiento)

print("iniciando sesion...")
resultado=primer_entrega.login(almacenamiento)
print(resultado)
primer_entrega.guardar_archivo(almacenamiento)


# Problema que tenia : si vamos a importar un solo modulo seria asi: from mi_primer_paquete import * o import Cliente o nombre de la clase que desee llamar
# si importamos dos o mas le indicamos nombre de la carpeta e importamos la carpeta que le sigue o archivo como hicimos ahora
# y desp tenemos que llamar desde el archivo primer_entrega en este caso cada variable que creamos con sus funciones.