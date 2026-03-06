"""
Faça um programa que calcule quantos anos são necessários para a população do país X
ultrapassar a população do país Y, considerando taxas de crescimento anual constantes para cada país.
País X: população inicial 70.000 e taxa de crescimento 3.5%
País Y: população inicial 180.000 e taxa de crescimento 1.5%
"""

populacao_X = 70000
populacao_Y = 180000
taxa_crescimento_X = 0.035
taxa_crescimento_Y = 0.015 
anos = 0

while (populacao_X <= populacao_Y):
    populacao_X += populacao_X * taxa_crescimento_X
    populacao_Y += populacao_Y * taxa_crescimento_Y
    anos += 1

print(f"Serao necessarios {anos} anos para a populacao do pais X ultrapassar a do pais Y.")