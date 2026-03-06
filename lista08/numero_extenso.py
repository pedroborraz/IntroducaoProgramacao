"""
Escreva um programa que solicite ao usuário que digite um número de 1 a 99 e imprima-o 
na tela por extenso.
"""

def numero_por_extenso(numero):

    unidades = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    segunda_dezena = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return segunda_dezena[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10
        if unidade == 0:
            return dezenas[dezena-1]
        else:
            return f"{dezenas[dezena-1]} e {unidades[unidade]}"


def main():
    numero = int(input("Digite um numero de 1 a 99: "))
    resultado = numero_por_extenso(numero)
    print(resultado)

if __name__ == "__main__":
    main()