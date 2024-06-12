for i in range(0,5):
    for j in range(0,5):
        print('*', end='  ')
    print()







for i in range(5):
    for j in range(i):
        print('  ', end='')
    for j in range(5 - i, 0, -1):
        print(j, end=' ')
    print()