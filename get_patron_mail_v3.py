import requests
from bs4 import BeautifulSoup
import sys
SCRIPT=sys.argv[0]
print('\n\t\tEjecutando [ '+SCRIPT+' ]\t...\t...\t...\t...\n')
print('Script para buscar los correos electronicos y el nombre del personal que le corresponde por medio de el tag "CLASS".\nPd: Si se desea cambiar el TAG hay que cambiar la validación\n')
if len(sys.argv) != 4:
    print('Ejemplo de uso:')
    print('\t\t'+SCRIPT+' ARG1 ARG2 ARG3')
    print('Donde')
    print('\tARG1: Class_Correo')
    print('\tARG2: Class_Nombre')
    print('\tARG3: URL')
    exit(1)

#VALORES QUE INGRESA EL USUARIO
C_MAIL=sys.argv[1]
C_NAME=sys.argv[2]

#VALORES QUE USA EL PROGRAMA
MAIL_LIST=[]
NAME_LIST=[]
FULL_LIST=[]
try:
    PAGE = requests.get(sys.argv[3])
except:
    print('\t\tError consegir el sitio web...')
    exit(1)

SOUP=BeautifulSoup(PAGE.text, 'html.parser')

#Se toman los valores de los correos
DATA=SOUP.find_all(class_=C_MAIL)
for elemento in DATA:
    CORREOS=elemento.contents[0]
    MAIL_LIST.append(CORREOS)

#Se toman los valores de los nombres
DATA=SOUP.find_all(class_=C_MAIL)
for elemento in DATA:
    NOMBRES=elemento.contents[0]
    NAME_LIST.append(NOMBRES)

#Se invierten las listas, se puede comentar.
MAIL_LIST.reverse()
NAME_LIST.reverse()

for elemento in range(0,len(MAIL_LIST)):
    FULL_LIST.append(MAIL_LIST.pop()+':'+NAME_LIST.pop())

for elemento in FULL_LIST:
    print (elemento)
