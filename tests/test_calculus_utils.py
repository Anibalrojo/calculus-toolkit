import sympy as sp
import sys
import os

# Add the src directory to the Python path to import calculus_utils
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from calculus_utils import get_critical_points

def test_get_critical_points():
    """
    Tests the get_critical_points function with a simple quadratic.
    """
    # Define a simple function f(x) = (x - 3)^2
    x = sp.Symbol('x')
    f = (x - 3)**2

    # The derivative is f'(x) = 2x - 6
    # The critical point is at x = 3
    expected_df = 2 * x - 6
    expected_critical_point = [3]

    # Calculate using the function
    df, critical_points = get_critical_points(f, x)

    # Assert that the results are correct
    assert df == expected_df
    assert critical_points == expected_critical_point

    print("Test passed!")

if __name__ == "__main__":
    test_get_critical_points()
