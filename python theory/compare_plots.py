import pandas as pd
import matplotlib.pyplot as plt

# Read data from the first CSV file
data1 = pd.read_csv('C:\DOCS\Programming\python\python_only\output1.csv')

# Read data from the second CSV file
data2 = pd.read_csv('C:\DOCS\Programming\python\python_only\output2.csv')

# Display the first few rows of each dataframe (optional, for verification)
print("Data from output1.csv:")
print(data1.head())
print("\nData from output2.csv:")
print(data2.head())

# Print the column names to debug the KeyError issue
print("\nColumns in data1:", data1.columns)
print("Columns in data2:", data2.columns)

# Strip any leading/trailing whitespace from column names
data1.columns = data1.columns.str.strip()
data2.columns = data2.columns.str.strip()

# Plotting the data
plt.figure(figsize=(12, 6))

# Plot data from the first CSV file
plt.plot(data1['time'], data1['n'], marker='o', linestyle='-', color='b', label='Output 1')

# Plot data from the second CSV file
plt.plot(data2['time'], data2['n'], marker='x', linestyle='--', color='r', label='Output 2')

# Add titles and labels
plt.title('Comparison of Time vs. Number of Elements')
plt.ylabel('Number of Elements (n)')
plt.xlabel('Time (microseconds)')

# Add a legend to distinguish between the two datasets
plt.legend()

# Add grid for better readability
plt.grid(True)

# Rotate x-axis labels if necessary
plt.xticks(rotation=45)

# Adjust layout to make room for rotated labels
plt.tight_layout()

# Show the plot
plt.show()
