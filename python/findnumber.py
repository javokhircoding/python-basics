import random

def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"I think about numbers from 1 to {x}, find it!")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Wrong, My number is greatest than you think")
        elif taxmin > tasodifiy_son:
            print("Wrong, My number is smallest than you think")
        else:
            break
    print(f"You won, Congrutulations! You found it with {taxminlar} expectations")
    return taxminlar


def sontop_pc(x=10):
    input(print(f"Think numbers that from 1 to {x} and press the whatever bottom, I shall find it."))
    quyi = 1 
    yuqori = x 
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"It was {taxmin} right(y),"
                      f"if it's greatest than you think(+), it's less than you thin(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break

    print(f"I found it with {taxminlar} expectations")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user > taxminlar_pc:
            print("I won")
        elif taxminlar_user < taxminlar_pc:
            print("You won")
        else:
            print("Draw!")

        yana = int(input("You wanna play again, Yes(1)/No(0)"))


play()