import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', color='blue', linestyle='--')
plt.title("Line Graph in Jupyter")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()