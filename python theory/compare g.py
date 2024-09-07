import numpy as np
import matplotlib.pyplot as plt
import time

# Method 1: O(n^2) approach
def compute_averages_n2(X):
    n = len(X)
    A = np.zeros(n)
    for i in range(n):
        A[i] = np.mean(X[:i+1])
    return A

# Method 2: O(n) approach
def compute_averages_n(X):
    n = len(X)
    A = np.zeros(n)
    running_sum = 0
    for i in range(n):
        running_sum += X[i]
        A[i] = running_sum / (i + 1)
    return A

# Function to measure execution times and plot results
def measure_and_plot():
    sizes = np.arange(100, 2100, 100)  # Array sizes from 100 to 2000
    times_n2 = []
    times_n = []

    for size in sizes:
        X = np.random.rand(size)
        
        # Measure time for O(n^2) method
        start_time = time.time()
        compute_averages_n2(X)
        times_n2.append(time.time() - start_time)
        
        # Measure time for O(n) method
        start_time = time.time()
        compute_averages_n(X)
        times_n.append(time.time() - start_time)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_n2, label='O(n^2) method')
    plt.plot(sizes, times_n, label='O(n) method')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Time Complexity Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the measurement and plot function
measure_and_plot()
