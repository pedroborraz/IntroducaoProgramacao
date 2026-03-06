"""
Faça um programa que calcule o peso ideal de uma pessoa de acordo com sua altura e sexo.
Para homens: Peso ideal = (72.7 * altura) - 58
Para mulheres: Peso ideal = (62.1 * altura) - 44.7
"""

altura = float(input("Digite sua altura em metros: "))
sexo = input("Voce e homem ou mulher?(H/M): ")

if (sexo.upper() == "H"):
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"O seu imc e igual a: {peso_ideal:.2f}")