"""
Faça um programa para imprimir: 
1
2 2
3 3 3
4 4 4 4
...
n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro 
imprima até a n-ésima linha.
"""

def triangulo_base(n):
    triangulo = ""
    for i in range(1, n + 1):
        triangulo += f"{i} " * i + "\n"
    return triangulo

def main():
    n = int(input("Digite um numero inteiro positivo: "))
    resultado = triangulo_base(n)
    print(resultado)

if __name__ == "__main__":
    main()