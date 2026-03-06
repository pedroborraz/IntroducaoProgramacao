"""
Faça um programa que realize a divisão inteira entre dois números sem usar o operador /.
O programa deve calcular o quociente e o resto usando apenas while e operadores aritméticos (+ e -).
"""

num1 = int(input("Digite o primeiro numero(dividendo): "))
num2 = int(input("Digite o segundo numero(divisor): "))

if (num2 == 0):
    print("Divisao por zero nao e permitida.")
else:
    quociente = 0 
    resto = num1

    while (resto >= num2):
        resto -= num2
        quociente += 1

    print(f"Divisao inteira: {quociente}")
    print(f"Resto: {resto}")

    # na mat. o quociente e o numero de vezes que o divisor cabe no dividendo o resto e o que sobra apos isso