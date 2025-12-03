from matrices import ingresar_matriz, imprimir_matriz, sumar, restar, transponer, multiplicar, calcular_determinante
from matrices import multiplicar_escalar

def pedir_entero(mensaje, valores_permitidos=None):
    # Pide un entero al usuario y valida que esté en 'valores_permitidos' si se proporciona.
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Entrada inválida — ingresa un entero.")
            continue
        if valores_permitidos is not None and valor not in valores_permitidos:
            print("Valor no permitido. Opciones: {}".format(sorted(valores_permitidos)))
            continue
        return valor


def pausar():
    input('\nPresiona Enter para continuar...')

def principal():
    # Carga obligatoria al inicio
    imprimir_encabezado('Carga de matrices (inicio)')
    orden = pedir_entero('Orden (2 o 3): ', valores_permitidos={2, 3})
    matriz_a = ingresar_matriz(orden, 'A')
    matriz_b = ingresar_matriz(orden, 'B')
    menu_principal(matriz_a, matriz_b, orden)

    
def elegir_matriz(descripcion='matriz'):
    while True:
        letra = input("Selecciona matriz ({}): A/B: ".format(descripcion)).strip().upper()
        if letra in ('A', 'B'):
            return letra
        print("Entrada inválida — escribe A o B.")


def imprimir_encabezado(titulo):
    print('\n' + '=' * 40)
    print(titulo)
    print('=' * 40)


def mostrar_mapa_memoria(matriz, nombre='M'):
    # Muestra una vista aplanada (fila‑mayor) de la matriz.
    if not matriz:
        print('Matriz {} vacía'.format(nombre))
        return
    orden = len(matriz)
    lista_aplanada = []
    for indice_fila in range(orden):
        for indice_columna in range(orden):
            lista_aplanada.append(matriz[indice_fila][indice_columna])
    print('\nMapa de memoria (fila‑mayor) de {}:'.format(nombre))
    for direccion, valor in enumerate(lista_aplanada):
        print('  dir {} -> {}'.format(direccion, valor))


def ejecutar_operacion(operacion, A, B, orden):
    # Ejecuta una operación y muestra una breve explicación para estudiantes.
    if operacion == 'suma':
        imprimir_encabezado('Suma: A + B')
        print('La suma se realiza elemento a elemento: C[i][j] = A[i][j] + B[i][j]')
        C = sumar(A, B)
        imprimir_matriz(C, 'A + B')

    elif operacion == 'resta':
        imprimir_encabezado('Resta: A - B')
        print('La resta se realiza elemento a elemento: C[i][j] = A[i][j] - B[i][j]')
        C = restar(A, B)
        imprimir_matriz(C, 'A - B')

    elif operacion == 'transpuesta':
        cual = elegir_matriz('a transponer')
        M = A if cual == 'A' else B
        imprimir_encabezado('Transpuesta')
        print('La transpuesta intercambia filas y columnas: T[i][j] = M[j][i]')
        T = transponer(M)
        imprimir_matriz(T, f"{cual}^T")

    elif operacion == 'multiplicacion':
        imprimir_encabezado('Multiplicación: A * B')
        print('Regla: C[i][j] = sum_k A[i][k] * B[k][j]')
        quiere = input('¿Ver rastro paso a paso de A * B? (s/n): ').strip().lower()
        if quiere == 's':
            C = multiplicar(A, B, mostrar_rastro=True)
        else:
            C = multiplicar(A, B, mostrar_rastro=False)
        imprimir_matriz(C, 'A * B')

    elif operacion == 'determinante':
        cual = elegir_matriz('para determinante')
        M = A if cual == 'A' else B
        imprimir_encabezado('Determinante')
        imprimir_matriz(matriz, cual)
        
        quiere = input('\n¿Ver cálculo paso a paso? (s/n): ').strip().lower()
        mostrar_pasos = (quiere == 's')
        
        d = calcular_determinante(M, mostrar_pasos)
        
        if not mostrar_pasos:
            print(f"\nDeterminante de {cual}: {d}")
    
    elif operacion == 'escalar':
        cual= elegir_matriz('a multiplicar por escalar')
        matriz = A if cual == 'A' else B

        esc= pedir_entero('Ingresa el escalar (entero): ')
        imprimir_encabezado(f"Multliplicación por escalar: ({esc})")
        print(f'Se multiplica cada elemento de {cual} por el escalar {esc}: C[i][j] = {esc} * M[i][j]')

        c= multiplicar_escalar(matriz, esc)
        imprimir_matriz(c, f"{esc} * {cual}")

    else:
        print('Operación desconocida')

    pausar()


def menu_principal(matriz_a, matriz_b, orden):
    imprimir_encabezado('Matrices cargadas')
    imprimir_matriz(matriz_a, 'A')
    imprimir_matriz(matriz_b, 'B')
    # pregunta didáctica: mostrar cómo se vería la memoria fila‑mayor
    if input('\n¿Quieres ver el mapa de memoria (fila‑mayor) de A y B? (s/n): ').strip().lower() == 's':
        mostrar_mapa_memoria(matriz_a, 'A')
        mostrar_mapa_memoria(matriz_b, 'B')
    while True:
        print('\nOperaciones disponibles:')
        print(' 1) Sumar A + B')
        print(' 2) Restar A - B')
        print(' 3) Transponer (elige A o B)')
        print(' 4) Multiplicar A * B')
        print(' 5) Determinante (elige A o B)')
        print(' 6) Recargar matrices (cambiar orden y cargar de nuevo)')
        print(' 7) Multiplicar matriz por escalar')
        print(' 0) Salir')
        opcion = pedir_entero('Elige (0-7): ', valores_permitidos={0, 1, 2, 3, 4, 5, 6, 7})
        if opcion == 0:
            return
        mapeo_operaciones = {1: 'suma', 2: 'resta', 3: 'transpuesta', 4: 'multiplicacion', 5: 'determinante', 7: 'escalar'}
        if opcion in mapeo_operaciones:
            ejecutar_operacion(mapeo_operaciones[opcion], matriz_a, matriz_b, orden)
        elif opcion == 6:
            orden = pedir_entero('Orden (2 o 3): ', valores_permitidos={2, 3})
            matriz_a = ingresar_matriz(orden, 'A')
            matriz_b = ingresar_matriz(orden, 'B')
            print('\nMatrices recargadas:')
            imprimir_matriz(matriz_a, 'A')
            imprimir_matriz(matriz_b, 'B')
            pausar()

if __name__ == '__main__':
    principal()
