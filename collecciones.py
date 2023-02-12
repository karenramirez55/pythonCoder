from collections import namedtuple, Counter
from datetime import datetime
#collections = modulo namedtuple=clase
# modulo import clase -en datetime-

compras=namedtuple("compras",["name","producto","precio"])
mis_compras=compras("Karen","Notbook","U$d 800")
print(mis_compras) #devuelve una tupla

print(mis_compras._asdict()) #devuelve un diccionario aunque a mi me aparece como lista

#############################
lista=[1,5,5,1,1,2,2,3,2,2,1,4]
print(Counter(lista)) # Counter nos devuelve cuantos valores hay de cada elemento que le pasemos

#############################
tiempo=datetime.now() # devuelve fecha y horario actual
print("FECHA Y HORA",tiempo)
print("AÑO",tiempo.year)
print("MES",tiempo.month)
print("DIA",tiempo.day)
#SOLO PARTES DE LA HORA

print("HORA",tiempo.hour)
print("MINUTOS",tiempo.minute)
print("SEGUNDOS",tiempo.second)
print("MICROSEGUNDOS",tiempo.microsecond)
