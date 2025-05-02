#crie um programa que sorteie um aluno entre quatro alunos e mostre o nome do aluno escolhido

import random

N = ['Daniela', 'Andrey', 'Ayla', 'Bruno']

NM = random.choice(N)

print(f'O aluno escolido foi {NM}')

#O import foi usado para buscar a tag random que e usada para gerar um numero aleatorio