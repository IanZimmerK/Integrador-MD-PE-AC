"""
Calculadora de matrices 
Matrices cuadradas n×n (mínimo 2×2, máximo 4×4).
Operaciones: Suma, Multiplicación, Transposición, Determinante, Matriz identidad.
Uso: python matrix_simulator.py
"""

# ====================================================
# ==================  OPERACIONES  ===================
# ====================================================

def shape(A):
    return len(A), len(A[0]) if A and A[0] else 0

def check_rect(A):
    if not A or not A[0]:
        raise ValueError("Matriz vacía")
    c = len(A[0])
    for fila in A:
        if len(fila) != c:
            raise ValueError("Filas de distinto tamaño")

def is_square(A):
    r, c = shape(A)
    return r == c

def add(A, B):
    rA, cA = shape(A)
    C = []
    for i in range(rA):
        fila = []
        for j in range(cA):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def transpose(A):
    r, c = shape(A)
    T = []
    for j in range(c):
        fila = []
        for i in range(r):
            fila.append(A[i][j])
        T.append(fila)
    return T

def mul(A, B):
    rA, cA = shape(A)
    rB, cB = shape(B)
    if cA != rB:
        raise ValueError("Dimensiones incompatibles para multiplicación")
    C = []
    for i in range(rA):
        fila = []
        for j in range(cB):
            s = 0
            for k in range(cA):
                s += A[i][k] * B[k][j]
            fila.append(s)
        C.append(fila)
    return C

def det(A):
    n, _ = shape(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    
    M = []
    for fila in A:
        M.append([float(x) for x in fila])
        
    sgn = 1
    
    for j in range(n):
        p = j
        maxv = abs(M[j][j])
        for i in range(j+1, n):
            if abs(M[i][j]) > maxv:
                maxv = abs(M[i][j])
                p = i
        
        if M[p][j] == 0:
            return 0
        
        if p != j:
            M[j], M[p] = M[p], M[j]
            sgn *= -1
            
        piv = M[j][j]
        
        for i in range(j+1, n):
            if piv == 0:
                continue
            fac = M[i][j] / piv
            for k in range(j, n):
                M[i][k] -= fac * M[j][k]
                
    d = sgn
    for i in range(n):
        d *= M[i][i]
        
    return d

def print_matrix(A):
    for fila in A:
        fila_str = " ".join(str(int(x)) for x in fila)
        print(fila_str)

# ----------------------------------
# Función nueva: Matriz identidad
# ----------------------------------
def identity(n):
    """Genera una matriz identidad n×n"""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# ====================================================
# ====================   MENÚ   ======================
# ====================================================

def read_square_matrix(name, n):
    M = []
    print("Ingrese", n, "filas de", n, "valores enteros (separados por espacio) para", name, ":")
    for i in range(n):
        while True:
            fila_str = input(name + "[fila " + str(i) + "]: ").strip().split()
            if len(fila_str) != n:
                print("Cantidad incorrecta. Reintente.")
                continue
            try:
                fila = [int(x) for x in fila_str]
                M.append(fila)
                break
            except ValueError:
                print("Ingrese solo números enteros válidos.")
    return M

def do_all_ops(A, B):
    print("\n--- Suma A + B ---")
    print_matrix(add(A, B))
    print("\n--- Multiplicación A × B ---")
    print_matrix(mul(A, B))
    print("\n--- Transposición Aᵀ ---")
    print_matrix(transpose(A))
    print("\n--- Transposición Bᵀ ---")
    print_matrix(transpose(B))
    print("\n--- Determinante det(A) ---")
    print(int(round(det(A))))
    print("\n--- Determinante det(B) ---")
    print(int(round(det(B))))

def menu(n):
    mats = {"A": None, "B": None}
    
    while True:
        print("\n=== CALCULADORA DE MATRICES n×n ===")
        print("1. Cargar matriz A")
        print("2. Cargar matriz B")
        print("3. Imprimir A, B o matriz identidad")
        print("4. Sumar A + B")
        print("5. Multiplicar A × B")
        print("6. Transponer A o B")
        print("7. Determinante det(A) o det(B)")
        print("8. HACER TODAS las operaciones")
        print("0. Salir")
        op = input("> ").strip()
        
        if op == "0":
            print("Hasta luego!")
            break
            
        try:
            if op == "1":
                mats["A"] = read_square_matrix("A", n)
            elif op == "2":
                mats["B"] = read_square_matrix("B", n)
            
            elif op == "3":
                w = input("¿Imprimir (A/B/I)? ").strip().upper()
                if w == "I":
                    print("\n--- Matriz identidad ---")
                    I = identity(n)
                    print_matrix(I)
                    mult = input("¿Multiplicar la identidad por (A/B) o Enter para no multiplicar? ").strip().upper()
                    if mult in ("A", "B") and mats[mult] is not None:
                        print(f"\n--- I × {mult} ---")
                        print_matrix(mul(I, mats[mult]))
                    elif mult in ("A", "B") and mats[mult] is None:
                        print(f"Error: La matriz {mult} no ha sido cargada.")
                else:
                    if mats[w] is None:
                        print(f"Error: La matriz {w} no ha sido cargada.")
                    else:
                        print_matrix(mats[w])
                    
            elif op == "4":
                if mats["A"] is None or mats["B"] is None:
                    print("Error: Debe cargar las matrices A y B primero.")
                else:
                    print_matrix(add(mats["A"], mats["B"]))
                    
            elif op == "5":
                if mats["A"] is None or mats["B"] is None:
                    print("Error: Debe cargar las matrices A y B primero.")
                else:
                    print_matrix(mul(mats["A"], mats["B"]))
                    
            elif op == "6":
                w = input("¿Transponer (A/B)? ").strip().upper()
                if mats[w] is None:
                    print(f"Error: La matriz {w} no ha sido cargada.")
                else:
                    print_matrix(transpose(mats[w]))
                    
            elif op == "7":
                w = input("¿Determinante (A/B)? ").strip().upper()
                if mats[w] is None:
                    print(f"Error: La matriz {w} no ha sido cargada.")
                else:
                    print(int(round(det(mats[w]))))
                    
            elif op == "8":
                if mats["A"] is None or mats["B"] is None:
                    print("Error: Debe cargar las matrices A y B primero.")
                else:
                    do_all_ops(mats["A"], mats["B"])
                    
            else:
                print("Opción inválida.")
                
        except KeyError:
            print("Error: Matriz no válida. Elija 'A' o 'B'.")
        except Exception as e:
            print("Error inesperado:", e)

def main():
    while True:
        try:
            n = int(input("Ingrese el tamaño n de las matrices cuadradas(n×n) (Mínimo 2 hasta 4): "))
            if n < 2 or n > 4:
                print("El tamaño debe ser entre 2 y 4.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")
    menu(n)

if __name__ == "__main__":
    main()
