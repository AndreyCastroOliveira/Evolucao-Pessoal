#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

A = float(input('Digite a largura da parede em metros: '))

L = float(input('Digite a altura da parede em metros: '))

Area = A * L

print(f'A area da parede e: {Area:.2f} m²')

T = Area / 2

print(f'A quantidade de tinta necessária para pintar a parede e: {T:.2f} L')