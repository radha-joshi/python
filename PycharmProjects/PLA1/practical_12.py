#line graph
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#bar graph
import matplotlib.pyplot as plt
x = ['A', 'B', 'C', 'D']
y = [5, 7, 3, 8]
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
#scatter plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [12, 18, 25, 30, 22]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#histogram
import matplotlib.pyplot as plt
data = [10, 20, 20, 30, 30, 30, 40, 50]
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
#pie chart
import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]
plt.pie(sizes, labels=labels)
plt.title("Pie Chart")
plt.show()