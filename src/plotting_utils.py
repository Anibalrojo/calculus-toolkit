import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_function_and_derivative(f_expr, df_expr, critical_points, x_left, x_right):
    """
    Plots the function f(x) and its derivative f'(x).
    Highlights the critical point on both graphs.

    Args:
        f_expr (sympy.Expr): The function f(x).
        df_expr (sympy.Expr): The derivative f'(x).
        critical_points (list): Critical points where f'(x) = 0.
        x_left (float): The left boundary of the interval.
        x_right (float): The right boundary of the interval.

    """
    # Convert symbolic expressions to numerical functions
    f_num = sp.lambdify(sp.Symbol('x'), f_expr, 'numpy')
    df_num = sp.lambdify(sp.Symbol('x'), df_expr, 'numpy')

    # Define the range of values
    x_vals = np.linspace(x_left, x_right, 400)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    # Create the plot
    plt.figure(figsize=(12, 5))

    # Plot f(x)
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.scatter(critical_points[0], f_num(critical_points[0]), color='red', zorder=5, label='Critical Point (Minimum)')
    plt.axvline(critical_points[0], linestyle='--', color='gray')
    plt.title('Function f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()

    # Plot f'(x)
    plt.subplot(1, 2, 2)
    plt.plot(x_vals, dy_vals, label="f'(x)", color='green')
    plt.axhline(0, linestyle='--', color='black')
    plt.scatter(critical_points[0], df_num(critical_points[0]), color='red', zorder=5, label="f'(x) = 0")
    plt.axvline(critical_points[0], linestyle='--', color='gray')
    plt.title("Derivative f'(x)")
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_3d_surface_and_contour(g_expr, critical_points):
    """
    Plots the 3D surface and a contour map for a two-variable function g(x, y).
    Highlights the critical point on both graphs.

    Args:
        g_expr (sympy.Expr): The symbolic expression of the function g(x, y).
        critical_points (dict): A dictionary with the critical points.
    """
    # Convert the symbolic function to a numerical one
    g_num = sp.lambdify((sp.symbols('x y')), g_expr, 'numpy')

    # Generate the grid of points
    x_vals = np.linspace(-5, 5, 100)
    y_vals = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Evaluate the function g on the grid
    Z = g_num(X, Y)

    # Extract critical points
    x, y = sp.symbols('x y')
    x0, y0 = float(critical_points[x]), float(critical_points[y])

    # Critical point value
    z0 = g_num(x0, y0)

    # 3D Surface
    fig = plt.figure(figsize=(14, 6))
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
    ax1.scatter(x0, y0, z0, color='red', s=50, label='Critical Point')
    ax1.set_title('3D Surface of g(x, y)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('g(x, y)')
    ax1.legend()

    # Contour Map
    ax2 = fig.add_subplot(1, 2, 2)
    contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
    ax2.scatter(x0, y0, color='red', label='Critical Point')
    ax2.set_title('Contour Map of g(x, y)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    plt.colorbar(contour)
    plt.tight_layout()
    plt.show()
