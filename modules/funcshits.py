# ################################################### #
#                                                     #
#           ..#######..########.##.....##             #
#           .##.....##.##.......##.....##             #
#           ........##.##.......##.....##             #
#           ..#######..######...#########             #
#           .##........##.......##.....##             #
#           .##........##.......##.....##             #
#           .#########.##.......##.....##             #
#                                                     #
#       Facebook checker v2.0 - coded by 2FH          #
#                                                     #
#   Proyecto: Facebook checker                        #
#   Autores: def Empty(): - YaderPR~                  #
#   Grupo: Two Factor Hack (2FH)                      #
#   Hora: 7:17 PM                                     #
#   Fecha: 21 de Julio del 2020.                      #
#                                                     #
# ################################################### #

if (__name__ == '__main__'): exit();

import requests
from re import match
from . import colors as color

def isNPH(nph): return (True if (match("^\+[0-9]{3,}?[0-9]{8,}$", nph)) else False);

def isEmail(email): return (True if match("^[^@ ]+@[^@ ]+\.[a-zA-Z]{2,}$", email) else isNPH(email));

def isPass(passw): return (True if match("^[\d\D\w\W\s\S]{6,}$", passw) else False);

def credsFilter(email, passw):

        set = color.Color()

        print(set.amarillo + "Filtrando credenciales... ", end = ""+set.reset);

        if (isEmail(email) and isPass(passw)): print(set.verde + "¡Filtrado exitoso!"); return True;
        elif (not (isEmail(email) or isPass(passw))): print(set.rojo + "Correo y contraseña no válidos"+set.reset);
        elif (not isEmail(email)): print(set.rojo + "El correo no es válido"+set.reset);
        else: print(set.rojo + "La contraseña no es válida"+set.reset);

        return False;

def toIterableList(location):

    try:

        if (location):

            set = color.Color()
             
            lista = [];

            file = open(location, "r+");

            print(set.amarillo + "\nExtrayendo credenciales de " + set.azul + location, end = f"{set.amarillo}... ");

            for i in file: lista += [i[:-1] if ("\n" in i[(len(i) - 1):]) else i];

            file.close()

            print(set.verde + "¡Extracción exitosa!" + set.reset);

        return [lista, len(lista)];

    except: return [[],0];

def listFilter(location):

    set = color.Color()
    
    lista = toIterableList(location);
    listaLen = lista[1];
    listaCont = lista[0];

    if (listaLen != 0):

        emails = [];
        passws = [];

        print(set.amarillo + "Filtrando credenciales... ", end = "");

        for i in listaCont:

            email = i[: i.find(":")];
            passw = i[i.find(":") + 1 :];

            if (isEmail(email) and isPass(passw)): emails.append(email); passws.append(passw);

        print(set.verde + "¡Filtrado exitoso!" + set.reset)
        print(set.morado + "Total de credenciales extraidas: " + str(len(emails)) + "\n" + set.reset);
            
        if (len(emails) > 0): return emails, passws;
        else: exit();

    else: print(set.rojo + "¡Archivo vacío o inexistente!" + set.reset); exit();