from matrices import input_matrix, print_matrix, add, transpose, multiply, determinant


def ask_int(prompt, allowed=None):
    """Pide un entero al usuario y valida que esté en 'allowed' si se proporciona."""
    while True:
        try:
            v = int(input(prompt))
        except ValueError:
            print("Entrada inválida — ingresa un entero.")
            continue
        if allowed and v not in allowed:
            print("Valor no permitido. Opciones: {}".format(sorted(allowed)))
            continue
        return v


def pause():
    input('\nPresiona Enter para continuar...')


def choose_matrix(name='matriz'):
    while True:
        c = input("Selecciona matriz ({}): A/B: ".format(name)).strip().upper()
        if c in ('A', 'B'):
            return c
        print("Entrada inválida — escribe A o B.")


def print_header(title):
    print('\n' + '=' * 40)
    print(title)
    print('=' * 40)


def show_memory_map(M, name='M'):
    """Muestra una vista aplanada (fila‑mayor) de la matriz."""
    if not M:
        print('Matriz {} vacía'.format(name))
        return
    n = len(M)
    flat = []
    for i in range(n):
        for j in range(n):
            flat.append(M[i][j])
    print('\nMapa de memoria (fila‑mayor) de {}:'.format(name))
    for idx, val in enumerate(flat):
        print('  addr {} -> {}'.format(idx, val))


def do_operation(op, A, B, n):
    """Ejecuta una operación y muestra una breve explicación para estudiantes."""
    if op == 'sum':
        print_header('Suma: A + B')
        print('La suma se realiza elemento a elemento: C[i][j] = A[i][j] + B[i][j]')
        C = add(A, B)
        print_matrix(C, 'A + B')

    elif op == 'transpose':
        which = choose_matrix('a transponer')
        M = A if which == 'A' else B
        print_header('Transpuesta')
        print('La transpuesta intercambia filas y columnas: T[i][j] = M[j][i]')
        T = transpose(M)
        print_matrix(T, f"{which}^T")

    elif op == 'multiply':
        print_header('Multiplicación: A * B')
        print('Regla: C[i][j] = sum_k A[i][k] * B[k][j]')
        want = input('¿Ver rastro paso a paso de A * B? (s/n): ').strip().lower()
        if want == 's':
            C = multiply(A, B, trace=True)
        else:
            C = multiply(A, B, trace=False)
        print_matrix(C, 'A * B')

    elif op == 'determinant':
        which = choose_matrix('para determinante')
        M = A if which == 'A' else B
        print_header('Determinante')
        print('Cálculo directo para matrices 2x2 o 3x3')
        d = determinant(M)
        print(f"Determinante de {which}: {d}")

    else:
        print('Operación desconocida')

    pause()


def initial_submenu(A, B, n):
    print_header('Matrices cargadas')
    print_matrix(A, 'A')
    print_matrix(B, 'B')
    # pregunta didáctica: mostrar cómo se vería la memoria fila‑mayor
    if input('\n¿Quieres ver el mapa de memoria (fila‑mayor) de A y B? (s/n): ').strip().lower() == 's':
        show_memory_map(A, 'A')
        show_memory_map(B, 'B')
    while True:
        print('\nOperaciones disponibles:')
        print(' 1) Sumar A + B')
        print(' 2) Transponer (elige A o B)')
        print(' 3) Multiplicar A * B')
        print(' 4) Determinante (elige A o B)')
        print(' 0) Volver al menú principal')
        choice = ask_int('Elige (0-4): ', allowed={0, 1, 2, 3, 4})
        if choice == 0:
            return
        mapping = {1: 'sum', 2: 'transpose', 3: 'multiply', 4: 'determinant'}
        do_operation(mapping[choice], A, B, n)


def main_menu(A, B, n):
    while True:
        print_header('Menú principal')
        print('Acciones:')
        print(' 1) Mostrar matrices (A, B)')
        print(' 2) Operaciones aritméticas (A + B, A * B)')
        print(' 3) Transformaciones (transponer A/B)')
        print(' 4) Determinante (A o B)')
        print(' 5) Recargar matrices (cambiar orden y cargar de nuevo)')
        print(' 0) Salir')
        choice = ask_int('Elige (0-5): ', allowed={0, 1, 2, 3, 4, 5})
        if choice == 0:
            if input('¿Seguro que quieres salir? (s/n): ').strip().lower() == 's':
                print('Saliendo...')
                return
            else:
                continue

        if choice == 1:
            print_header('Mostrar matrices')
            print_matrix(A, 'A')
            print_matrix(B, 'B')
            pause()
        elif choice == 2:
            print('\nOperaciones aritméticas:')
            print(' 1) Sumar A + B')
            print(' 2) Multiplicar A * B')
            sub = ask_int('Elige (1-2): ', allowed={1, 2})
            if sub == 1:
                do_operation('sum', A, B, n)
            else:
                do_operation('multiply', A, B, n)
        elif choice == 3:
            do_operation('transpose', A, B, n)
        elif choice == 4:
            do_operation('determinant', A, B, n)
        elif choice == 5:
            n = ask_int('Orden (2 o 3): ', allowed={2, 3})
            A = input_matrix(n, 'A')
            B = input_matrix(n, 'B')
            print('\nMatrices recargadas:')
            print_matrix(A, 'A')
            print_matrix(B, 'B')
            pause()
        else:
            print('Opción no implementada')


def main():
    # Carga obligatoria al inicio
    print_header('Carga de matrices (inicio)')
    n = ask_int('Orden (2 o 3): ', allowed={2, 3})
    A = input_matrix(n, 'A')
    B = input_matrix(n, 'B')
    initial_submenu(A, B, n)
    main_menu(A, B, n)


if __name__ == '__main__':
    main()
