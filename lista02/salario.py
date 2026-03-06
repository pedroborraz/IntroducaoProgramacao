"""
Faça um programa que calcule o salário de um funcionário a partir do valor da hora e horas trabalhadas.
Descontos aplicados:
- Imposto de Renda: 11%
- INSS: 8%
- Sindicato: 5%
"""

valor_hora = float(input("Quanto voce ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas voce trabalha por mes? "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato 

print(f"Salario bruto: R${salario_bruto:.2f}")
print(f"IR: R${imposto_renda:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salario liquido: R${salario_liquido:.2f}")