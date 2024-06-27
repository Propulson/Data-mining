import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2, color='blue')
# diagram's name and x and y
ax.set_title('Squares, Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.tick_params(axis='both', labelsize=14)


plt.plot()
