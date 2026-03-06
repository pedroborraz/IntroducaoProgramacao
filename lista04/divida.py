"""
Faça um programa que calcule a quantidade de meses necessários para quitar uma dívida,
o total pago ao final e os juros totais pagos.
O programa simula o pagamento mês a mês com acréscimo de juros.
"""

valor_inicial = float(input("Digite o valor inicial da divida: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
pag_mensal = float(input("Digite o valor do pagamento mensal: R$ "))
meses = 0
total_pago = 0
valor_divida = valor_inicial

if (pag_mensal <= (valor_inicial * taxa_juros / 100)):
    print("O valor do pagamento mensal e insuficiente para cobrir os juros. A divida nunca sera quitada.")
else:
    while (valor_divida > 0):
        juros_mes = valor_divida * taxa_juros / 100
        valor_divida += juros_mes
        valor_divida -= pag_mensal
        total_pago += pag_mensal
        meses += 1
        if (valor_divida < 0): # ajustar o valor pago no ultimo mes, se necessario
            total_pago += valor_divida  
            valor_divida = 0

    juros_totais = total_pago - valor_inicial

    print(f"\nNumero de meses para quitar a divida: {meses} meses")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Juros pagos: R$ {juros_totais:.2f}")