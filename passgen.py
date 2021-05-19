#modulos
import random
import string

print('\n\t=  Generador de contraseñas  =')

#Entrada de datos
longitud = int(input('\nIngresar la longitud de la contraseña: '))

#Definicion del tipo de datos integrados en el generador
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#Combinacion definiciones
all = lower + upper + num + symbols

#Variable temporal
temp = random.sample(all, longitud)

#all = string.ascii_letters + string.digits + string.punctuation
#pass = "".join(random.sample(all,length))

#Se asigna a password
password = "".join(temp)

#Imprime la contraseña generada
print(password)
