"""
Desenvolva um jogo da forca. O programa terá uma lista de palavras como entrada e 
escolherá uma aleatoriamente. O jogador poderá errar seis vezes antes de ser enforcado.
"""

from random import randint

def criar_lista_palavras(palavras):
    lista = []
    palavra = ""

    for caractere in palavras:
        if caractere == " ":
            lista.append(palavra)
            palavra = ""
        else:
            palavra += caractere

    lista.append(palavra) # caso nao termine com um espaço, adiciona a ultima palavra
    return lista

def escolher_palavra(lista):
    return lista[randint(0, len(lista) - 1)]

def jogo_forca(palavra, palavra_oculta, letra):

    for i in range(len(palavra)):
        if palavra[i] == letra and palavra_oculta[i] == "_":
            return i
        
    return "letra nao encontrada"

def main():
    palavras = input("Digite uma lista de palavras separadas por um espaço: ")
    lista_palavras = criar_lista_palavras(palavras)
    palavra = escolher_palavra(lista_palavras)

    palavra_oculta = "_" * len(palavra)
    erros = 0

    while erros < 6 and "_" in palavra_oculta:
        print(f"Palavra: {palavra_oculta} possui {len(palavra)} letras")
        letra = input("Digite uma letra: ")
        posicao = jogo_forca(palavra, palavra_oculta, letra)

        if posicao != "letra nao encontrada":
            palavra_oculta = palavra_oculta[:posicao] + letra + palavra_oculta[posicao + 1:] # _ ate a posicao da letra certa + letra certa + o resto de _
        else:
            erros += 1
            print(f"Voce errou pela {erros} vez! Tente de novo.")

    if "_" not in palavra_oculta:
        print(f"Voce acertou! A palavra era: {palavra}")
    else:
        print(f"Voce perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    main()