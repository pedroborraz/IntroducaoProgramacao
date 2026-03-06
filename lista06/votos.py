"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de
eleitores, leia os votos consistindo nos números dos candidatos (você define tais números)
e, ao final, exiba o número de votos de cada um recebeu.
"""

eleitores = int(input("Digite o numero de eleitores: "))

candidato_um = 0
candidato_dois = 0 
candidato_tres = 0
for i in range(eleitores):
    print("Candidatos disponiveis: 1 - 2 - 3")
    voto = int(input("Digite o numero do candito que deseja votar: "))
    if voto == 1:
        candidato_um += 1
    elif voto == 2:
        candidato_dois += 1
    elif voto == 3:
        candidato_tres += 1 
    else:
        print("Numero de candidato invalido!")
        
print(f"O candidato 1 recebeu {candidato_um}")
print(f"O candidato 2 recebeu {candidato_dois}")
print(f"O candidato 3 recebeu {candidato_tres}")