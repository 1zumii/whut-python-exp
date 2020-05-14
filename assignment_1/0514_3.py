n = input('n: ')
if int(n) < 10:
    print(True)
else:
    test = list(n)
    test.reverse()
    if int(''.join(test)) == int(n):
        print(True)
    else:
        print(False)
