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
    
    




