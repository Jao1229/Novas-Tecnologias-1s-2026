from matrix import transpor_matriz, multiplicar_matriz

print("--- Teste de Transposição ---")
A_transp = [[1, 2], [3, 4], [5, 6]]
resultado_transp = transpor_matriz(A_transp)

print(f"Entrada: {A_transp}")
print(f"Saída:   {resultado_transp}")
print("-" * 30)

print("\n--- Teste de Multiplicação ---")
A_mult = [[1, 2], [3, 4]]
B_mult = [[5, 6], [7, 8]]
resultado_mult = multiplicar_matriz(A_mult, B_mult)

print(f"Matriz A: {A_mult}")
print(f"Matriz B: {B_mult}")
print(f"Resultado: {resultado_mult}")