a = 1
while a<=100:
    if a/15 == int(a/15):
        print('FizzBuzz')
    elif a/3 == int(a/3):
        print('Fizz')
    elif a/5 == int(a/5):
        print('Buzz')
    else:
        print(a)
    a = a + 1
