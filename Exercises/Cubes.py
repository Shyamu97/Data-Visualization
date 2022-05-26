import matplotlib.pyplot as plt

number = range(1,5001)
number_cube = [x**3 for x in number]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(number, number_cube,c=number_cube, cmap=plt.cm.Blues, linewidth=3)

# Set chart title and label axex.

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Number", fontsize=14)

# Set size of tick labels.

ax.tick_params(axis='both', which='major', labelsize=20)

plt.show()
