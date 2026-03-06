"""
Escreva um programa que leia um número e verifique se ele é primo. Para fazer essa
verificação, calcule o resto da divisão do número informado por todos os número menores
que ele a partir de 2. Se o resto de uma dessas divisões for igual a 0, o número não é
primo. Note que 0 e 1 não são primos e que 2 é o único primo que é par.
"""

numero = int(input("Digite um numero inteiro positivo: "))

primo = True
if numero <= 1:
    print("Numero nao e primo")
else:
    for i in range (2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("Numero informado e primo")
    else:
        print("Numero informado nao e primo")