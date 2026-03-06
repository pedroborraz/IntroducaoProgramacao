"""
Crie um programa que leia uma matriz 3x3 e troque os elementos da linha 2 pela coluna 2 e vice-versa.
"""

matriz = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posicao[{i+1}][{j+1}]: "))

print("A matriz original:")
for linha in matriz:
    print(linha)

nova_matriz = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        if i == 1 or j == 1: # verifica se esta na linha 2 ou na coluna 2 para fazer a troca
            nova_matriz[i][j] = matriz[j][i] # fixa a troca usando j para acessar a linha e i para acessar a coluna, invertendo os indices
        else:
            nova_matriz[i][j] = matriz[i][j] # normal para outras linhas/colunas

print("A matriz atualizada e:")
for linha in nova_matriz:
    print(linha)
print("Foi feita a troca da linha 2 pela coluna 2 e coluna 2 pela linha 2.")