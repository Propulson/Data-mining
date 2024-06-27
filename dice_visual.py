from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create 2 cubes
die1 = Die()
die2 = Die()

# mode some trying
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyze
frequencies = []
max_result = die1.sides + die2.sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#view results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='My Results', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename='d6.html')

print(frequencies)
