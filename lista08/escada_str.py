"""
Escreva um programa em Python que  receba uma string e a imprima na vertical e em 
formato de escada.
Se a string for "Fulano", a saida deve ser:
F
Fu
Ful
Fula
Fulano
"""

def imprimir_vertical_escada(texto):

    string = ""
    for i in range(len(texto)):
        string += texto[:i+1] + "\n"

    return string

def main():
    texto = input("Digite uma string: ")
    resultado = imprimir_vertical_escada(texto)
    print(resultado)

if __name__ == "__main__":
    main()