"""
Escreva um programa em Python que simula o lançamento de um dado n vezes e imprime o percentual de surgimento de cada face.
O valor n é definido pelo usuário; o programa encerra se n for zero.
Deve-se utilizar um array para armazenar a contagem de cada face.
Dica: Use random.randint(ini, fim) para gerar os números aleatórios.
"""

import random

lancamentos = int(input("Digite o numero de vezes que o dado sera lancado(0 para sair): "))

while lancamentos != 0:
    contagem = [0] * 6 
    for _ in range(lancamentos):
        face = random.randint(1, 6) # escolhe uma face aleatoria do dado
        contagem[face - 1] += 1 # incrementa a contagem da face correspondente      
    print(contagem)

    print("Percentual de cada face:")
    for i in range(6):
        percentual = (contagem[i] / lancamentos) * 100
        print(f"Face {i+1}: {percentual:.2f}%")
    lancamentos = int(input("Digite o numero de vezes que o dado sera lancado(0 para sair): "))