import matplotlib.pyplot as plt

number = [1,2,3,4,5]
number_cube = [1,8,27,64,125]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(number, number_cube, linewidth=3)

# Set chart title and label axex.

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Number", fontsize=14)

# Set size of tick labels.

ax.tick_params(axis='both', which='major', labelsize=20)

plt.show()
