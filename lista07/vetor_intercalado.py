"""
Faça um programa que leia dois vetores com cinco elementos cada
e gere um terceiro vetor de 10 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor1 = [None] * 5
for i in range(5):
    vetor1[i] = int(input(f"Digite o {i+1} valor inteiro para o primeiro vetor: "))

vetor2 = [None] * 5
for i in range(5):
    vetor2[i] = int(input(f"Digite o {i+1} valor inteiro para o segundo vetor: "))

vetor3 = [None] * 10
for i in range(10):
    if i % 2 == 0: # intercala por elementos par/impar ja que 1 impar e 2 par, 3 impar e 4 par, etc (alterna de 1 em 1)
        vetor3[i] = vetor1[i // 2]
    else:
        vetor3[i] = vetor2[i // 2]

print(f"Aqui esta o vetor resultante: {vetor3}")