"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
"""

numero = int(input("Qual numero voce quer saber a tabuada? "))

print("Tabuada de ", numero)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
