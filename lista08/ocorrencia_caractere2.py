"""
Faça um programa que exiba na tela o número de ocorrências de cada caractere de uma 
frase digitada pelo usuário. A contagem dos caracteres deve ocorrer dentro de uma função 
que recebe uma string por parâmetro e retorna um dicionário cuja chave é o próprio 
caractere e o valor corresponde ao número de vezes que ele aparece na string.
"""

def contar_aparicoes_caracteres(frase):
    aparicoes = {}

    for caractere in frase:
        if caractere in aparicoes:
            aparicoes[caractere] += 1
        else:
            aparicoes[caractere] = 1

    return aparicoes

def main():
    frase = input("Digite uma frase: ")
    resultado = contar_aparicoes_caracteres(frase)
    print(resultado)

if __name__ == "__main__":
    main()