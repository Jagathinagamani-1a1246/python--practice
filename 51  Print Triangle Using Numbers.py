# 51. Print Triangle Using Numbers

""" with arguements and no return values"""
def num(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
n=int(input("Enter value:"))
num(n)

""" with no arguements and no return values"""
def num():
    n=int(input("Enter value:"))
    for i in range(1,n):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
num()

""" with no arguements and return values"""
def num():
    n=int(input("Enter value:"))
    for i in range(1,n):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
num()
