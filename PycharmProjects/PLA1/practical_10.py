#file handling in python

#writing into file
a= open('readme.txt', 'w')
a.write("hello world, my name is radha joshi. im a 2nd year engineering "
        "student at priyadarshini college of engineering")
a.close()

#reading from file
a=open('readme.txt', 'r')
print(a.read())
a.close()

#counting no of words from file
def count_no_of_words_in_file():
    a=open('readme.txt', 'r')
    data= a.read()
    words=data.split()
    count=len(words)
    a. close()
    return (count)

print("no of words in the file are:", count_no_of_words_in_file())

#Radha Joshi [122-A]
# appending a new line to the existing file
a = open('readme.txt', 'a')
a.write("\nthis file has been appended")
a.close()

a = open('readme.txt', 'r')
print("\nappended file is :")
print(a.read())
a.close()