#Escreva um programa que calcule o valor a ser pago por um aluguel de carro. O programa deve solicitar o número de dias que o carro foi alugado e a quantidade de quilômetros rodados. O preço do aluguel é de R$ 60,00 por dia e R$ 0,15 por quilômetro rodado. O programa deve calcular e exibir o valor total a ser pago.

D = int(input('Quantos dias o carro foi alugado? '))
K = float(input('Quantos quilometros foram rodados? '))

Dia = 60
Km = 0.15

T = (D * Dia) + (K * Km)

print(f'O valor total a ser pago pelo aluguel do carro e: R$ {T:.2f}')