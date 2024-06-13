import pandas as pd
import numpy as np

# Load the tidal data
df = pd.read_csv('tidal_data.csv')

# Define the threshold for tidal transition (e.g., 0.5 meters)
transition_threshold = 0.5

# Calculate the differences in tidal heights
df['Height_diff'] = df['Height (m)'].diff()

# Identify tidal transitions
df['Transition'] = np.where((df['Height_diff'] > transition_threshold) | (df['Height_diff'] < -transition_threshold), 1, 0)

# Label the transitions (1: high to low, -1: low to high)
df['Transition_type'] = np.where(df['Height_diff'] > transition_threshold, -1, 1)

# Print the results
print(df.head())