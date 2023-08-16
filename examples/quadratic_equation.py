"""
Example shows solutions of quadratic equation by formula and in a better way.
Calculation of exact bits shows which way is better.
"""
import decimal
import xnumpy as np


def solve_quadratic_equation(__a, __b, __c):
    """Solution by a formula with discriminant"""
    __d = __b * __b - 4 * __a * __c
    sqrt_of_d = __d.sqrt()
    root1 = (-__b + sqrt_of_d) / (2 * __a)
    root2 = (-__b - sqrt_of_d) / (2 * __a)
    if root1 > root2:
        root1, root2 = root2, root1
    return root1, root2


def smart_solve_quadratic_equation(__a, __b, __c):
    """More exact solution"""
    __d = __b * __b - 4 * __a * __c
    sqrt_of_d = __d.sqrt()
    root1 = (-__b + (sqrt_of_d if float(__b) < 0 else -sqrt_of_d)) / (2 * __a)
    root2 = __c / __a / root1
    if root1 > root2:
        root1, root2 = root2, root1
    return root1, root2


def main():
    __a = np.xf64(1.0)
    __b = np.xf64(1_000.0)
    __c = np.xf64(-0.000_000_000_02)
    x1_ff64_v1, x2_ff64_v1 = solve_quadratic_equation(__a, __b, __c)
    x1_ff64_v2, x2_ff64_v2 = smart_solve_quadratic_equation(__a, __b, __c)

    n_digits = 18
    decimal.getcontext().prec = n_digits
    a_d = decimal.Decimal(1.0)
    b_d = decimal.Decimal(1000.0)
    c_d = decimal.Decimal(-0.000_000_000_02)
    #x1_dec_v1, x2_dec_v1 = solve_quadratic_equation(a_d, b_d, c_d)
    #x1_dec_v2, x2_dec_v2 = smart_solve_quadratic_equation(a_d, b_d, c_d)
    n_digits = 18
    decimal.getcontext().prec = n_digits
    a_d = decimal.Decimal(1.0)
    b_d = decimal.Decimal(1000.0)
    c_d = decimal.Decimal(-0.000_000_000_02)
    #x1_dec_v1, x2_dec_v1 = solve_quadratic_equation(a_d, b_d, c_d)
    #x1_dec_v2, x2_dec_v2 = smart_solve_quadratic_equation(a_d, b_d, c_d)

    print(
        'Quadratic equation\n'
        f'{__a}*x^2 + {__b}*x + {__c} == 0\n\n'
        'Solution with xf64:\n'
        f'1st method: {x1_ff64_v1}, {x2_ff64_v1}\n'
        f'2nd method: {x1_ff64_v2}, {x2_ff64_v2}\n'
        '\n'
        '1st method\n'
        'x_1\n'
        f'float64: {float(x1_ff64_v1):.12f} {float(x1_ff64_v1):.15e}\n'
        f'xf64:  {x1_ff64_v1:.12f} {x1_ff64_v1:.15e}\n'
        'x_2\n'
        f'float64: {float(x2_ff64_v1):+.15f} {float(x2_ff64_v1):+.15e}\n'
        f'xf64:  {x2_ff64_v1:+.15f} {x2_ff64_v1:+.15e}\n'
        '2nd method\n'
        'x_1\n'
        f'float64: {float(x1_ff64_v2):.12f} {float(x1_ff64_v2):.15e}\n'
        f'xf64:  {x1_ff64_v2:.12f} {x1_ff64_v2:.15e}\n'
        'x_2\n'
        f'float64: {float(x2_ff64_v2):+.15f} {float(x2_ff64_v2):+.15e}\n'
        f'xf64:  {x2_ff64_v2:+.15f} {x2_ff64_v2:+.15e}\n'
    )

if __name__ == '__main__':
    main()

