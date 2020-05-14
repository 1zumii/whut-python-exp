for i in range(1, 12):
    if i % 5 is 1:
        for k in range(1, 12):
            if k % 5 is 1:
                print('+', end=' ')
            else:
                print('-', end=' ')
    else:
        for k in range(1, 12):
            if k % 5 is 1:
                print('|', end=' ')
            else:
                print(' ', end=' ')
    print()
