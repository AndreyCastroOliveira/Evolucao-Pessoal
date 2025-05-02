#Crie um programa que leia um número qualquer e mostre na tela o seu valor inteiro

import math

n = float(input('Digite um numero: '))

print(f'O numero {n} tem a parte inteira {math.floor(n)}')#A funcao floor e uma funcao da biblioteca math que arredonda o valor para baixo
