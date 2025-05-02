#Crie um programa que escolha um aluno aleatoriamente entre quatro alunos e mostre eles em ordem.

import random

N = ['Daniela', 'Andrey', 'Ayla', 'Bruno']

NM = random.sample(N, 4)

print(f'O aluno escolido foi {NM}')