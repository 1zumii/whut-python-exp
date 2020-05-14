inputYear = int(input("year:"))
inputMonth = int(input("month:"))
inputDay = int(input("day:"))

monthMap = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

dayPostfix = ['1st', '2nd', '3rd']

if inputMonth not in range(1, 13):
    print('Error inputMonth\t', inputMonth)
elif inputDay not in range(1, 32):
    print('Error inputDay\t', inputDay)
else:
    d0 = inputDay % 10
    d1 = inputDay // 10
    if d0 in [1, 2, 3] and d1 is not 1:
        if d1 is 0:
            outputDay = '' + dayPostfix[d0 - 1]
        else:
            outputDay = str(d1) + dayPostfix[d0 - 1]
    else:
        outputDay = '{}th'.format(inputDay)
    print('\n{} {}, {}'.format(monthMap[inputMonth - 1], outputDay, inputYear))
