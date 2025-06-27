#######################
# Ejecicio 1
#######################

import os

comprador = {
    1 : {"Nombre" : "Juan",
         "Entrada" : "G",
         "Codigo" : "Acceso123"
         },
    2 : {"Nombre" : "Alejandro",
         "Entrada" : "V",
         "Codigo" : "Acceso123"}
}


def menu():
    while True:
        try:
            op = int(input("""==== Bienvenido ====
1.- Comprar entrada
2.- Consultar comprador
3.- Cancelar compra
4.- Salir
"""))
            return op
        except Exception as e:
            print(f"Error: {e}")

def sistema():
    while True:
        op = menu()
        match op:
            case 1:
                comprar()
            case 2:
                consultar()
            case 3:
                borrar()
            case 4:
                print("Programa terminado...")
                break
            case _:
                print("Ingrese una opcion valida")

def comprar():
    while True:
        nombre = input("Ingrese su nombre:\n")
        if any(c["Nombre"] == nombre for c in comprador.values()):
            print("Error, ese comprador ya estaba ingresado")
        else:
            break
    while True:
        entrada = input("Ingrese el tipo de entrada:        [G/V]\n").lower()
        if entrada not in ["g", "v"]:
            print("Error, seleccione un tipo de entrada valido")
        else:
            break
    while True:
        clave = input("Ingrese el codigo de confirmacion:\n")
        if validar(clave):
            nuevo_id = max(comprador.keys(), default = 0) + 1
            comprador[nuevo_id] = {"Nombre" : nombre,
                                   "Entrada" : entrada.upper(),
                                   "Codigo" : clave}
            print("Usuario ingresado con exito")
            input("Pulse Enter para continuar...")
            os.system("cls")
            break
        else:
            print("Codigo no valido, Intente otra vez")


def validar(clave):
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
        print("Debe contener almenos 1 mayuscula, 1 minuscula y un numero hasta un maximo de 6 digitos")
        return False

# def validar(clave):
#     if len(clave) < 6:
#         print("El codigo tiene que tener un minimo de 6 caracteres")
#         return False
#     elif sum(1 for c in clave if c.isupper()) == 0:
#         print("La clave debe de tener al menos 1 letra mayuscula")
#         return False
#     elif sum(1 for c in clave if c.islower()) == 0:
#         print("La clave debe de tener al menos 1 letra minuscula")
#         return False
#     elif sum(1 for c in clave if c.isdigit()) == 0:
#         print("La clave debe de tener al menos 1 numero")
#         return False
#     else:
#         return True

def consultar():
    nombre = input("Ingrese el nombre del comprador a buscar:\n")
    if not any(comp["Nombre"] == nombre for comp in comprador.values()):
        print("El comprador no se encuentra")
    for c in comprador.values():
        if c["Nombre"] == nombre:
            print(f"Tipo de entrada: {c['Entrada']}, Codigo: {c['Codigo']}")
            input("Pulse Enter para continuar...")
            os.system('cls')
            break

def borrar():
    borrar = input("Ingrese el nombre del comprador a cancelar:\n")
    id_a_borrar = None
    for key, c in comprador.items():
        if c["Nombre"] == borrar:
            id_a_borrar = key
            break
    if id_a_borrar is not None:
        del comprador[id_a_borrar]
        print("Compra cancelada")
        input("Pulse Enter para continuar...")
        os.system('cls')
    else:
        print("No se pudo cancelar la compra")

def borrar_perros(dict):
    for key, perro in dict.items():
        print(key , perro)
    comprador(perros)
    borrar=int(input("Seleccione el perro a borrar (ingrese el numero)\n"))
    del perros[borrar]

sistema()