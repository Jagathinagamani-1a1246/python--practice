
    






#  1. To find maximum of two numbers
def num():
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    if a>b:
        return a;
    else:
        return b;
maxnum = num()
print("Max of two numbers:\n",maxnum)

# 2. To find maximum of three numbers
def num(a,b,c):
    if a>b and a>c:
        return a;
    elif b>a and b>c:
        return b;
    else:
        return c;
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
maxnum = num(a,b,c)
print("Maximum number is:", maxnum)

# 3. Check whether a number is negative, positive or zero
def num():
    n=int(input("Enter n value:"))
    if n>0:
        return "positive";
    elif n<0:
        return "negative";
    else:
        return "zero";
check_num = num()
print(check_num)

#4.To check whether a number is divisible by 5 and 11 or not
"""with arguements and with return values"""
def num(n):
    if n%5==0 and n%11==0:
        return "divisible by both 5 and 11";
    else:
        return "not divisible"
n=int(input("enter value:"))
checknum=num(n)
print(checknum)

"""with return values and no arguements"""
def num():
    n=int(input("Enter n value:"))
    if n%5==0 and n%11==0:
        return "Divisible by both 5 and 11";
    else:
        return "Not Divisible"
checknum=num()
print(checknum)

#5. Check whether a number is even or odd
"""with arguements and with return values"""
def num(n):
    if n%2==0:
        return "n is even";
    else:
        return "n is odd";
n=int(input("Enter value:"))
check=num(n)
print("The number is:",check)

"""with return values and no arguements"""
def num():
    n=int(input("Enter value:"))
    if n%2==0:
        return "n is even";
    else:
        return "n is odd";
check=num()
print("The number is:",check)

#6. Check whether a year is Leap Year or not
"""with arguements and with return values"""
def year(n):
    if n%400==0 or n%4==0 and n%100!=0:
        return "LEAP YEAR";
    else:
        return "NOT LEAP YEAR";
n=int(input("Enter n value:"))
check_year=year(n)
print("YEAR is:",check_year)

"""with return values and no arguements"""
def year():
    n=int(input("Enter n value:"))
    if n%400==0 or n%4==0 and n%100!=0:
        return "LEAP YEAR";
    else:
        return "NOT LEAP YEAR";
check_year=year()
print("YEAR is:",check_year)


# 7. Check whether a character is alphabet or not
"""with arguements and with return vaues"""
def character(name):
    if (name>='A' and name<='Z') or (name>='a' and name<='z'):
        return "ALPHABET";
    else:
        return "NOT an ALPHABET";
name=input("Enter character:")
check_alphabet=character(name)
print("The Character is:",check_alphabet)

#8. Check whether an alphabet is vowel or consonant
"""with no arguements and with return vaues"""
def character():
    n=input("Enter character:")
    if (n=='a' or n=='e' or n=='i' or n=='o' or n=='u' or n=='A' or n=='E' or n=='I' or n=='O' or n=='U'):
        return "vowe1";
    else:
        return " consonant";
checkchar=character()
print("ALPHABET is :",checkchar)

#9. Check whether a character is alphabet, digit or special character
def check_character(ch):
    if (ch>='A' and ch <= 'Z') or (ch>='a' and ch <= 'z'):
        return "Alphabet";
    elif ch>= '0' and ch <= '9':
        return "Digit";
    else:
        return "Special Character";
ch = input("Enter a character: ")
result = check_character(ch)
print(result)

#10. Check whether a character is uppercase or lowercase alphabet
def character(ch):
    if ch>='A' and ch<='Z':
        return "LOWER CASE";
    elif ch>='a' and ch<='z':
        return "UPPER CASE";
    else:
        return "not an vowel";
ch=input("Enter character:")
check_char=character(ch)
print("The Alphabet is :",chech_char)
        
        
    

