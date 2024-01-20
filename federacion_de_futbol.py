import os
os.system('cls')
titulo = """
         ------------------------------------------
         +                                        +
         + BIENVENIDO AL SISTEMA DE PUNTOS FCF SA +
         +                                        +
          ------------------------------------------
"""
equipos = []
nombre = 0
opciones = '1.Agregar equipo\n2. Registro de partidos\n3.Reportes de tabla de posciones\n4.Salir'
sistema_en_uso = True
nfecha = []
fecha_jueg = 0
while sistema_en_uso:
    os.system ('cls')
    print (titulo)
    print (opciones)
    op = int (input('Ingrese el operador que desea utilizar '))
    if (op == 1):
        local = str(input('Digite el nombre del equipo que quiere agregar '))
        equipos.append([local,0,0,0,0,0,0,0]) #esta linea de codigo le agrega un pj,pg... a cada uno de los equipos que se añada a la lista
        print ('su equipo ha sido registrado correctamente')
        os.system('pause')
    elif(op == 2):
        fecha_juego = int (input('Ingerese el numero de fecha '))
        nfecha.append([fecha_juego])
        local = str (input('Ingrese el nombre del equipo local '))
        marcador1 = int (input ('ingrese el numero de goles que marcó el equipo local '))
        visitante = str(input('Ingrese el nombre del equipo visitante '))
        marcador2 = int (input ('ingrese el numero de goles que marcó el equipo visitante '))
        for i,item in enumerate(equipos):
            if (local in item):
                if (marcador1>marcador2):
                    item[1]+= 1
                    item[2]+= 1
                    item[3]+= marcador1
                    item[4]+= marcador2
                    item[7]+= 3
                if (marcador2>marcador1):
                     item[4]+= marcador2
                     item[5]+= 1
            elif (visitante in item):        
                if (marcador2>marcador1):
                    item[1]+= 1
                    item[2]+= 1
                    item[3]+= marcador2
                    item[4]+= marcador1
                    item[7]+= 3
                if (marcador2<marcador1):
                    item[1]+=1
                    item[3]+= marcador2
                    item[4]+= marcador1
                    item[5]+= 1
        else:
                if (local in item):
                    item[1]+= 1
                    item[3]+=marcador1
                    item[4]+=marcador2
                    item[6]+= 1
                    item[7]+= 1
                elif (visitante in item):
                    item[1]+= 1
                    item[3]+=marcador2
                    item[4]+=marcador1
                    item[6]+= 1
                    item[7]+= 1
    elif(op == 3):
        print ('Reporte de tabla de posciones')
        import os
        from tabulate import tabulate
        print(tabulate(equipos,headers=['Equipo','PJ','PG','GF','GC','PP','PE','TP']))
        for i,item in enumerate(equipos):
            for j in range(int(i+1),len(equipos),1):
                if (equipos[i][4] < equipos[j][4]):
                    aux = equipos[i]
                    equipos [i] =equipos [j]
                    equipos[j] = aux
            mayorgol = equipos[0][0]    
            print (f'El equipo con mas goles fue {mayorgol} ')

        for i,item in enumerate(equipos):
            for j in range(int(i+1),len(equipos),1):
                if (equipos[i][7] < equipos[j][7]):
                    aux = equipos[i]
                    equipos [i] =equipos [j]
                    equipos[j] = aux
            mayorpuntos = equipos[0][0]    
            print (f'El equipo con mas puntos fue {mayorpuntos} ')

        for i,item in enumerate(equipos):
            for j in range(int(i+1),len(equipos),1):
                if (equipos[i][2] < equipos[j][2]):
                    aux = equipos[i]
                    equipos [i] =equipos [j]
                    equipos[j] = aux
            mayorpartidos = equipos[0][0]    
            print (f'El equipo que mas partidos gano fue {mayorpartidos} ')
        os.system('pause')

        for item in equipos:
            sumaequipos += item[4]
            division += 1
            promedio = sumaequipos/division
            print(f'El promedio de goles de los equipos fue {promedio}')
    elif (op ==4):
        sistema_en_uso = False
        print ('muchas gracias por hacer uso del sofware')
        os.system('pause')
    else:
        os.system('cls')
        print ('Digitacion de opcion no valida')
        os.system('pause')
# #acceder a un elemento de la lista 
# print (numero[0])