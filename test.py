from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt
from fourier import apply_fourier_x
from transformations import Accel

# Interval between two accelerations in seconds
frequency = 0.25

# Quantity of accelerations to get before doing fourier
data_quantity = 1000

# Values after Fourier
fourier_values = []


# Plot fourier of segment of data
def plot_fourier():
    global fourier_values, frequency

    # Number of sample points
    N = data_quantity

    # sample spacing
    T = 1.0 / frequency

    # returns evenly spaced numbers from 0 to N, with N*T increments
    x = np.linspace(0.0, N * T, N)

    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    print(y)
    yf = fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

    plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
    plt.grid()


def test_fourier_functions():
    y = np.array([])
    i = 1
    while i <= 1000:
        np.append(y, np.array([Accel(np.random.random_sample(), 0, 0)]))
        i = i + 1

    print(y)
    yf = apply_fourier_x(y)
    print(yf)


# Start the thread and the plotters
def main():
    #plot_fourier()
    #plt.show()
    #test_fourier_functions()
    array = [Accel(np.random.random_sample(), 0, 0), Accel(np.random.random_sample(), 0, 0), Accel(np.random.random_sample(), 0, 0)]
    x_values = map(lambda y: y.x, array)
    print(x_values)

main()