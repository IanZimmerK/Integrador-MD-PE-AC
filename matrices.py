def input_matrix(n, name='A'):
    """Pide al usuario n filas de n enteros y devuelve la matriz como lista de listas.
    Se valida que la fila tenga exactamente n valores
    y que sean enteros.
 """
    print("Introduce los elementos de la matriz {} {}x{} fila por fila, separados por espacios:".format(name, n, n))
    mat = []
    for i in range(n):
        while True:
            raw = input("Fila {} ({} valores): ".format(i + 1, n)).strip()
            parts = raw.split()
            if len(parts) != n:
                print("Se esperaban {} valores, recibidos {}. Intenta de nuevo.".format(n, len(parts)))
                continue
            try:
                row = [int(x) for x in parts]
            except ValueError:
                print("Valores inválidos: usa enteros.")
                continue
            mat.append(row)
            break
    return mat


def print_matrix(M, name='M'):
    """Imprime la matriz de forma legible. Evita formatos avanzados.
    """
    if M is None or len(M) == 0:
        print("Matriz {}: (vacía)".format(name))
        return
    n = len(M)
    print("Matriz {} ({}x{}):".format(name, n, len(M[0]) if n > 0 else 0))
    for row in M:
        # imprimimos con espacio simple para que sea claro
        print('  ' + ' '.join(str(v) for v in row))


def add(A, B):
    """Suma A + B (asume matrices cuadradas del mismo tamaño).
    Implementada con bucles claros para que los alumnos comprendan índices i,j.
    """
    if not A or not B or len(A) != len(B):
        return None
    n = len(A)
    C = []
    for i in range(n):
        row = []
        for j in range(n):
            # suma elemento a elemento
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C


def transpose(A):
    """Transpuesta de A: intercambia filas por columnas.
    Se usa un doble bucle sencillo: nuevo[i][j] = A[j][i]
    """
    n = len(A)
    T = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[j][i])
        T.append(row)
    return T


def multiply(A, B, trace=False):
    """Multiplica A * B (matrices cuadradas). Si trace=True imprime un rastro sencillo.
    Algoritmo clásico con tres bucles: i (filas de A), j (columnas de B), k (suma de productos).
    """
    if not A or not B or len(A) != len(B):
        return None
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc = 0
            for k in range(n):
                # producto A[i][k] * B[k][j]
                a = A[i][k]
                b = B[k][j]
                prod = a * b
                acc += prod
                if trace:
                    # dirección fila‑mayor simple: addr = fila * n + columna
                    addr_a = i * n + k
                    addr_b = k * n + j
                    print("Acceso: A[{}][{}] (addr {}) = {} ; B[{}][{}] (addr {}) = {} ; prod = {} ; acc = {}".format(i, k, addr_a, a, k, j, addr_b, b, prod, acc))
            C[i][j] = acc
    return C


def determinant2(A):
    """Determinante de 2x2: ad - bc"""
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def determinant3(A):
    """Determinante de 3x3 usando la regla de Sarrus con pasos explícitos."""
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    # diagonales positivas
    p1 = a * e * i
    p2 = b * f * g
    p3 = c * d * h
    # diagonales negativas
    n1 = c * e * g
    n2 = a * f * h
    n3 = b * d * i
    return (p1 + p2 + p3) - (n1 + n2 + n3)


def determinant(A):
    """Selector de determinante según el tamaño (2 o 3)."""
    n = len(A)
    if n == 2:
        return determinant2(A)
    if n == 3:
        return determinant3(A)
    return None


if __name__ == '__main__':
    # Pequeña demo para quien abra este archivo directamente.
    print('Demo rápido: suma y multiplicación 2x2')
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print('A =', A)
    print('B =', B)
    print('A + B =', add(A, B))
    print('A * B =')
    C = multiply(A, B)
    print(C)