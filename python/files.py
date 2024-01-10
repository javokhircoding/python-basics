filename = 'data.txt'
with open(filename, 'w') as f:
    while True:
        a = input("Enter something: ")
        if a != 'stop':
            f.write(a)
        else:
            break
with open(filename) as p:
    c = p.read()
for x in c:
    print(x)
print(c)