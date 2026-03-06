"""
Faça um programa que leia continuamente números do usuário até que -1 seja digitado.
Ao final, o programa deve exibir o menor, o maior e a soma de todos os números informados.
"""

num = float(input("Digite um numero (-1 para sair): "))
if (num == -1):
    print("Nenhum numero foi fornecido.")
    exit()

menor = num
maior = num
soma = 0

while (num != -1):
    if (num < menor):
        menor = num
    if (num > maior):
        maior = num
    soma += num
    num = float(input("Digite um numero (-1 para sair): "))

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Soma: {soma}")
