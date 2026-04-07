# object-oriented programming in python

# Radha Joshi [122-A]

print("class student with data members: name, roll number and address")


class Student:

    def read(self):
        self.name = input("Enter name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.address = input("Enter address: ")

    def show(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Address:", self.address)


# Radha Joshi [122-A]
s1 = Student()
s1.read()
s1.show()

print("\nbase class PERSON with attributes: name, contact number. "
      "Inherit class EMPLOYEE with attributes: ID and SALARY. "
      "Also inherit class STUDENT from class PERSON. "
      "Class STUDENT should have attributes: enroll_no, dept.")


# Radha Joshi [122-A]
# base class
class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def display_person(self):
        print("Name:", self.name)
        print("Contact:", self.contact)


# derived class employee
class Employee(Person):
    def __init__(self, name, contact, emp_id, salary):
        super().__init__(name, contact)
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        super().display_person()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Radha Joshi [122-A]
# derived class student
class Student(Person):
    def __init__(self, name, contact, enroll_no, dept):
        super().__init__(name, contact)
        self.enroll_no = enroll_no
        self.dept = dept

    def display_student(self):
        super().display_person()
        print("Enrollment No:", self.enroll_no)
        print("Department:", self.dept)


# Radha Joshi [122-A]
# Creating objects
e1 = Employee("Radha", "9130018365", 101, 50000)
s2 = Student("Mohini", "9850399472", 202,
             "Computer Science")

# Display details
print("\nEmployee Details:")
e1.display_employee()

print("\nStudent Details:")
s2.display_student()