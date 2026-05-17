# SISTEMA TRANSPORTE ZIPAQUIRA
rutas = {
    "Centro": {
        "Terminal": 4,
        "La Paz": 3 
    },
    "Terminal": {
        "Centro": 4,
        "Universidad": 6
    },
    "La Paz": {
        "Centro": 3,
        "Estacion Tren": 2
    },
    "Estacion Tren": {
        "La Paz": 2,
        "Universidad": 5
    },
    "Universidad": {
        "Terminal": 6,
        "Estacion Tren": 5
    }
}
    
# VALORES HEURISTICOS (Estimación en línea recta a Universidad)
heuristica = {
    "Centro": 7,
    "Terminal": 6,
    "La Paz": 4,
    "Estacion Tren": 2,
    "Universidad": 0,
}

def a_estrella(rutas, heuristica, inicio, destino):
    rutas_pendientes = [inicio]
    distancia_recorrida = {inicio: 0}
    ruta_anterior = {inicio: inicio}

    print(f"\n=== INICIANDO SISTEMA DE RUTAS: Desde {inicio} a {destino} ===")

    while rutas_pendientes:
        # 1. MOSTRAR RUTAS DISPONIBLES
        print(f"\nRUTAS DISPONIBLES:")
        mejor_estacion = None
        
        for estacion in rutas_pendientes:
            g = distancia_recorrida[estacion]
            h = heuristica[estacion]
            f = g + h
            print(f" • {estacion:15} = Costo total proyectado: {f}")

            if mejor_estacion is None or f < (distancia_recorrida[mejor_estacion] + heuristica[mejor_estacion]):
                mejor_estacion = estacion

        # 2. MOSTRAR RUTA FINAL
        if mejor_estacion == destino:
            mejor_ruta = []
            while ruta_anterior[mejor_estacion] != mejor_estacion:
                mejor_ruta.append(mejor_estacion)
                mejor_estacion = ruta_anterior[mejor_estacion]
            mejor_ruta.append(inicio)
            mejor_ruta.reverse()

            print("\n" + "="*45)
            print(f"¡MEJOR RUTA ENCONTRADA!")
            print(f" Camino: {' -> '.join(mejor_ruta)}")
            print(f" Costo Final: {distancia_recorrida[destino]} minutos")
            print("="*45)
            return

        # 3. Explorar conexiones internas de forma silenciosa
        for conexion in rutas[mejor_estacion]:
            nueva_distancia = distancia_recorrida[mejor_estacion] + rutas[mejor_estacion][conexion]
            if conexion not in distancia_recorrida or nueva_distancia < distancia_recorrida[conexion]:
                distancia_recorrida[conexion] = nueva_distancia
                ruta_anterior[conexion] = mejor_estacion
                if conexion not in rutas_pendientes:
                    rutas_pendientes.append(conexion)
        
        rutas_pendientes.remove(mejor_estacion)

    print("No se encontró ruta")

# EJECUCION
a_estrella(rutas, heuristica, "Centro", "Universidad")
