"""
Escreva um programa que leia frases repetidamente e gere um dicionário para cada uma,
onde as chaves são os caracteres e os valores são a frequência de aparição.
O programa encerra quando o usuário digitar -1.
Exemplo: Para "Dados", o dicionário seria {'D': 2, 'a': 1, 'd': 2, 'o': 1, 's': 1}.
"""

frase = input("Digite uma frase (ou -1 para encerrar): ")
while frase != "-1":
    contagem_geral = {}
    for letra in frase.lower():
        if letra != " ":
            if letra in contagem_geral:
                contagem_geral[letra] += 1
            else:
                contagem_geral[letra] = 1   
            # contagem ignorando os espacos e considerando maiusculas e minusculas como iguais

    letras_contador = {}
    for letra in frase:
        if letra != " ":
            letras_contador[letra] = contagem_geral[letra.lower()]
        # contagem que diferencia maisculas e minusculas (como pede no exemplo)

    print(letras_contador)
    frase = input("Digite outra frase (ou -1 para encerrar): ")