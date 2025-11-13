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


def restar(matriz_a, matriz_b):
    # Resta matriz_a - matriz_b (asume matrices cuadradas del mismo tamaño).
    # Implementada con bucles claros para que los alumnos comprendan índices fila, columna.
    if not matriz_a or not matriz_b or len(matriz_a) != len(matriz_b):
        return None
    orden = len(matriz_a)
    matriz_resultado = []
    for indice_fila in range(orden):
        fila_resultado = []
        for indice_columna in range(orden):
            # resta elemento a elemento
            fila_resultado.append(matriz_a[indice_fila][indice_columna] - matriz_b[indice_fila][indice_columna])
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


def determinante_2x2(matriz, mostrar_pasos=False):
    # Determinante de 2x2: ad - bc
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    
    producto_principal = a * d
    producto_secundario = b * c
    
    if mostrar_pasos:
        print('\nCálculo del determinante 2x2:')
        print('  Diagonal principal: {} × {} = {}'.format(a, d, producto_principal))
        print('  Diagonal secundaria: {} × {} = {}'.format(b, c, producto_secundario))
        print('\nDeterminante: {} - {} = {}'.format(producto_principal, producto_secundario, producto_principal - producto_secundario))
    
    return producto_principal - producto_secundario


def determinante_3x3(matriz, mostrar_pasos=False):

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    
    diagonal_positiva_1 = a * e * i
    diagonal_positiva_2 = d * h * c
    diagonal_positiva_3 = f * b * g
    
    
    diagonal_negativa_1 = c * e * g
    diagonal_negativa_2 = d * b * i
    diagonal_negativa_3 = f * h * a

    
    if mostrar_pasos:
        suma_positivas = diagonal_positiva_1 + diagonal_positiva_2 + diagonal_positiva_3
        suma_negativas = diagonal_negativa_1 + diagonal_negativa_2 + diagonal_negativa_3
        
        print('\nDiagonales positivas:')
        print('  {} × {} × {} = {}'.format(a, e, i, diagonal_positiva_1))
        print('  {} × {} × {} = {}'.format(d, h, c, diagonal_positiva_2))
        print('  {} × {} × {} = {}'.format(f, b, g, diagonal_positiva_3))
        print('  Suma positivas: {} + {} + {} = {}'.format(diagonal_positiva_1, diagonal_positiva_2, diagonal_positiva_3, suma_positivas))
        
        print('\nDiagonales negativas:')
        print('  {} × {} × {} = {}'.format(c, e, g, diagonal_negativa_1))
        print('  {} × {} × {} = {}'.format(d, b, i, diagonal_negativa_2))
        print('  {} × {} × {} = {}'.format(f, h, a, diagonal_negativa_3))
        print('  Suma negativas: {} + {} + {} = {}'.format(diagonal_negativa_1, diagonal_negativa_2, diagonal_negativa_3, suma_negativas))
        
        resultado = suma_positivas - suma_negativas
        print('\nDeterminante: {} - {} = {}'.format(suma_positivas, suma_negativas, resultado))
    



def calcular_determinante(matriz, mostrar_pasos=False):
    """Selector de determinante según el tamaño (2 o 3)."""
    orden = len(matriz)
    if orden == 2:
        return determinante_2x2(matriz, mostrar_pasos)
    if orden == 3:
        return determinante_3x3(matriz, mostrar_pasos)
    return None