#Aquí definimos todas las funciones para mantener un orden en el código.
def regiones(k): #Esta funcion traduce el número presentado por el usuario a palabras.
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
        return switcher.get(k, 'region invalida')    

def lineas(valor):                              #Esta funcion busca las listas que empiecen con la palabra dada por la funcion anterior, 
    archivo = open('vacunacion_region.csv','r') #de esta manera nos "agarra" solo las listas que necesitamos, o sea, vacunados con primera y segunda dosis por 1 region seleccionada
    x = archivo.readlines() #Se leen todas las lineas del archivo
    region = valor #La palabra traducida se almacena en region
    for i in (x): #se recorre la lista
        i = i.split(',') #se separan mediante las ","
        if i[0]== region: #se verifica que si la posicion [0] = a la region que traducimos se agrega a una lista
            lista_rellenable.append(i) #se agrega

def listas_grafico(): #Esta funcion es tomar las 2 listas que nos interesan (primera y segunda dosis por region) y graficarlas
    archivo = open('vacunacion_region.csv','r')
    fechas= archivo.readline() #se lee la primera linea (fechas)
    list(fechas) #se pasa a lista
    fechas=fechas.split(",") #se separa
    primera_dosis = lista_rellenable[0] #la posicion [0] (o sea la sublista 1(solo primeras dosis)) se alacena en una variable
    segunda_dosis = lista_rellenable[1] #ocurre lo mismo con la posicion[1] (solo segunda dosis)
    fechas.pop(0) #se quitan los 2 primeros elementos que son palabras
    fechas.pop(0)
    primera_dosis.pop(0) #aquí ocurre algo extraño ya que el pop no aparece con su color amarillo normal
    primera_dosis.pop(0)
    segunda_dosis.pop(0)
    segunda_dosis.pop(0)

    import matplotlib.pyplot as plt   #se importa matplotlib para graficar
    results = primera_dosis  #estas 2 operacion son para transformar las listas a int para que no ocurran problemas con los numeros graficados
    primera_dosis_int = [int(i) for i in results]

    results = segunda_dosis
    segunda_dosis_int = [int(i) for i in results]

    fig, ax= plt.subplots() #se llaman a los subplots de matplotlib
    plt.title('Grafico de primera y segunda dosis de la region seleccionada') #y todo esto no son mas que oslo detalles esteticos para el grafico, como lo son los titulos,
    plt.xticks(rotation = 90)                                                 #los nombres de ejes y los colores,etc.
    plt.plot(fechas,primera_dosis_int,color="g",label="Primera dosis")
    plt.legend()  
    ax.set_ylabel("Personas vacunadas")
    plt.plot(fechas,segunda_dosis_int,color="r",label="Segunda dosis")
    plt.legend()  
    ax.set_xlabel("Fechas")
    ax.grid(linestyle = "dashed")
    plt.show()
#Aquí hago un recalco que en esta funcion ocurre un error ya que cuando uno intenta graficar (con las funciones anteriores) las regiones numero 5, 8, 9, 10, 11, 14, 
#tira un error de "list out of range" e intentamos arreglarlo, pero no supimos como solucionar el error , por lo que en esos casos da un error. Nos disculpamos de ante mano

#Damos por inicio el código aquí
print('Bienvenido a tu informativo de los datos actualizados sobre el covid-19 en Chile\nAquí se mostrara información sobre el proceso de vacunación en Chile')
print('Elija una de las siguientes tres opciones') #se printean los respectivos datos del inicio al ejecutar
print('1-Informacion por region sobre la vacunación\n2-Información general de la vacunación en Chile\n3-Comparación de entre regiones')
opcion1 = input() #guardamos el numero del usuario en variable
while not opcion1.isnumeric(): #Estos 2 while lo que hacen es validar que sea un numero y que sea entre 0 y 4
    print('Debe ingresar un valor valido porfavor')
    opcion1 = input()
while int(opcion1) <=0 or int(opcion1) >3:
    print('Ingrese un valor valido porfavor')
    opcion1 = input()

#Aquí empieza la opción 1: esta opcion solo da datos sobre una region en concreto, o osea que grafica la region que solicita el usuario dando datos de cantidad de personas con primera y segunda dosis
if opcion1 =='1': #se pregunta y da todas las regiones de chile con sus respectivos numeros y en orden de norte a sur
    print('Estas son las regiones de chile:\n15-Arica y parinacota\n1-Tarapaca\n2-Antofagasta\n3-Atacama\n4-Coquimbo\n5-Valparaiso\n13-Metropolitana\n6-Bernardo Ohiggins\n7-Maule\n16-Ñuble\n8-Bío bío\n9-Araucania\n14-Los rios\n10-Los lagos\n11-Aysen\n12-Magallanes')
    print('Escriba el número de una region para ver la comparación entre la cantidad de personas que se vacunan con la primera dosis y la segunda dosis') #se despliega la opcion para que el usuario ponga el n° ded reegion que quiere saber info sobre vacunacion
    info_region = input() #numero del usuaario se alacena en una variable
    while not info_region.isnumeric(): #se vuelve a condicionar con while, pero ahora desde el 0 al 16
        print('Debe ingresar un valor valido porfavor')
        info_region = input()
    while int(info_region) <=0 or int(info_region) >16:
        print('Ingrese un valor valido porfavor')
        info_region = input()

    traductor_nr = regiones(info_region) #el numero del usuario se traduce llamando a la funcion y se almacena en una varible
    lista_rellenable = [] #se crea una vareable de lista vacia
    lineas(traductor_nr) #el dato ya traducido se ejecuta en la funcion para sacar las lineas y volverlas listas
    listas_grafico() #y por ultimo se llama a la funcion que grafica para graficar las listas
      
