"""
Escreva um programa que elimina os brancos de uma string digitada pelo usuário. (Dica: 
Crie uma nova string, atribuindo a ela os caracteres digitados que são diferentes de 
branco)
"""

def eliminar_espacos(texto):
    nova_string = ""
    
    for caractere in texto:
        if caractere != " ":
            nova_string += caractere

    return nova_string

def main():
    texto = input("Digite uma string: ")
    resultado = eliminar_espacos(texto)
    print("String sem espacos:", resultado)

if __name__ == "__main__":
    main()