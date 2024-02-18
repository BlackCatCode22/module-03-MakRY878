#edited maximum and minimum


num = 0
tot = 0.0
max_num = None
min_num = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:

        fval = float(sval)
    except:
        print('Invalid Input')
        continue

    print(fval)

    num = num + 1
    tot = tot + fval


    if max_num is None or fval > max_num:
        max_num = fval
    if min_num is None or fval < min_num:
        min_num = fval

print('\n',tot)
if num > 0:
    print('\nMaximum:', max_num)
    print('\nMinimum:', min_num)
else:
    print('no valid numbers entered.')

print('\nAll Done')
#print('\n', tot,'\n',num,'\n',tot/num)