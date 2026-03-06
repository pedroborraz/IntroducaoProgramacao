"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros
no período.
"""

deposito = float(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite a taxa de juros da sua poupanca (sem %): "))

taxa_multiplicador = 1 + (taxa_juros / 100)
saldo = deposito
for mes in range(1, 25):
    saldo *= taxa_multiplicador
    print(f"Mes {mes}: R${saldo:.2f}")
total_juros = saldo - deposito

print(f"\nTotal ganho com juros no periodo: R${total_juros:.2f}")