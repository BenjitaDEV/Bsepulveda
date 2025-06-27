#Repaso de listas y diccionarios

# LISTAS

#       -5 -4 -3 -2 -1
milista=["hola", 8, 6, 7, 2]
#        0  1  2  3  4


# el primer elemento de la lista siempre es indice 0
# el ultimo elemento de la lista siempre es indice -1

#print(milista)
# print(milista[0])

# recorrer una lista

# for elem in milista:
#     print(elem)

# DICCIONARIO
# es un conjunto de pares de datos

# dic={"nombre": "Benjamin Sepulveda",
#      "numero": 334,
#      "casado": False,
#      "empleado": False,
#      "Direccion": "Tocornal Grez #676"
#     }

# print(dic)
# agregar
# dic["edad"]=19

# print(dic)
# actualizar estad
# dic["empleado"]=True

# print(dic)

##EJEMPLO CORREDORES LISTAS

# corredores = ["Vegeta", "Goku", "Pikkoro"]

# tiempos = [10.9, 11.5, 13.6]

# while True:
#     try:
#         print('''
#             1.- Registrar Corredor y tiempo
#             2.- Ver listado de corredores                       
#             3.- Ver estadisticas (Tiempo menor, tiempo mayor, ordenados por mas rapido)                       
#             4.- Salir                       
#               ''')
#         op = int (input("Seleccione una opcion:\n"))
#         match op:
#             case 1:
#                 corre = input("ingrese el nombre del corredor:\n")
#                 corredores.append(corre) #.append() Sirve para agregar un valor dentro de un diccionario
#                 tempo=float(input("Registre su mejor tiempo:\n"))
#                 tiempos.append(tempo)
#             case 2:
#                 for i  in range(len(corredores)): #len() Retorna el numero de items en un contenedor
#                     print(f"Corredor: {corredores[i]} , Tiempo: {tiempos[i]}")
#             case 3:
#                 print("El corredor mas rapido es", min(tiempos) )#min() minimo
#                 print("El corredor mas lento es", max(tiempos) )#max() maximo
#                 print("Ordenados de mas rapido al mas lento")
#                 tiempos.sort() #.sort() ordena listas de menor a mayor, .reverse() mayor a menor
#                 print(tiempos)
#             case 4:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("opcion invalida")
#     except Exception as e:
#         print("Error:" , e)

##EJEMPLO 2 Diccionario


# productos={
#     "lapiz": 200,
#     "goma": 200,
#     "estuche": 1000,
#     "plumon": 300,
# }

# while True:
#     try:
#         print('''
#           1.- Agregar articulo y precio
#           2.- Ver listado
#           3.- Borrar
#           4.- Actualizar
#           5.- Salir
#           ''')
#         op=int(input("Seleccione una opcion\n"))
#         match op:
#             case 1:
#                 art=input("Ingrese el nombre del articulo:\n")
#                 precio=int(input("Ingrese el precio del articulo:\n"))
#                 productos[art]=precio
#             case 2:
#                 for key, value in productos.items(): #.items() Hace una division entre los dos valores de los pares de valores
#                     print (key, "$", value) #Key, value valores para ver el diccionario
#             case 3:
#                 borrar = input ("Cual es el producto que deseas eliminar:\n")
#                 del productos[borrar] #del borra
#                 print(f"El articulo {borrar} fue borrado")
#             case 4:
#                 for nom, precio in productos.items():
#                     print (nom, "$", precio)
#                 art = input("Cual es el producto que desea actualizar:\n")
#                 if art in productos:
#                     precio = int(input("Ingrese el precio nuevo:\n"))
#                     productos[art]=precio
#                 else:
#                     print("El articulo no existe")
#             case 5:
#                 print ("Saliendo")
#                 break
#             case _:
#                 print ("Opcion invalida")
#     except Exception as error:
#         print ("Error, hiciste algo mal:", error)

# def valida_pass(clave):
#     Mayuscula=False
#     Minuscula=False
#     Numero=False
#     While True:

#         for palabra in clave:
#         if palabra.isupper():
#             Mayuscula=True
#         if palabra.islower():
#             Mayuscula=True
#         if palabra.isdigit():
#             Mayuscula=True
#         if {Mayuscula, Minuscula, Numero} and len(clave)==6:
#             print("la clave está bien escrita")
#             break
#         else:
#             print("la clave esta mal escroto")

#DICCIONARIO PERROS

# perros={
#     1:{"Nombre": "Snoopy",
#        "Raza": "Quiltro",
#        "Codigo": "Soop07"}
# }

# def mostrar_perros(dict):
#     for key, perro in dict.items():
#         print(key , perro)

