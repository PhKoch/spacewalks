import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'  # The output graph is supposed to be a png file

# load and tidy up data, stored as a Pandas data frame
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

# use the Pandas function to store data in the output csv file
eva_df.to_csv(output_file, index=False)

# prepare data for plotting (process the duration and add it up to cumulative_time column)
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# generate the plot
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')  # creates a scatter plot of date (x axis) and cumulative_time (y axis) with black (k), solid line ('-') and dots (o), 
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()  # change the margins
plt.savefig(graph_file)  # save the figure to the png file
plt.show()  # displays the plot