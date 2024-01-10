#!usr/bin/python


import typer
import time
from uuid import uuid4
import random



i = 0

while i < 10000000000000:

    a = uuid4()
    b = uuid4()
    c = uuid4()
    e = uuid4()
    k = uuid4()

    d = [2, 3, 4, 2]
    f = random.choice(d)

    if f == 2:
        print(typer.style(f"{a}-{b}", fg=typer.colors.GREEN))

    elif f == 3:
        print(typer.style(f"{a}-{b}-{c}", fg=typer.colors.GREEN))

    elif f == 4:
        print(typer.style(f"{a}-{b}-{c}-{e}", fg=typer.colors.GREEN))