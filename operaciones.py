import os 
os.system('cls')
titulo = """
    ++++++++++++++++++++++++++++
    +  OPERACIONES CON LISTAS  +
    ++++++++++++++++++++++++++++
"""
opciones = '1.Agregar camper\n2. Eliminar camper\n3. Buscar camper\n4. Salir'
isActivate = True 
campers = []
while isActivate:
    os.system('cls')
    print (titulo)
    print(opciones)
    op = int (input('ingrese la opcion de su eleccion '))
    if (op == 1):
        id = str(len(campers)).zfill(5) # esto es para darle un id a cada uno de los campers con 5 ceros
        nombre = input ('Ingrese el nomre del camper ')
        campers.append([id,nombre])
    elif (op == 2):
        nombre = input ('Ingrese el nombre del camper a eliminar ')
        for i,item in enumerate (campers): # for i, item es igual a: para elemento, en la lista, enumarte le da la posicion del elemento y del valor de cada poscicon
            if (nombre in item):
                campers.pop(i)
                break
    elif (op == 3):
        nombre = input ('Ingrese el nombre del camper a buscar ')
        for item in campers:
            if ( nombre in item):
                print (f'codgio {item[0]}')
                print (f'nombre {item[1]}')
                os.system('pause')
    elif (op == 4):
        isActivate = False
        print ('Muchas gracias por usar el programa')
        os.system('pause')
    else:
        os.system('cls')
        print('La opcion ingresada no es valida')
        os.system('pause')