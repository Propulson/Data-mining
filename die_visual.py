from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create cube
die = Die()

# mode some trying
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyze
frequencies = []
for value in range(1, die.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#view results
x_values = list(range(1, die.sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='My Results', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename='d6.html')

print(frequencies)
