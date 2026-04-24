import inventario
import json

#Constantes
ARCHIVO_TXT = "inventario.txt"
ARCHIVO_JSON = "lista_servidores.json"



def guardar_servidores():
    lista_servidores, _, _ = inventario.procesar_inventario(ARCHIVO_TXT)
    with open(ARCHIVO_JSON, "w") as f:
        json.dump(lista_servidores, f, indent=4)

def leer_servidores():
    with open(ARCHIVO_JSON, "r") as f:
        lista_servidores = json.load(f)
    return lista_servidores

def cargar_servidores():
    guardar_servidores()
    return leer_servidores()

#Pruebas
if __name__ == "__main__":
    servidores = cargar_servidores()
    for s in servidores:
        print(s)
