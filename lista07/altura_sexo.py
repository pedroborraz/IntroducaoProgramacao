"""
Processar um conjunto de dados de altura e sexo (M/F) de 10 pessoas. O programa deve:
(a) Armazenar os dados em duas listas vinculadas (alturas e sexos).
(b) Determinar a maior e a menor altura, indicando o sexo desses indivíduos.
(c) Calcular a média de altura para o sexo feminino ('F') e para o sexo masculino ('M').
(d) Determinar o número total de indivíduos de cada sexo.
"""

altura = []
sexo = []

for i in range(10):
    altura.append(float(input(f"Digite a altura da pessoa {i+1}: ")))
    sexo.append(input(f"Digite o sexo da pessoa {i+1} (M/F): "))

maior_altura = altura[0]
menor_altura = altura[0]
sexo_maior = sexo[0]
sexo_menor = sexo[0]

soma_altura_f = 0
soma_altura_m = 0
n_mulheres = 0
n_homens = 0

for i in range(len(altura)):
    if altura[i] > maior_altura:
        maior_altura = altura[i]
        sexo_maior = sexo[i]
    if altura[i] < menor_altura:
        menor_altura = altura[i]
        sexo_menor = sexo[i]
        # compara a altura atual com a anterior a ser registrada como maior ou menor, e registra o sexo correspondente

    if sexo[i] == 'F':  
        soma_altura_f += altura[i]
        n_mulheres += 1
    else:
        soma_altura_m += altura[i]
        n_homens += 1

if n_mulheres > 0:
    media_feminina = soma_altura_f / n_mulheres
else:
    media_feminina = 0

if n_homens > 0:
    media_masculina = soma_altura_m / n_homens
else:
    media_masculina = 0
    
print(f"Maior altura: {maior_altura} m, Sexo: {sexo_maior}")
print(f"Menor altura: {menor_altura} m, Sexo: {sexo_menor}")
print(f"Media de altura para o sexo feminino (F): {media_feminina:.2f} m")
print(f"Media de altura para o sexo masculino (M): {media_masculina:.2f} m")
print(f"Numero total de individuos do sexo feminino (F): {n_mulheres}")
print(f"Numero total de individuos do sexo masculino (M): {n_homens}")