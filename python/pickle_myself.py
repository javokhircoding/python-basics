with open('practise.txt', 'w') as file:
    while True:
        a = str(input('Enter something: '))
        if a != 'stop':
            file.write(a)
        else:
            print("System has stopped!")
            break


with open('practise.txt') as file:
    p = file.read()
    print(p)