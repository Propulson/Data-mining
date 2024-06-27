from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create 2 cubes
die1 = Die()
die2 = Die()
die3 = Die()
# mode some trying
results = [die1.roll() + die2.roll() + die3.roll() for roll_num in range(1000)]

#analyze
max_result = die1.sides + die2.sides + die3.sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]
#view results
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='My Results', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename='d6.html')

print(frequencies)
