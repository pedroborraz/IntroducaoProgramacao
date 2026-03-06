"""
Faça um programa que simule um sistema de vendas simples com uma tabela de preços.
O programa deve permitir ao usuário selecionar produtos pelo código (1-5), informar a quantidade desejada
e calcular o total da compra. O programa encerra quando o código 0 é digitado.
"""

tabela_preco = """
Codigo | Preco
----------------
1      | R$ 5.50
2      | R$ 2.30
3      | R$ 4.75
4      | R$ 6.80
5      | R$ 9.30
"""

print(tabela_preco)
msg_codigo = "Digite o codigo do produto (de 1-5 e 0 para sair): "
codigo_produto = int(input(msg_codigo))

while (codigo_produto != 0):
    quantidade = int(input("Digite a quantidade desejada: "))
    
    if (codigo_produto == 1):
        preço = 5.50
    elif (codigo_produto == 2):
        preço = 2.30
    elif (codigo_produto == 3):
        preço = 4.75
    elif (codigo_produto == 4):
        preço = 6.80
    elif (codigo_produto == 5):
        preço = 9.30
    else:
        print("Codigo invalido. Tente novamente.")
        codigo_produto = int(input(msg_codigo))
        continue
    
    total = preço * quantidade
    print(f"O total da compra e: R$ {total:.2f}")
    codigo_produto = int(input(msg_codigo))
