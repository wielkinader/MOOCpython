x = int(input('Number 1: '))
y = int(input('Number 2: '))

operinput = input('Operation: ')

adding = x + y
subtracting = x - y
multiplying = x * y

if operinput == 'add':
    print(f"{x} + {y} = {adding}")
elif operinput == 'multiply':
    print(f"{x} * {y} = {multiplying}")
elif operinput == 'subtract':
    print(f"{x} - {y} = {subtracting}")