import sqlite3
import servers_json

NOMBRE_DB = "servidores.db"


def crear_db(nombre_db):
    with sqlite3.connect(nombre_db) as conexion:
        cursor = conexion.cursor()

        sql_drop = "DROP TABLE IF EXISTS Servidores"
        cursor.execute(sql_drop)

        sql_create = """
        CREATE TABLE Servidores (
            nombre TEXT PRIMARY KEY,
            ip TEXT,
            sistema TEXT,
            ubicacion TEXT,
            responsable TEXT
        );
        """
        cursor.execute(sql_create)

        conexion.commit()
        print("Base de datos creada correctamente")


def insertar_datos():
    servidores = servers_json.cargar_servidores()

    with sqlite3.connect(NOMBRE_DB) as conexion:
        cursor = conexion.cursor()

        sql_insert = """
        INSERT OR REPLACE INTO Servidores
        (nombre, ip, sistema, ubicacion, responsable)
        VALUES (?, ?, ?, ?, ?);
        """

        for servidor in servidores:
            datos = (
                servidor["nombre"],
                servidor["ip"],
                servidor["sistema"],
                servidor["ubicacion"],
                servidor["responsable"]
            )
            cursor.execute(sql_insert, datos)

        conexion.commit()
        print("Datos insertados correctamente")


def consultar_servidor(nombre):
    with sqlite3.connect(NOMBRE_DB) as conexion:
        cursor = conexion.cursor()

        sql_select = """
        SELECT nombre, ip, sistema, ubicacion, responsable
        FROM Servidores
        WHERE nombre = ?;
        """
        cursor.execute(sql_select, (nombre,))
        servidor = cursor.fetchone()

        if servidor is None:
            print("Servidor non existe")
        else:
            print("Datos do servidor:")
            print(f"Nombre: {servidor[0]}")
            print(f"IP: {servidor[1]}")
            print(f"Sistema: {servidor[2]}")
            print(f"Ubicación: {servidor[3]}")
            print(f"Responsable: {servidor[4]}")


def xestionar_servidores():
    opcion = ""

    while opcion != "4":
        print("\n--- MENÚ SERVIDORES ---")
        print("1 - Crear BDD")
        print("2 - Inserir Datos")
        print("3 - Consultar servidor")
        print("4 - Saír")

        opcion = input("Escolle unha opción: ")

        if opcion == "1":
            crear_db(NOMBRE_DB)

        elif opcion == "2":
            insertar_datos()

        elif opcion == "3":
            nombre = input("Introduce o nome do servidor: ")
            consultar_servidor(nombre)

        elif opcion == "4":
            print("Saíndo do programa")

        else:
            print("Opción non válida")


# PRUEBAS
if __name__ == "__main__":
    xestionar_servidores()
