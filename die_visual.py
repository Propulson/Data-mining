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

print(frequencies)

