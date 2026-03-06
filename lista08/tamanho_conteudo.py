"""
Faça um programa que leia duas strings e informe o conteúdo delas seguido do seu 
comprimento. Informe também se as duas strings possuem o mesmo comprimento e são 
iguais ou diferentes no conteúdo.
"""

def operacoes(str01, str02):
    if len(str01) == len(str02):
        comprimento = "mesmo comprimento"
    else:
        comprimento = "comprimentos diferentes"
    if str01 == str02:
        conteudo =  "mesmo conteudo"
    else:
        conteudo =  "conteudos diferentes"

    return comprimento, conteudo


def main():
    str01 = input("Digite a primeira string: ")
    str02 = input("Digite a segunda string: ")

    comprimento, conteudo = operacoes(str01, str02)

    print(f"String 1: '{str01}' (Tamanho: {len(str01)} caracteres)")
    print(f"String 2: '{str02}' (Tamanho: {len(str02)} caracteres)")
    print(f"As strings possuem {comprimento}")
    print(f"As strings possuem {conteudo}")

if __name__ == "__main__":
    main()