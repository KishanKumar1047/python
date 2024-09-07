import time
import matplotlib.pyplot as plt
import numpy as np

def average_n2(X):
    n = len(X)
    A = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += X[j]
        A[i] = total / (i + 1)
    return A

def average_n(X):
    n = len(X)
    A = [0] * n
    total = 0
    for i in range(n):
        total += X[i]
        A[i] = total / (i + 1)
    return A

def measure_time(func, X):
    start_time = time.time()
    func(X)
    end_time = time.time()
    return end_time - start_time

def main():
    ns = [100, 200, 400, 800, 1600, 3200, 6400]
    times_n2 = []
    times_n = []

    for n in ns:
        X = np.random.rand(n)
        
        time_n2 = measure_time(average_n2, X)
        times_n2.append(time_n2)
        
        time_n = measure_time(average_n, X)
        times_n.append(time_n)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(ns, times_n2, label='O(n²) Method', marker='o')
    plt.plot(ns, times_n, label='O(n) Method', marker='o')
    plt.xlabel('n (Number of elements)')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Time Complexities')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
