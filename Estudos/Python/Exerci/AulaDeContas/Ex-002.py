#Crie um programa que leia um número inteiro e mostre na tela o seu dobro, triplo e raiz quadrada.

N = int(input('digite um numero: '))

D = N * 2
T = N * 3
R = N ** (1/2)

print(f'O dobro de {N} e {D}, o triplo e {T} e a raiz quadrada e {R:.2f}')

#Para fazer esse programa, basta multiplicar o numero por 2 e 3, e a raiz quadrada e feita com o operador **, que e o mesmo que elevar a potencia, e no caso da raiz quadrada, e elevado a 1/2