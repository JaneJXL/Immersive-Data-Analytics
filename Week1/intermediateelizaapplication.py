firstg = input('Good day. What is your problem? Enter your response here or Q to quit: ')
good = 'false'

while good == 'false':
    if firstg == 'i am feeling great' or firstg =='Q' or firstg =='q':
       firstN =''
       firstN = firstN + 'you are feeling great'
       print(firstN)
       print('Have a nice day!')
       good = 'true'
    
    else:
        firstg_splt = firstg.split()
        replaces_dic = {'i':'you', 'me':'you', 'my':'your', 'am':'are'}
        res_E = ['','']

        for item in firstg_splt:
            firstN1 = ''   # create a new string
            firstN2 = ''
            count1 = 0
            count2 = 0
            count3 = 0
            for wo, ni in replaces_dic.items():
                if item != wo:
                    count1 = count1 + 1
                    if count1 <= 1:
                        firstN1 = firstN1 + item
                    else:
                        firstN1 = firstN1 + ''
                    count2 = count2 + 1
                    if count2 >= 4:
                        res_E.append(firstN1 + ' ')
                else:
                   item = ni
                   firstN2 = firstN2 + item
                   count3 = count3 + 1
                   if count3 <= 1:
                       res_E.append(firstN2 + ' ')
        print(''.join(res_E))
        firstg = input('Enter your response here or Q to quit: ')
        good == 'false'