#Aquí empieza la opción 2: esta opcion lo que hace es mas que nada dar informacion nacional sobre la vacunacion
elif opcion1 =='2': #se valida y posteriormente (linea de abajo) se le presentan 4 opciones al usuario para que decida cual ver
    print('ingrese la opción que desee realizar\n1-Mostrar las 5 regiones con el mayor número de personas vacunadas con la primera dosis\n2-Mostrar las 5 regiones con el mayor número de personas vacunadas con la segunda dosis.\n3-Mostrar en un gráfico, la cantidad de personas que se aplican la segunda dosis y las que no\n4-Mostrar la región con mayor número de vacunados totales.')
    info_pais = input() #numero de usuario se almacena
    while not info_pais.isnumeric(): #se verifica que sea desde 0 al 4
        info_pais = input('Debe ingresar un valor valido porfavor',)
    while int(info_pais) <=0 or int(info_pais) >4:
        info_pais = input('Ingrese un valor valido porfavor')
    if info_pais == "1": #en esta opcion se printean las 5 regiones con mayor numero de vacunados con la primera dosis (se printean directamente ya que se sacaron los datos manualmente del documento)
        print("Las 5 regiones con mayor numero de vacunados con la primera dosis al dia de hoy son:\n1-Metropolitana con 860.084 vacunados\n2-Valparaiso con 269.474 vacunados\n3-Biobio con 241.877 vacunados\n4-Maule con 148.009 vacunados\n5-Araucanía con 131.466 vacunados")

    elif info_pais == "2": #esta opcion hace lo mismo que la anterior solo que se printean las 5 regiones con mayor cantidad de vacunados con la segunda dosis
        print("Las 5 regiones con mayor numero de vacunados con la segunda dosis al dia de hoy son:\n1-O’Higgins con 11.353 vacunados\n2-Coquimbo con 8496 vacunados\n3-Metropolitana con 7846 vacunados\n4-Ñuble con 7703 vacunados\n5-Antofagasta con 5885 vacunados")

    elif info_pais == "3": #esta 3ra opcion lo que hace es graficar la cantidad de personas con 1ra y segunda dosis pero a nivel nacional
        #basicamente estos 3 primeros parrafos lo que hacen es leer la linea 1, linea 2, linea 3, borrar las 2 primeras palabras de cada linea y volverlas listas
        archivo = open('vacunacion_region.csv','r')
        linea1 = archivo.readline() #Estas son las fechas
        list(linea1)
        linea1 = linea1.split(",")
        linea1.pop(0)
        linea1.pop(0)

        linea2 = archivo.readline() #Estas son las personas vacunadas con la primera dosis en chile
        list(linea2)
        linea2 = linea2.split(",")
        linea2.pop(0)
        linea2.pop(0)

        linea3 = archivo.readline() #Estas son las persinas vacunadas con la segundas dosis en chile
        list(linea3)
        linea3 = linea3.split(",")
        linea3.pop(0)
        linea3.pop(0)
        
        import matplotlib.pyplot as plt #se llama a matplotlib para graficar y se transforman los elementos de la lista en elementos int
        resultado2 = linea2
        Primerasdosis_int = [int(i) for i in resultado2]

        resultado2 = linea3
        segundasdosis_int = [int(i) for i in resultado2]

        print("De este grafico podemos concluir que", 2320697-55028,"personas no se han vacunado") #acá se printea una conclusion del grafico
        fig, ax= plt.subplots() #mayormente todo esto son detalles esteticos del grafico
        plt.title('Grafico Vacunados a nivel nacional') 
        plt.xticks(rotation = 90)
        plt.yticks([0,200000,400000,600000,800000,1000000,1200000,1400000,1600000,1800000,2000000,2200000,2400000])
        plt.plot(linea1,Primerasdosis_int,color="g",label="Primera dosis")
        plt.legend()
        ax.set_ylabel("Cantidad de personas en millones")
        plt.plot(linea1,segundasdosis_int,color="r",label="Segunda dosis")
        plt.legend() 
        ax.set_xlabel("Fechas")
        ax.grid(linestyle = "dashed")
        plt.show()
   
    elif info_pais =="4": #esta 4ta y ultima sub-opcion de la opcion 2 lo que hace es que printea directamente (ya que los datos se sacaron manualmente del archivo) la region con mas vacunados totales 
        print("La region con mas número de vacunados totales es la región\nMetropolitana con 860.084 vacunados con la primera y\n7846 con la segunda dosis.")

