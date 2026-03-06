"""
Escreva uma função que receba três argumentos (parâmetros) e retorne sua soma. Escreva 
um programa para testá-la.
"""

def soma_de_tres(a, b, c):
    return a + b + c

def main():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))
    resultado = soma_de_tres(valor1, valor2, valor3)
    print(f"A soma dos tres valores: {resultado}")

if __name__ == "__main__":
    main()