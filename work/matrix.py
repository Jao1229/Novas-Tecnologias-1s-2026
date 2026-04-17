#matrix.py

def transpor_matriz(matriz):
    if not matriz:
        return []
    
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    
    transposta = [[matriz[i][j] for i in range(qtd_linhas)] for j in range(qtd_colunas)]
    
    return transposta


def multiplicar_matriz(matriz_a, matriz_b):

    linhas_a = len(matriz_a)
    cols_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    cols_b = len(matriz_b[0])

    if cols_a != linhas_b:
        print("Erro: O número de colunas de A deve ser igual ao número de linhas de B.")
        return None

    resultado = [[0 for _ in range(cols_b)] for _ in range(linhas_a)]

    for i in range(linhas_a):          
        for j in range(cols_b):        
            for k in range(cols_a):     
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado