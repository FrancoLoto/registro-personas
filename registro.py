ruta = "/Users/francoloto/Desktop/python_projects/registro_de_personas/personas.txt"

def Agregar(nombre, edad, genero):
    with open(ruta, "a") as archivo:
        fila = f"{nombre}, {edad}, {genero}\n"
        archivo.write(fila)
        print("----Persona Agregada-----")

def Lista():
    with open(ruta, "r") as archivo:
        print("-----Lista-----")
        print(archivo.read())
        print("---------------")


def Listar_Genero(letra_genero):
    with open(ruta, "r") as archivos:
        
        archivos.seek(0, 0)

        for archivo in archivos:
            archivo = archivo.strip("\n")
            nombre, edad, genero = archivo.split(",")

            if letra_genero == genero:
                print(archivo)



while True:
    print("\n---Elige una opción----")
    print("1 - Agregar una persona")
    print("2 - Listar personas")
    print("3 - Listar personas por genero")
    print("4 - Cerrar registro")
    opcion = input("Que quieres hacer? (1-4):".strip())

    if int(opcion) == 1:
        nom = input("Tu nombre: ").strip().capitalize()
        ed = input("Tu edad: ").strip()
        gen = input("Genero: ").strip().upper()
        Agregar(nom, ed, gen)
    elif int(opcion) == 2:
        Lista()
    elif int(opcion) == 3:
        gen = input("Ingresa el genero (M/F): ").strip().upper()
        Listar_Genero(gen)
    elif int(opcion) == 4:
        break 
    else:
        print("Opcion invalida")