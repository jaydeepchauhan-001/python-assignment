import numpy as np
import matplotlib.pyplot as plt

def generate_random_data(size=1000, mean=0, std_dev=1):
    """Generates random data using a normal distribution."""
    data = np.random.normal(loc=mean, scale=std_dev, size=size)
    return data

def calculate_statistics(data):
    """Calculates and prints basic statistics of the data."""
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)

    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

def plot_histogram(data):
    """Plots a histogram of the data."""
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Random Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def main():
    data = generate_random_data()
    calculate_statistics(data)
    plot_histogram(data)

if __name__ == "__main__":
    main()
