# iff divisble by three print fizz
# if divisible by 5 print buzz
#if divisble by both print fizzbuzz

num = int(input('Number: '))
f = 'Fizz'
b = 'Buzz'

if num % 3 == 0 and num % 5 == 0:
    print(f + b)
elif num % 3 == 0:
    print(f)
elif num % 5 == 0:
    print(b)

