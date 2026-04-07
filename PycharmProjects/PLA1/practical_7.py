#modules in python

#Radha Joshi [122-A]
import int
import math
import college
import keyword

def area_of_circle(radius):
    area = math.pi * radius**2
    return area

def perimeter_of_circle(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

#Radha Joshi [122-A]
def circumference_of_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Enter the radius:"))
print("area of circle is ", area_of_circle(radius),
      " In and perimeter is ", perimeter_of_circle(radius))

print("The square root of 25 is:", math.sqrt(25))
print("The factorial of 4 is:", math.factorial(4))

#Radha Joshi [122-A]
college.accept_name()
int.accept_int()


print("\nTesting Keyword Module")
# checking if  the follwoing words are Python keywords
word1 = "return"
word2 = "radha"

print("Is '", word1, "' a keyword?", keyword.iskeyword(word1))
print("Is '", word2, "' a keyword?", keyword.iskeyword(word2))