"""
No século XIII, o matemático Leonardo Pisa, conhecido como Fibonacci, propôs a seguinte
sequência: (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...). Essa sequência tem uma lei de formação
simples; cada elemento, a partir do terceiro, é obtido somando-se os dois anteriores. Veja:
1+1=2, 2+1=3, 3+2=5 e assim por diante. Faça um programa que leia um número inteiro n
e exiba na tela a sequência de Fibonacci com nelementos.
"""

elementos = int(input("Digite a quantidade de elementos na sequencia de Fibonacci: "))

if elementos <= 0:
    print("Numero invalido!")
elif elementos == 1:
    print("Sequencia de Fibonacci com 1 elemento:")
    print("1")
elif elementos == 2:
    print("Sequencia de Fibonacci com 2 elementos:")
    print("1 1")
else:
    print("Sequencia de Fibonacci com", elementos, "elementos:")
    anterior = 1
    atual = 1
    print(anterior, atual, end=" ")
    for i in range(2, elementos):
        proximo = anterior + atual
        print(proximo, end=" ")
        anterior = atual
        atual = proximo
    print()