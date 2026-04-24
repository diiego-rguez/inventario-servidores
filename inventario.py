def leer_fichero(ruta_fichero):
    lineas_validas = []

    try:
        with open(ruta_fichero, "r") as i:
            for linea in i:
                linea = linea.strip()

                if linea == "":
                    continue

                if linea.startswith("#"):
                    continue

                lineas_validas.append(linea)

    except FileNotFoundError:
        print("Error")

    return lineas_validas




def normalizar_linea(linea):
    linea = linea.replace(",", ";")
    partes = linea.split(";")

    for i in range(len(partes)):
        partes[i] = partes[i].strip()

    nombre = partes[0] if len(partes) > 0 else ""
    ip = partes[1] if len(partes) > 1 else ""
    sistema = partes[2].lower() if len(partes) > 2 else ""
    ubicacion = partes[3] if len(partes) > 3 else ""
    responsable = partes[4].capitalize() if len(partes) > 4 else ""

    diccionario = {
        "nombre": nombre,
        "ip": ip,
        "sistema": sistema,
        "ubicacion": ubicacion,
        "responsable": responsable
    }

    return diccionario




def validar_datos(diccionario_linea):
    nombre = diccionario_linea["nombre"]
    ip = diccionario_linea["ip"]
    sistema = diccionario_linea["sistema"]
    ubicacion = diccionario_linea["ubicacion"]
    responsable = diccionario_linea["responsable"]

    if nombre == "":
        return (False, "Error: nombre obligatorio")

    partes_ip = ip.split(".")
    if len(partes_ip) != 4:
        return (False, "Error: ip inválida")

    for bloque in partes_ip:
        if not bloque.isdigit():
            return (False, "Error: ip inválida")

        valor = int(bloque)
        if valor < 0 or valor > 255:
            return (False, "Error: ip inválida")

    sistemas_validos = ["linux", "windows", "macos"]
    if sistema not in sistemas_validos:
        return (False, "Error: sistema inválido")

    if ubicacion == "":
        ubicacion = None

    if responsable == "" or responsable == "-" or responsable is None:
        responsable = None

    diccionario_linea["ubicacion"] = ubicacion
    diccionario_linea["responsable"] = responsable

    return (True, diccionario_linea)




def procesar_inventario(ruta_fichero):
    lineas = leer_fichero(ruta_fichero)

    inventario = []
    errores = []

    for linea in lineas:
        datos_norm = normalizar_linea(linea)
        valido, resultado = validar_datos(datos_norm)

        if valido:
            inventario.append(resultado)
        else:
            errores.append(resultado)




    ips_unicas = []
    sistemas_contador = {}
    responsables_unicos = set()


    for servidor in inventario:
        if servidor["ip"] not in ips_unicas:
            ips_unicas.append(servidor["ip"])


        sis = servidor["sistema"]
        if sis not in sistemas_contador:
            sistemas_contador[sis] = 1
        else:
            sistemas_contador[sis] += 1


        if servidor["responsable"] is not None:
            responsables_unicos.add(servidor["responsable"])

    informe = {
        "servidores_validos": len(inventario),
        "lineas_descartadas": len(errores),
        "ips_unicas": ips_unicas,
        "contadores_sistema": sistemas_contador,
        "responsables_distintos": len(responsables_unicos)
    }

    return inventario, errores, informe




def escribir_informe(informe, ruta_salida):
    try:
        with open(ruta_salida, "w") as f:
            f.write(f"Número de servidores válidos cargados: {informe['servidores_validos']}\n")
            f.write(f"Número de líneas descartadas (con errores): {informe['lineas_descartadas']}\n")

            ips = ", ".join(informe["ips_unicas"])
            f.write(f"Lista de IPs únicas: {ips}\n")

            f.write(f"Responsables distintos: {informe['responsables_distintos']}\n")

    except:
        print("Error")




inventario, errores, informe = procesar_inventario("inventario.txt")
escribir_informe(informe, "informe_servidores.txt")

print(inventario)
print(errores)
print(informe)
