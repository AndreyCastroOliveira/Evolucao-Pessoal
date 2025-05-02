#Crie um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.

from math import sin, cos, tan

A = int(input('Digite o angulo: '))

print(f'O angulo de {A} tem o seno de {sin(A):.2f}')
print(f'O angulo de {A} tem o cosseno de {cos(A):.2f}')
print(f'O angulo de {A} tem a tangente de {tan(A):.2f}')

#O import foi usado para buscar as tags sin, cos, tan que sao usadas para calcular seno, cosseno e tangente respectivamente