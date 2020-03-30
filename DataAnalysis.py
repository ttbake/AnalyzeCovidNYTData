import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in data from csv files
us_counties_input_file = 'us-counties.csv'
us_states_input_file = 'us-states.csv'
us_states_codes = 'us_states_codes.csv'

us_counties_data = pd.read_csv(us_counties_input_file)
us_states_data = pd.read_csv(us_states_input_file)
us_states = pd.read_csv(us_states_codes)

# Merge us states data with csv file to join data with state codes
us_states_data_with_codes = pd.merge(us_states_data, us_states, on='state', how='left').dropna(how='all')

# Filter to most recent date of data
recent_day_us_states_data_with_codes = us_states_data_with_codes[us_states_data_with_codes.date == '2020-03-27']

print(recent_day_us_states_data_with_codes.date.unique())

# Start with just analyzing the US states
us_states = recent_day_us_states_data_with_codes["Code"].dropna(how='all')
covid_cases = recent_day_us_states_data_with_codes["cases"].dropna(how='all')
covid_deaths = recent_day_us_states_data_with_codes["deaths"].dropna(how='all')

x = []
y = []

x = list(us_states)
y = list(covid_deaths)

print(x)
print(y)
states_unique = us_states.unique()
deaths_unique = covid_deaths.unique()

# Plot bar chart of deaths by state
plt.bar(x, y)

plt.xlabel('US States')
plt.ylabel('Total COVID Deaths')
plt.title('Data')
plt.show()