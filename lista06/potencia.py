"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente (inteiro): "))

resultado = 1
for i in range(abs(expoente)):
    resultado *= base

if expoente < 0:
    resultado = 1 / resultado

print(f"{base} ** {expoente} = {resultado}")