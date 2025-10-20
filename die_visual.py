from die import Die
import plotly.express as px

# create a D6
die_1 = Die()
die_2 = Die(10)

#make rolls and store in a list 
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequency = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    freq = results.count(value)
    frequency.append(freq)

# visualize the results
fig = px.bar(x=poss_results, y=frequency)
fig.update_layout(xaxis_dtick=1)
fig.show()