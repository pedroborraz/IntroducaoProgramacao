"""
Faça uma função que retorne a quantidade de dígitos de um determinado número inteiro 
passado por parâmetro.
"""

def quantidade_digitos(numero):
    numero_string = ""
    for digito in numero:
        if digito == '-' or digito == '+':
            continue
        numero_string += digito
    return len(numero_string)

def main():
    numero = input("Digite um numero inteiro: ")
    resultado = quantidade_digitos(numero)
    print(f"O numero {numero} tem {resultado} digitos.")

if __name__ == "__main__":
    main()