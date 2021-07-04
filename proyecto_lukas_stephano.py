<<<<<<< Updated upstream
print('Bienvenido a tu informativo de los datos actualizados sobre el covid-19 en Chile','\n','Aquí se mostrara información sobre el proceso de vacunación en Chile')
print('Elija una de las siguientes tres opciones')
print(' 1-Informacion por region sobre la vacunación','\n','2-Información general de la vacunación en Chile')
y = input()
while not y.isnumeric():
    print('Debe ingresar un valor valido porfavor')
    y = input()
while int(y) <=0 or int(y) >4:
    print('Ingrese un valor valido porfavor')
    y = input()
if y=='1':
    print('Estas son las regiones de chile:','\n','15-Arica y parinacota','\n','1-Tarapaca','\n','2-Antofagasta','\n','3-Atacama','\n','4-Coquimbo','\n','5-Valparaiso','\n','13-Metropolitana','\n',"6-Bernardo O'higgins",'\n','7-Maule','\n','8-Bío bío','\n','9-Araucania','\n','14-Los rios','\n','10-Los lagos','\n','11-Aysen','\n','12-Magallanes')
    print('Seleccione una region para ver la comparación entre la cantidad de personas que se vacunan con la primera dosis y la segunda dosis')
    x = input()
    while not x.isnumeric():
        print('Debe ingresar un valor valido porfavor')
        x = input()
    while int(x) <=0 or int(x) >15:
        print('Ingrese un valor valido porfavor')
        x = input()
    archivo = open('vacunacion_region.csv','r')
    def regiones(x):
        switcher={
            15:'arica y parinacota',
            1:'Tarapaca',
            2:'Antofagasta',
            3:'Atacama',
            4:'Coquimbo',
            5:'Valparaiso',
            13:'Metropolitana',
            6:"Bernardo O'Higgins",
            7:'Maule',
            8:'Bío-bío',
            9:'Araucania',
            14:'Los rios',
            10:'Los lagos',
            11:'Aysen',
            12:'Magallanes'}
        return switcher.get(x,"region invalida")
    
    
    
    

    
    




=======
print('Bienvenido a tu informativo de los datos actualizados sobre el covid-19 en Chile','\n','Aquí se mostrara información sobre el proceso de vacunación en Chile')
print('Elija una de las siguientes tres opciones')
print(' 1-Informacion por region sobre la vacunación','\n','2-Información general de la vacunación en Chile')
y = input()
while not y.isnumeric():
    print('Debe ingresar un valor valido porfavor')
    y = input()
while int(y) <=0 or int(y) >4:
    print('Ingrese un valor valido porfavor')
    y = input()
if y=='1':
    print('Estas son las regiones de chile:','\n','15-Arica y parinacota','\n','1-Tarapaca','\n','2-Antofagasta','\n','3-Atacama','\n','4-Coquimbo','\n','5-Valparaiso','\n','13-Metropolitana','\n',"6-Bernardo O'higgins",'\n','7-Maule','\n','16-Ñuble','\n','8-Bío bío','\n','9-Araucania','\n','14-Los rios','\n','10-Los lagos','\n','11-Aysen','\n','12-Magallanes')
    print('Seleccione una region para ver la comparación entre la cantidad de personas que se vacunan con la primera dosis y la segunda dosis')
    x = input()
    while not x.isnumeric():
        print('Debe ingresar un valor valido porfavor')
        x = input()
    while int(x) <=0 or int(x) >16:
        print('Ingrese un valor valido porfavor')
        x = input()
def regiones(f):
        switcher={
            '15':'Arica y Parinacota',
            '1':'TarapacÃ¡',
            '2':'Antofagasta',
            '3':'Atacama',
            '4':'Coquimbo',
            '5':'ValparaÃ­ so',
            '13':'Metropolitana',
            '6':"Oâ€™Higgins",
            '7':'Maule',
            '16':'Ã‘uble',
            '8':'BiobÃ o',
            '9':'AraucanÃ o',
            '14':'Los RÃ o',
            '10':'Los lagos',
            '11':'AysÃ©n ',
            '12':'Magallanes'}
        return switcher.get(f, 'region invalida')   
t = regiones(x)
archivo = open('vacunacion_region.csv','r')
x = archivo.readlines()
region = t
d = []
for i in (x):
    i = i.split(',')
    if i[0]== region:
        d.append(i)

print(d) #primera y segunda dosis de region en listas
archivo = open('vacunacion_region.csv','r')
linea= archivo.readline()
list(linea)
linea=linea.split(",")

r = d[0]

import matplotlib.pyplot as plt
from numpy import result_type
linea.pop(0)
linea.pop(0)
ejex= linea
r.pop(0)
r.pop(0)
ejey= result_type

plt.title('Cantidad de personas con la segunda dosis')
plt.xticks(rotation = 90)
plt.plot(ejex,ejey)
plt.show()

    





>>>>>>> Stashed changes
