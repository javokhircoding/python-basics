a = input("Enter the number: ")
try:
    a = int(a)
except ValueError:
    print("Enter the init number!")
else:
    print(a)
print("The programm is still working")


#here is some types of Errors
ValueError
ZeroDivisionError
NotADirectoryError
NotImplementedError
SyntaxError
SystemError
IndentationError
IndexError
KeyError
FileExistsError
FileNotFoundError
