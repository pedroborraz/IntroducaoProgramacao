"""
Define uma função que retorna o valor de caractere 'P', se seu argumento for positivo, e 
'N', se seu argumento for zero ou negativo.
"""

def positivo_negativo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'
    
def main():
    numero = float(input("Digite um numero: "))
    resultado = positivo_negativo(numero)
    print(f"O numero {numero} e: {'positivo' if resultado == 'P' else 'negativo ou zero'}")

if __name__ == "__main__":
    main()