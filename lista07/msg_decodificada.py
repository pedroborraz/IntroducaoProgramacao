"""
Duas amigas estabeleceram um código onde cada letra equivale a um número entre 1 e 26, e o espaço ao 0.
O programa deve receber uma lista de números representando uma mensagem codificada, armazená-los em uma lista e traduzi-los de acordo com o código fornecido.
"""

entrada = input("Digite os numeros da mensagem separados por espaço(0-26): ")

lista_numeros = []
memoria = ""
for numero in entrada:
        if numero != " ":
            memoria += numero
        else:
            if memoria != "":
                lista_numeros.append(int(memoria))
                memoria = ""

if memoria != "": # para ter certeza de que o ultimo numero seja adicionado a lista caso a entrada nao termine com um espaco
    lista_numeros.append(int(memoria))

alfabeto = " abcdefghijklmnopqrstuvwxyz"
mensagem_decodificada = ""
for numero in lista_numeros:
    if 0 <= numero <= 26:
        mensagem_decodificada += alfabeto[numero] # concatena a letra correspondente ao numero na mensagem decodificada
    else:
        print(f"encontrado numero fora do intervalo:({numero}), ignorando...")

print(mensagem_decodificada) # para teste ola mundo = 15 12 1 0 13 21 14 4 15
