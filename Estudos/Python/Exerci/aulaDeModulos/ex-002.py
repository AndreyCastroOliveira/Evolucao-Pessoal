#Crie um programa que leia o cateto oposto e o cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot 

Co = float(input('Digite o cateto oposto: '))
Ca = float(input('Digite o cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(Co, Ca):.2f}')

##O import foi usado para buscar a tag hypot que e usada para calcular a hipotenusa
