import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)
plt.title("My First Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig('line_graph.png')
plt.show()
