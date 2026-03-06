"""
Escreva um programa que leia as coordenadas de N pontos do plano cartesiano e exiba as distâncias mínima, máxima e média entre eles.
Os pontos devem ser representados como uma lista de tuplas.
Deve-se utilizar a distância euclidiana para o cálculo.
distancia euclidiana ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
ponto = (x1, y1), pontos = [(x1, y1), (x2, y2), ...]
"""


n_pontos = int(input("Quantos pontos voce quer informar? "))

lista_pontos = []
for i in range(n_pontos):
    ponto = []
    for j in range(2):
        ponto.append(float(input(f"Digite o ponto[{i+1}][{j+1}]: ")))
    ponto_tupla = (ponto[0], ponto[1]) # convertendo a lista para tupla a cada dois elementos, representando um ponto
    lista_pontos.append(ponto_tupla)

print(lista_pontos)

distancias = []
for i in range(n_pontos):
    for j in range(i + 1, n_pontos): # i + 1 para evitar calcular a distancia do mesmo ponto 
        distancia = ((lista_pontos[i][0] - lista_pontos[j][0]) ** 2 + (lista_pontos[i][1] - lista_pontos[j][1]) ** 2) ** 0.5
        distancias.append(distancia)
        # a distancia e calculada para cada par de pontos

if distancias: # se a lista estiver vazia nao entra no bloco
    soma_dist = 0
    dist_min = distancias[0]
    dist_max = distancias[0]
    for distancia in distancias:
        soma_dist += distancia
        if distancia < dist_min:
            dist_min = distancia
        if distancia > dist_max:
            dist_max = distancia
    media_dist = soma_dist / len(distancias)

    print(f"Distancia minima: {dist_min:.2f}")
    print(f"Distancia maxima: {dist_max:.2f}")
    print(f"Distancia media: {media_dist:.2f}")
else:
    print("Nao ha distancias para calcular.")