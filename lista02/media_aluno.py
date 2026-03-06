"""
Faça um programa que calcule a média de um aluno a partir de duas notas e atribua um conceito.
Conceitos:
- A: média >= 9
- B: média >= 7.5
- C: média >= 6
- D: média >= 4
- E: média < 4
"""

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 9):
    print(f"Sua media e {media:.2f} com o conceito A")
elif (media >= 7.5):
    print(f"Sua media e {media:.2f} com o conceito B")
elif (media >= 6):
    print(f"Sua media e {media:.2f} com o conceito C")
elif (media >= 4):
    print(f"Sua media e {media:.2f} com o conceito D")
else:
    print(f"Sua media e {media:.2f} com o conceito E")