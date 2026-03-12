"""
Desenvolva um jogo da forca. O programa terá uma lista de palavras como entrada e 
escolherá uma aleatoriamente. O jogador poderá errar seis vezes antes de ser enforcado.
"""

from random import choice

def criar_lista_palavras(palavras):
    lista = []
    palavra = ""

    for caractere in palavras:
        if caractere == " ":
            lista.append(palavra)
            palavra = ""
        else:
            palavra += caractere

    lista.append(palavra) # add ultima palavra caso o ultimo caractere nao seja um espaco
    return lista

def escolher_palavra(lista):
    return choice(lista)

def tentativa(palavra, palavra_oculta, letra):

    posicoes = []
    for i in range(len(palavra)):
        if palavra[i] == letra and palavra_oculta[i] == "_": # verifica se a letra esta na palavra e se ainda nao foi revelada
            posicoes.append(i)

    if len(posicoes) > 0: # se tiver posicoes, retorna a lista de posicoes onde a letra foi encontrada
        return posicoes
    return -1 # se nao for encontrada, retorna -1

def main():
    palavras = input("Digite uma lista de palavras separadas por um espaço: ")
    lista_palavras = criar_lista_palavras(palavras)
    palavra = escolher_palavra(lista_palavras)

    palavra_oculta = "_" * len(palavra)
    erros = 0
    letras_usadas = []

    while erros < 6 and "_" in palavra_oculta:
        print(f"Palavra: {palavra_oculta} possui {len(palavra)} letras")
        if letras_usadas:
            print(f"Letras ja usadas: {', '.join(letras_usadas)}")
        letra = input("Digite uma letra: ")

        if letra in letras_usadas:
            print(f"Voce ja tentou a letra '{letra}' tente outra")
            continue

        letras_usadas.append(letra)
        resultado_tentativa = tentativa(palavra, palavra_oculta, letra)

        if resultado_tentativa != -1: # se a letra foi encontrada, atualiza a palavra oculta revelando as letras encontradas
            for p in resultado_tentativa:
                palavra_oculta = palavra_oculta[:p] + letra + palavra_oculta[p + 1:]
        else:
            erros += 1
            print(f"Voce errou pela {erros} vez tente de novo")

    if "_" not in palavra_oculta: # se nao tiver mais letras ocultas, o jogador venceu
        print(f"Voce acertou, a palavra era: {palavra}")
    else:
        print(f"Voce perdeu, a palavra era: {palavra}")

if __name__ == "__main__":
    main()