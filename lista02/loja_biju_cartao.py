"""
Faça um programa que calcule o desconto em uma loja de bijuteria com múltiplas formas de pagamento.
Formas de pagamento:
- D (dinheiro): 10% de desconto se valor >= R$100
- C (cheque): sem desconto
- CD (cartão de débito): sem desconto
- CC (cartão de crédito): sem desconto, permite parcelamento em até 3 vezes
"""

valor_produto = float(input("Digite o valor do produto: R$"))
forma_pagamento = input("Digite a forma de pagamento (D para dinheiro, C para cheque, CD para cartao de debito e CC para cartao de credito): ")

if (valor_produto >= 100 and forma_pagamento.upper() == "D"):
    print(f"Voce ganhou 10% de desconto, o produto ficou por {(valor_produto * 0.9):.2f}")
elif (forma_pagamento.upper() == "C"):
    print(f"Voce nao tem desconto, o produto ficou por {valor_produto:.2f}")
elif (forma_pagamento.upper() == "CD"):
    print(f"Voce nao tem desconto, o produto ficou por {valor_produto:.2f}")
elif (forma_pagamento.upper() == "CC"):
    num_parcela = int(input("Quantas parcelas? Voce pode dividir em ate 3 vezes: "))
    if (num_parcela <=3):
        print(f"Voce nao tem desconto, o produto ficou por {valor_produto:.2f} em {num_parcela} parcela(s) de {(valor_produto / num_parcela):.2f} ")
    else:
        print("Numero de parcelas invalidas.")
else:
    print("Forma de pagamento invalida.")