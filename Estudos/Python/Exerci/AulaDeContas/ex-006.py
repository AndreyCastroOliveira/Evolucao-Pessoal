#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27.

V = float(input('Digite o valor em reais: '))

Conversao = V / 3.27
print(f'Com {V} reais voce pode comprar {Conversao:.2f} dolares.')

#A formula dessa conta, e baseada na conversao do cambio do dolar, que e feio pelo: valor da moeda dividido pelo valor da segunda moeda que vale mais
