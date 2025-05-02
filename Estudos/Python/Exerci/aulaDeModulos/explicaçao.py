#As bibliotecas sao um conjunto de tags que podem ser usadas para expandir o funcionamento do python
#Por exemplo, o math que e uma biblioteca que tem um conjunto de funcoes matematicas

import math

n = float(input('Digite um numero: '))
s = math.sqrt(n) #A funcao sqrt e uma funcao da biblioteca math que calcula a raiz quadrada de um numero

print(f'A raiz de {n} e {s:.2f}')# antes da string indica que e uma f-string, que permite interpolar variaveis dentro da string

#o math.ceil(s) arredonda o valor para cima 

#Tambem e possivel importar apenas uma funcao de uma biblioteca, com o comando from

from math import sqrt

n = float(input('Digite um numero: '))
s = sqrt(n)

print(f'A raiz de {n} e {s:.2f}')