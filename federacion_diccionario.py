import os
import json

federacion ={}

grupos = {
    "A": [],
    "B": []
}
fechas_de_juego = {
}
partido = {

}
fecha = 0
menu = ("1.Agregar equipo","2.Crear grupos","3.fechas de juego","4.Salir")
#Equipo PJ PP PE PG GF GC
#update o Agregar o Modificar informacion en el diccionario
isAddTeam = True
isActive = True
local = 0
visitante = 0
mensaje = """
    ++++++++++++++++++++++++++++++++++
    + TORNEO BETPLAY - COLOMBIA 2024 +
    ++++++++++++++++++++++++++++++++++
"""
while isActive :
    os.system('cls')
    print(mensaje)
    for item in menu:
        print(item)
    op = int(input(":)_"))
    if (op == 1):
        isAddTeam = True
        while isAddTeam:
            os.system('cls')
            nombre= input("Ingrese el nombre del equipo ")
            equipo={
                'nombre' : nombre,
                'pj':0,
                'pp':0,
                'pe':0,
                'pg':0,
                'gf':0,
                'gc':0,
                'estado':0
            } 
            federacion.update({str(len(federacion)+1).zfill(4):equipo})
            isAddTeam = bool(input("Desea continuar agregando mas equipos S(Si) o Enter(No) "))

    elif (op == 2):
        for key,valor in federacion.items():
            if valor['estado']== 0:
                os.system('cls')
                print(f"Seleccione el grupo al que quiere ingresar el equipo {valor['nombre']}")
                for key2 in grupos:
                    if (len(grupos[key2])) < 4:  #len permite obtener cantidad de elementos que hay en una cadena de caracteres
                        print(f'{key2}. grupo {key2}')
                grp = input(':)_').upper()
                equip = {
                    'codeEquipo' : key,
                    'nombre' : valor['nombre']
                }
                federacion.get(key)['estado'] = 1
                grupos.get(grp).append(equip)
        os.system('pause')
    elif (op == 3):
        print('Ingreso de fechas de juego')
        input('Ingrese la fecha de juego YYY-MM-DD ')
        fechas_de_juego.update({fecha:[]})
        local = str (input('Ingrese el nombre del equipo local ')).upper()
        marcador_local = int (input('Ingrese el marcador del local '))
        visitante = (input('Ingrese el nombre del vistante ')).upper()
        marcador_visitante = int (input('Ingrese el marcador del visitante '))
        partido.update({'local':[local,marcador_local]}) #actualizar un elemento se debe usar la estructura .updated({'nombre para el dato en la biblioteca':[dato]})
        partido.update({'visitante':[visitante,marcador_visitante]})
        fechas_de_juego[fecha].append(partido) # por que no hace referencia al valor que le estoy agregando de fecha de juego
        print(fechas_de_juego)
        os.system ('pause')
    elif(op == 4):
        isActive = False


print(json.dumps(federacion,indent=4))


# fecha = input('Ingrese la fecha de juego YYY-MM-DD')
# fechasdejuego.update({fechas:[]})
# encuentro ={}
# local = input ('Ingrese vistante')
# encuentro.update({'local':[local,3]})
# print(encuentro)
# visitante = input ('ingrese visitante')
# encuentro.update({'visitante':[visitante,3]})
# fechasJuego.get(fechas).append(encuentro)
# print(fechasjuego)