# while True:
#     try:
#         print('''
#               1.- Registrar un perro
#               2.- Mostrar perros
#               3.- Actualizar perro
#               4.- Exterminar perro >:D
#               5.- Salir
#               ''')
#         op=int(input("Seleccione una opcion\n"))
#         match op:
#             case 1:
#                 nombre=input("Ingrese un nombre\n")
#                 raza=input("Ingrese la raza\n")
#                 codigo=input("Ingrese su codigo\n")
#                 largo=list(perros.keys())[-1]
#                 perros[largo+1]={"Nombre": nombre,
#                                "Raza": raza,
#                                "Codigo": codigo}
#             case 2:
#                 mostrar_perros(perros)
#             case 3:
#                 mostrar_perros(perros)
#                 act=int(input("¿seleccione el perro a actualizar:\n"))
#                 while True:
#                     print('''
#                           1.- Nombre
#                           2.- Raza
#                           3.- Codigo
#                           4.- -pagina anterior-
#                           ''')
#                     dato=int(input("¿Que dato va a actualizar?:\n"))
#                     match dato:
#                         case 1:
#                             n=input("Ingrese el nuevo nombre\n")
#                             perros[act]["Nombre"]=n
#                         case 2:
#                             r=input("Ingrese el nueva raza\n")
#                             perros[act]["Raza"]=r
#                         case 3:
#                             c=input("Ingrese el nuevo codigo\n")
#                             perros[act]["Codigo"]=c
#                         case 4:
#                             break
#                         case _:
#                             print("Opcion invalida")
#             case 4:
#                 mostrar_perros(perros)
#                 borrar=int(input("Seleccione el perro a borrar (ingrese el numero)\n"))
#                 del perros[borrar]
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as e:
#         print("El error es: ", e)

#el codigo debe tener una mayuscula, una minuscula, un numero y un largo exacto de 6

# clave = "Nn1111"
# def valida_pass(clave):
#     Mayuscula=False
#     Minuscula=False
#     Numero=False
#     for palabra in clave:
#         if palabra.isupper():
#             Mayuscula=True
#         if palabra.islower():
#             Minuscula=True
#         if palabra.isdigit():
#             Numero=True
#     if Mayuscula and Minuscula and Numero and len(clave)==6:
#         print("la clave está bien escrita")
#         return True
#     else:
#         print("la clave ta mal escroto")
#         return False


perros={
    1:{"Nombre": "Snoopy",
       "Raza": "Quiltro",
       "Codigo": "Soop07"}
}

def mostrar_perros(dict):
    for key, perro in dict.items():
        print(key , perro)
        
def valida_pass(clave):
    Mayuscula=False
    Minuscula=False
    Numero=False
    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)==6:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave ta mal escroto")
        return False

def ingrese_perro(dict):
    nombre=input("Ingrese un nombre\n")
    raza=input("Ingrese la raza\n")
    codigo=input("Ingrese su codigo\n")
    if valida_pass(codigo):
        largo=list(dict.keys())[-1]
        dict[largo+1]={"Nombre": nombre,
                       "Raza": raza,
                       "Codigo": codigo}
    else:
        print("el parametro de la clave no es correcta")
        print("la clave debe tener una mayuscula, una minuscula, un numero y un largo de 6 digitos")

def act_perros(dict):
    mostrar_perros(dict)
    act=int(input("¿seleccione el perro a actualizar:\n"))
    while True:
        print('''
                1.- Nombre
                2.- Raza
                3.- Codigo
                4.- -pagina anterior-
                ''')
        dato=int(input("¿Que dato va a actualizar?:\n"))
        match dato:
            case 1:
                n=input("Ingrese el nuevo nombre\n")
                dict[act]["Nombre"]=n
            case 2:
                n=input("Ingrese el nueva raza\n")
                dict[act]["Raza"]=n
            case 3:
                n=input("Ingrese el nuevo codigo\n")
                if valida_pass(n):
                    dict[act]["Codigo"]=n
                else:
                    print("el parametro del codigo no es correcta")
                    print("el codigo debe tener una mayuscula, una minuscula, un numero y un largo de 6 digitos")
            case 4:
                break
            case _:
                print("Opcion invalida")

def borrar_perros(dict):
    mostrar_perros(perros)
    borrar=int(input("Seleccione el perro a borrar (ingrese el numero)\n"))
    del perros[borrar]

while True:
    try:
        print('''
              1.- Registrar un perro
              2.- Mostrar perros
              3.- Actualizar perro
              4.- Exterminar perro >:D
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion\n"))
        match op:
            case 1:
                ingrese_perro(perros)
            case 2:
                mostrar_perros(perros)
            case 3:
                act_perros(perros)
            case 4:
                borrar_perros(perros)
            case 5:
                print("Saliendo")
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("El error es: ", e)