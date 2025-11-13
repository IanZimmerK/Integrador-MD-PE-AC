def ingresar_matriz(orden, nombre='A'):
    # Pide al usuario orden filas de orden enteros y devuelve la matriz como lista de listas.
    # Se valida que la fila tenga exactamente orden valores
    # y que sean enteros.
    print("Introduce los elementos de la matriz {} {}x{} fila por fila, separados por espacios:".format(nombre, orden, orden))
    matriz = []
    for indice_fila in range(orden):
        while True:
            entrada_texto = input("Fila {} ({} valores): ".format(indice_fila + 1, orden)).strip()
            partes = entrada_texto.split()
            if len(partes) != orden:
                print("Se esperaban {} valores, recibidos {}. Intenta de nuevo.".format(orden, len(partes)))
                continue
            try:
                fila = [int(valor) for valor in partes]
            except ValueError:
                print("Valores inválidos: usa enteros.")
                continue
            matriz.append(fila)
            break
    return matriz


def imprimir_matriz(matriz, nombre='M'):
    # Imprime la matriz de forma legible
    if matriz is None or len(matriz) == 0:
        print("Matriz {}: (vacía)".format(nombre))
        return
    orden = len(matriz)
    print("Matriz {} ({}x{}):".format(nombre, orden, len(matriz[0]) if orden > 0 else 0))
    for fila in matriz:
        # imprimimos con espacio simple para que sea claro
        print('  ' + ' '.join(str(valor) for valor in fila))


def sumar(matriz_a, matriz_b):
    # Suma matriz_a + matriz_b (asume matrices cuadradas del mismo tamaño).
    # Implementada con bucles claros para que los alumnos comprendan índices fila, columna.
    if not matriz_a or not matriz_b or len(matriz_a) != len(matriz_b):
        return None
    orden = len(matriz_a)
    matriz_resultado = []
    for indice_fila in range(orden):
        fila_resultado = []
        for indice_columna in range(orden):
            # suma elemento a elemento
            fila_resultado.append(matriz_a[indice_fila][indice_columna] + matriz_b[indice_fila][indice_columna])
        matriz_resultado.append(fila_resultado)
    return matriz_resultado

def transponer(matriz):
    # Transpuesta de matriz: intercambia filas por columnas.
    # Se usa un doble bucle sencillo: transpuesta[fila][columna] = matriz[columna][fila]
    orden = len(matriz)
    matriz_transpuesta = []
    for indice_fila in range(orden):
        fila_resultado = []
        for indice_columna in range(orden):
            fila_resultado.append(matriz[indice_columna][indice_fila])
        matriz_transpuesta.append(fila_resultado)
    return matriz_transpuesta


def multiplicar(matriz_a, matriz_b, mostrar_rastro=False):
    # Multiplica matriz_a * matriz_b (matrices cuadradas). Si mostrar_rastro=True imprime un rastro sencillo.
    # Algoritmo clásico con tres bucles: fila (filas de A), columna (columnas de B), indice (suma de productos).
    
    if not matriz_a or not matriz_b or len(matriz_a) != len(matriz_b):
        return None
    orden = len(matriz_a)
    matriz_resultado = [[0 for _ in range(orden)] for _ in range(orden)]
    for indice_fila in range(orden):
        for indice_columna in range(orden):
            acumulador = 0
            for indice in range(orden):
                # producto matriz_a[fila][indice] * matriz_b[indice][columna]
                valor_a = matriz_a[indice_fila][indice]
                valor_b = matriz_b[indice][indice_columna]
                producto = valor_a * valor_b
                acumulador += producto
                if mostrar_rastro:
                    # dirección fila‑mayor simple: direccion = fila * orden + columna
                    direccion_a = indice_fila * orden + indice
                    direccion_b = indice * orden + indice_columna
                    print("Acceso: A[{}][{}] (dir {}) = {} ; B[{}][{}] (dir {}) = {} ; producto = {} ; acumulador = {}".format(
                        indice_fila, indice, direccion_a, valor_a, indice, indice_columna, direccion_b, valor_b, producto, acumulador))
            matriz_resultado[indice_fila][indice_columna] = acumulador
    return matriz_resultado


def determinante_2x2(matriz):
    """Determinante de 2x2: ad - bc"""
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


def determinante_3x3(matriz):
    """Determinante de 3x3 usando la regla de Sarrus con pasos explícitos."""
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    # diagonales positivas
    diagonal_positiva_1 = a * e * i
    diagonal_positiva_2 = b * f * g
    diagonal_positiva_3 = c * d * h
    # diagonales negativas
    diagonal_negativa_1 = c * e * g
    diagonal_negativa_2 = a * f * h
    diagonal_negativa_3 = b * d * i
    return (diagonal_positiva_1 + diagonal_positiva_2 + diagonal_positiva_3) - (diagonal_negativa_1 + diagonal_negativa_2 + diagonal_negativa_3)


def calcular_determinante(matriz):
    """Selector de determinante según el tamaño (2 o 3)."""
    orden = len(matriz)
    if orden == 2:
        return determinante_2x2(matriz)
    if orden == 3:
        return determinante_3x3(matriz)
    return None