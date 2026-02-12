#functions in python
def greet(): #no argument no return 1 usage
    print("hello world!")

greet #function call

def greet_me(name): #with argument no return 1usage
    print("hello", name)

name=input("enter a name:")
greet_me(name) #function call

def sum(): #no argument with returnTusage a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    c=a+b
    return (c)

print("sum is =", sum()) #function call

def multiply(a,b): #with argument with return usage mul=a*b
    mul=a*b
    return (mul)

a=int(input("enter a number:"))
b=int(input("enter another number: "))

print("multiplication is =", multiply(a,b)) #Function call

def check_prime(num):
    if num>1:
        for i in range(2, num):
            if (num % i) ==0:
                print (num,"is not prime")
                break;
    else:
        print(num, "is not prime")

check_prime (14)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact=fact * i
    print("factorial of ", n, " is =", fact)

n=int(input("enter number to get factorial: "))
factorial(n)