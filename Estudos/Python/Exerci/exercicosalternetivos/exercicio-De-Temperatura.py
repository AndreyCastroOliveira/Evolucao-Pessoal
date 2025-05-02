A = input('Digite seu tipo de temeperatura: ')

if A == 'C e K':
    C = float(input('Digite a temperatura em Celsius: '))
    K = C + 273.15
    print(f'A temperatura em Kelvin e {K:.2f}')

elif A == 'C e F':
    C = float(input('Digite a temperatura em Celsius: '))
    F = (C * 9/5) + 32
    print(f'A temperatura em Fahrenheit e {F:.2f}')

elif A == 'F e K':
    F = float(input('Digite a temperatura em Fahrenheit: '))
    K = ((F - 32) * 5/9) + 273.15
    print(f'A temperatura em Kelvin e {K:.2f}')

elif A == 'F e C':
    F = float(input('Digite a temperatura em Fahrenheit: '))
    C = (F - 32) * 5/9
    print(f'A temperatura em Celsius e {C:.2f}')

elif A == 'K e C':
    K = float(input('Digite a temperatura em Kelvin: '))
    C = K - 273.15
    print(f'A temperatura em Celsius e {C:.2f}')

else:
    K = float(input('Digite a temperatura em Kelvin: '))
    F = ((K - 273.15) * 9/5) + 32
    print(f'A temperatura em Fahrenheit e {F:.2f}')

