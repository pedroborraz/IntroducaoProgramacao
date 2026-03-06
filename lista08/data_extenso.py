"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o 
nome do mês por extenso. 
Ex.: 
Informe uma data: 25/10/2018 
Data por extenso: 25 de outubro de 2018. 
"""

def data_por_extenso(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    str_data = ""
    lista_data = []

    for caractere in data:
        if caractere != "/":
            str_data += caractere
        else:
            lista_data.append(str_data)
            str_data = ""

    lista_data.append(str_data)
    lista_data[1] = meses[int(lista_data[1]) - 1]

    return f"{lista_data[0]} de {lista_data[1]} de {lista_data[2]}."

def main():
    data = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    resultado = data_por_extenso(data)
    print("Data por extenso:", resultado)

if __name__ == "__main__":
    main()