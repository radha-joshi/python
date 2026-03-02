#functions in python

print("4 types of python functions.")
#Radha Joshi 122-A

print("no argument no return")

def greet():
    print("hello world!")

greet() #function call

print("with argument no return")

def greet_me(name):
    print("hello", name)

name=input("enter a name:")
greet_me(name) #function call

print("no argument with return")
#Radha Joshi 122-A

def sum():
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    c=a+b
    return (c)

print("sum is =", sum()) #function call

print("with argument with return")

def multiply(a,b):
    mul=a*b
    return (mul)

a=int(input("enter a number:"))
b=int(input("enter another number: "))
print("multiplication is =", multiply(a,b)) #Function call

print("python function to check if number is prime")
#Radha Joshi 122-A

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

check_prime (14)

check_prime(7)

print("python function to get the factorial of a number")
#Radha Joshi 122-A

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact=fact * i
    print("factorial of ", n, " is =", fact)

n=int(input("enter number to get factorial: "))

factorial(n)

print("python function to merge two lists into a tuple")
#Radha Joshi 122-A

def merge_to_tuple(list1, list2):
    combined = list1 + list2
    return tuple(combined)

l1=["a","b","c"]
l2=["d","e","f"]

print("l1=",l1)
print("l2=",l2)

print("merged list=", merge_to_tuple(l1,l2))

print("python function to print student report")
#Radha Joshi 122-A

student = {
    "name": "Rahul",
    "Maths": 80,
    "Science": 75,
    "English": 85
}

def print_report(student_marks):
    total = 0
    for subject in student_marks:
        if subject != "name":
            total += student_marks[subject]

    print("Student Name:", student_marks["name"])
    print("Total Marks:", total)

    if total >= 150:
        print("Final Result: Passed")
    else:
        print("Final Result: Failed")

print_report(student)