elif opcion1 == "3":#acá recien empieza la 3ra opcion de las 3 principales, la cual es un comparador entre regiones, las grafica una al lado de la otra y le da la info al usuario
    print("Ingrese los números de las 2 regiones las cuales quiere comparar:\n(Ejemplo: 13,15)\n")
    comparacion = input() #se le pide al usuario que escriba las 2 regiones que quiere comparar, lamentablemente para probarlo hay que tener en cuenta las regiones que generan error y no nombrarlas (5,8,9,10,11,14)
    comparacion = comparacion.split(",") #se vuelve una lista el input entregado por el usuario
    primera_region=regiones(comparacion[0]) #Region 1 ya separada,traducida y almacenada en la variable
    segunda_region=regiones(comparacion[1]) #Region 2 ya separada,traducida y almacenada en la variable
    
    lista_rellenable=[] #se crea otra vez una variable lista vacia
    lineas(primera_region) #se llama a la funcion para tomar las lineas del archivo que nos interesan 
    archivo = open('vacunacion_region.csv','r')
    fechas1= archivo.readline() #aca se guardan las fechas
    list(fechas1)#se vuelve lista
    fechas1=fechas1.split(",") #se separan los elementos
    primera_dosis1 = lista_rellenable[0] #se separan las 2 listas
    segunda_dosis1 = lista_rellenable[1]
    fechas1.pop(0) #se borran las palabras del inicio con el .pop
    fechas1.pop(0)
    primera_dosis1.pop(0) #vuelve a estar raro el hecho de que no salga el .pop en su respectivo color amarillo
    primera_dosis1.pop(0)
    segunda_dosis1.pop(0)
    segunda_dosis1.pop(0)

    results1 = primera_dosis1 #los elementos de la lista se vuelven int
    primera_dosis_int1 = [int(i) for i in results1]
    results1 = segunda_dosis1
    segunda_dosis_int1 = [int(i) for i in results1]

    lista_rellenable = [] #se vuelve a crear una lista vacia
    lineas(segunda_region) #se aplica la funcion para sacar las lineas pero ahora para la segunda region ingresada
    archivo = open('vacunacion_region.csv','r') #se vuelve a hacer el mismo procedimiento de la primera region pero ahora con los datos de la segunda
    fechas2= archivo.readline()
    list(fechas2)
    fechas2=fechas2.split(",") 
    primera_dosis2 = lista_rellenable[0] #se almacena cada lista en una varible distinta para poder graficarla
    segunda_dosis2 = lista_rellenable[1]
    fechas2.pop(0)
    fechas2.pop(0)
    primera_dosis2.pop(0)
    primera_dosis2.pop(0)
    segunda_dosis2.pop(0)
    segunda_dosis2.pop(0) #se leen del archivo, se vuelven lista, se separan los elementos, se separan las 2 sub-listas y se eliminan las primeras palabras

    results2 = primera_dosis2
    primera_dosis_int2 = [int(i) for i in results2]
    results2 = segunda_dosis2
    segunda_dosis_int2 = [int(i) for i in results2]

    import matplotlib.pyplot as plt #y por ultimo acá se grafica 
    fig, ax = plt.subplots(2,2,sharey = True)                                  #todo lo de abajo no son mas que detalles esteticos para el grafico, en este caso opté por un grafico 
    ax[0,0].set_ylabel("Primera dosis de primera region seleccionada")         #2x2 en el cual salen 4 recuadros, 2 por region, de tal modo que se vean primeras y segundas dosis por cada region
    ax[0,1].set_ylabel("Segunda dosis de primera region seleccionada")
    ax[1,0].set_ylabel("Primera dosis de segunda region seleccionada")
    ax[1,1].set_ylabel("Segunda dosis de segunda region seleccionada")
    ax[0,0].set_xlabel("Fechas")
    ax[0,1].set_xlabel("Fechas")
    ax[1,0].set_xlabel("Fechas")
    ax[1,1].set_xlabel("Fechas")
    ax[0,0].grid(linestyle = "dashed")
    ax[0,1].grid(linestyle = "dashed")
    ax[1,0].grid(linestyle = "dashed")
    ax[1,1].grid(linestyle = "dashed")
    ax[0,0].plot(fechas1,primera_dosis_int1,color = "g")
    ax[0,1].plot(fechas1,segunda_dosis_int1,color = "g")
    ax[1,0].plot(fechas2,primera_dosis_int2,color = "r")
    ax[1,1].plot(fechas2,segunda_dosis_int2,color = "r")
    plt.show()#y se grafica
    
#aquí se finaliza el codigo, lamentamos los errores pero nos esfrozamos mucho pensando en como lograr esta enredada meta, esperamos que le haya gustado 
#este codigo y su funcionalidad. 
