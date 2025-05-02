month = int(input('Qual o mês do ano? '))  # Using `int()` to convert input to an integer

if month in (1, 2, 3):
    print('It\'s winter')  # Professional casing

elif month in (4, 5, 6):
    print('It\'s spring')

elif month in (7, 8, 9):
    print('It\'s summer')

elif month in (10, 11, 12):
    print('It\'s autumn')

else:
    print('Invalid input. Please enter a number between 1 and 12.')

