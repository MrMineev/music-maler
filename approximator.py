import numpy as np
from fft import get_fft, get_ifft, make_audio
from func import f1, f2, f3, f4
import matplotlib.pyplot as plt

def get_approximation_for_data(data):
    # Collect data points
    data_points = np.arange(len(data))
    g_values = np.array(data)

    # Create the design matrix
    X = np.column_stack([f1(data_points), f2(data_points), f3(data_points), f4(data_points)])

    # Solve for coefficients using least squares regression
    coefficients, residuals, _, _ = np.linalg.lstsq(X, g_values, rcond=None)

    # Approximate the target function using the coefficients
    def g_approx(x):
        return np.dot(np.column_stack([f1(x), f2(x), f3(x), f4(x)]), coefficients)

    # Test the approximation
    test_points = np.arange(len(data))
    approximated_values = g_approx(test_points)

    # Plot the results
    plt.plot(data_points, g_values, 'o', label='Data points')
    plt.plot(test_points, data, label='Actual g(x)')
    plt.plot(test_points, approximated_values, label='Approximated g(x)')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.title('Function Approximation using Least Squares Regression')
    plt.show()

    return approximated_values










