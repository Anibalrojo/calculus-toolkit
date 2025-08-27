import sympy as sp

def get_critical_points(f_expr, var):
    """
    Calculates the symbolic derivative of a function f(x)
    and solves the equation f'(x) = 0 to find the critical points.

    Args:
        f_expr (sympy.Expr): The symbolic expression of the function.
        var (sympy.Symbol): The variable to differentiate with respect to.

    Returns:
        df (sympy.Expr): The derivative of the function.
        critical_points (list): A list of points where f'(x) = 0.
    """
    # Symbolic derivative
    df = sp.diff(f_expr, var)

    # Solve f'(x) = 0
    critical_points = sp.solve(df, var)

    return df, critical_points
