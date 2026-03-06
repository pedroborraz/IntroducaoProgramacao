"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá
verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))

soma_idades = 0
for i in range(1, quantidade_pessoas+1):
    idade = int(input(f"{i}. Digite a sua idade: "))
    soma_idades += idade

media = soma_idades / quantidade_pessoas
if media > 60:
    print("Essa turma e idosa!")
elif media >= 26:
    print("Essa turma e adulta!")
else:
    print("Essa turma e jovem!")