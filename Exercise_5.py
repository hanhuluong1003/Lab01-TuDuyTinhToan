import os

with open("output.txt", 'w') as file:
    text = "I'm a student\n"
    file.write(text)
    file.write(f"{1/7:.5f}\n")

    print("Enter a:")
    a = int(input())
    print("Enter b:")
    b = int(input())

    file.write(str(a + b))

    file.write('\n')

    name = input("Enter file name:")

    if(os.path.isfile(name)):
        file.write("Exist")
    else:
        file.write("Not Exist")