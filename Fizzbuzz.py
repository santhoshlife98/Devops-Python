'''Title: FizzBuzz'''
'''Authore: SanthoshBheeman'''

n=int(input("Enter the Range:"))
for i in range(n):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
