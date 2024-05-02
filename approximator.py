import numpy as np
from fft import get_fft, get_ifft, make_audio
from func import MusicFunc
import matplotlib.pyplot as plt

def get_approximation_for_data(data):
    # Collect data points
    data_points = np.arange(len(data))
    g_values = np.array(data)

    # Create the design matrix
    music = MusicFunc()
    input_value = []
    for i in range(music.N):
        val = []
        for x in data_points:
            val.append(music.super_f(i, x))
        input_value.append(val)
    X = np.column_stack(input_value)

    # Solve for coefficients using least squares regression
    coefficients, residuals, _, _ = np.linalg.lstsq(X, g_values, rcond=None)

    # Approximate the target function using the coefficients
    def g_approx(x):
        col_stk = []
        for i in range(music.N):
            col_stk.append(music.super_f(i, x))
        return np.dot(np.column_stack(col_stk), coefficients)

    # Test the approximation
    test_points = np.arange(len(data))
    
    approximated_values = []
    for i in range(len(test_points)):
        approximated_values.append(g_approx(test_points[i]))

    '''
    # Plot the results
    plt.plot(data_points, g_values, 'o', label='Data points')
    plt.plot(test_points, data, label='Actual g(x)')
    plt.plot(test_points, approximated_values, label='Approximated g(x)')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.title('Function Approximation using Least Squares Regression')
    plt.show()
    '''

    return approximated_values










