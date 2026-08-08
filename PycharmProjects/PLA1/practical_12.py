#graphs in python

#Radha Joshi [122-A]
#line graph
import matplotlib.pyplot as plt
x = ["Pencil", "Eraser", "Scale", "Scissors", "Notebook"]
y = [10, 10, 20, 40, 50]
plt.plot(x, y)
plt.title("Stationary Price Distribution")
plt.xlabel("Stationary")
plt.ylabel("Prices")
plt.show()

#Radha Joshi [122-A]
#bar graph
import matplotlib.pyplot as plt
x = ['Math', 'Science', 'English', 'Geography']
y = [60, 70, 50, 90]
plt.bar(x, y)
plt.title("Academic Performance of Student")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

#Radha Joshi [122-A]
#scatter plot
import matplotlib.pyplot as plt
x = ["Pencil", "Eraser", "Scale", "Scissors", "Notebook"]
y = [10, 10, 20, 40, 50]
plt.scatter(x, y)
plt.title("Stationary Price Distribution")
plt.xlabel("Stationary")
plt.ylabel("Prices")
plt.show()

#Radha Joshi [122-A]
#histogram
import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 30, 30, 40, 50]
plt.hist(data)
plt.title("Data Frequency Distribution")
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.show()

#Radha Joshi [122-A]
#pie chart
import matplotlib.pyplot as plt
Subjects = ['IoT', 'DS', 'OOP', 'CAO']
Proportion = [25, 35, 20, 20]
plt.pie(Proportion, labels=Subjects)
plt.title("Elective Subject Preferences")
plt.show()