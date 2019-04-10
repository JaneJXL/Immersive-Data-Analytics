firstg = input('Good day. What is your problem? Enter your response here or Q to quit.\n')
good = 'false'

while good == 'false':
    if firstg == 'I am feeling great' or firstg == 'I AM FEELING GREAT' or firstg == 'i am feeling great' or firstg =='Q' or firstg =='q':
        print('Have a nice day!')
        good = 'true'
    else:
        firstg = input('Enter your response here or Q to quit.\n')
        good == 'false'
