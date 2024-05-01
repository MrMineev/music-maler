import numpy as np
import matplotlib.pyplot as plt

# Define your basis functions
def f1(x):
    # Define the first basis function
    return np.sin(x)

def f2(x):
    # Define the second basis function
    return np.cos(x)

def get_approximation_for_data(data):
    # Collect data points
    data_points = np.arange(len(data))
    g_values = np.array(data)

    # Create the design matrix
    X = np.column_stack([f1(data_points), f2(data_points)])

    # Solve for coefficients using least squares regression
    coefficients, residuals, _, _ = np.linalg.lstsq(X, g_values, rcond=None)

    # Approximate the target function using the coefficients
    def g_approx(x):
        return np.dot(np.column_stack([f1(x), f2(x)]), coefficients)

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

data = []
with open('data.txt', 'r') as f: # loading data from recording from file "data.txt"
    text = f.readlines() # reading all the lines
    mas = text[0].split('|') # spliting all the text for each element of mas to be one number matching to the pressure at that time
    for i in range(len(mas) - 1):
        st = mas[i][1:-1] # deleting simbol '[' and simbol ']'
        data.append(float(st)) # saving data
    f.close() # closing 'data.txt'

approximated_values = get_approximation_for_data(data)
