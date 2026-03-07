"""
Desenvolva um programa que solicite a digitação de um número de CPF no formato 
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos 
verificadores dos caracteres de formatação. (Dica: Pesquise na Internet como os números 
de CPF são formados)
"""

def digitos_cpf(cpf):
    lista_numeros = []

    for caractere in cpf:
        if caractere != "." and caractere != "-":
            lista_numeros.append(int(caractere))

    return lista_numeros

def validar_cpf(cpf):
    pesosdv1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesosdv2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # somatorio dos pesos vezes digitos do cpf
    soma1 = 0
    soma2 = 0

    for i in range(9):
        soma1 += cpf[i] * pesosdv1[i]
        soma2 += cpf[i] * pesosdv2[i]

    dv1 = 11 - (soma1 % 11)

    if dv1 >= 10:
        dv1 = 0

    soma2 += dv1 * pesosdv2[9] # termina de calcular a soma do dv2, incluindo o dv1

    dv2 = 11 - (soma2 % 11)

    if dv2 >= 10:
        dv2 = 0

    if dv1 == cpf[9] and dv2 == cpf[10]:
        return "CPF valido"
    else:
        return "CPF invalido"

def main():
    cpf = input("Digite um numero de CPF no formato xxx.xxx.xxx-xx: ")
    digitos = digitos_cpf(cpf)
    resultado = validar_cpf(digitos)
    print(resultado)

if __name__ == "__main__":
    main()