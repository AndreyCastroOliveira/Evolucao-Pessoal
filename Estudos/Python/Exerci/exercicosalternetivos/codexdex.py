PL = int(input('Qual o planeta? '))
P = float(input('Digite seu peso: '))

if PL == 1:
  PL = P * 0.38
  print(f'Peso em Marte e em Mercurio e: {PL:.2f}')

elif PL == 3:
  PL = P * 0.38
  print(f'Peso em Mercurio e: {PL:.2f}')  

elif PL == 2:
  PL = P * 0.91
  print(f'Peso em venus: {PL:.2f}')

elif PL == 4:
  PL = P * 2.53
  print(f'Peso em jupiter e: {PL:.2f}')

elif PL == 5:
  PL = P * 1.07
  print(f'Peso em saturno e: {PL:.2f}')

elif PL == 6:
  PL = P * 0.89
  print(f'Peso em urano e: {PL:.2f}')

elif PL == 7:
  PL = P * 1.14
  print(f'Peso em Netuno e: {PL:.2f}')

else:
  print('escolha um planeta entre 1 e 7')