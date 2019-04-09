names = {'1':'Mary','2':'John','3':'Bob','4':'Mel','5':'Jen','6':'Sue','7':'Ken','8':'Dave','9':'Beth','10':'Ray'}
hourrates = {40:15.00,25:22.00,4:35.00,62:43.00,33:17.00,45:29.00,36:40.00,17:20.00,37:37.00,80:16.50}

a = 0
for hour, payrate in hourrates.items():
    a = a + 1
    if hour > 40:
        salary = 40 * payrate + (hour-40) * 1.5 * payrate
        print(names[str(a)] + ' earned',salary)
    else:
        salary = hour * payrate
        print(names[str(a)] + ' earned',salary)
