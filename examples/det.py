import scipy
import xnumpy as np
from xnumpy import xf64


def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    # Converts N into a list of tuples of columns
    tuple_N = list(zip(*N))

    # Nested list comprehension to calculate matrix multiplication
    return [
            [
                sum(el_m * el_n for el_m, el_n in zip(row_m, col_n))
                for col_n in tuple_N
        ] for row_m in M
    ]


def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values
    id_mat = [[xf64(i == j) for i in range(m)] for j in range(m)]

    # Rearrange the identity matrix such that the largest element of
    # each column of M is placed on the diagonal of of M
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(float(M[i][j])))
        if j != row:
            # Swap the rows
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U
    L = [[xf64(0.0) for __ in range(n)] for _ in range(n)]
    U = [[xf64(0.0) for __ in range(n)] for _ in range(n)]

    # Create the pivot matrix P and the multipled matrix PA
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)

    # Perform the LU Decomposition
    for j in range(n):
        # All diagonal entries of L are set to unity
        L[j][j] = xf64(1.0)

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = \
                    (PA[i][j] - s2) \
                    / U[j][j]

    return (P, L, U)


def sgn(P):
    s = 0
    for i in range(len(P)):
        for j in range(i):
            if float(P[i][j]) > 0.0 and i + j % 2 != 0:
                s += 1
    if s % 2 == 0:
        return 1
    else:
        return -1


def main():
    A = np.numpy.array([
            [ 3 + 1e-3, 3,       -1 + 1e-4,  1],
            [ 3,        3,        1 + 1e-4, -1],
            [-1,        1 + 3e-2, 2 + 1e-4, -2 - 1e-3],
            [-1 - 1e-3, 1,       -2 + 1e-4,  2 - 1e-3],
        ])

    print("Input array:")
    print(A)

    P, L, U = scipy.linalg.lu(A)

    det1 = np.prod(np.diag(U)).item()

    P, L, U = lu_decomposition(A)
    

    det2 = 1
    for i in range(4):
        det2 *= U[i][i]
    det2 *= sgn(P)
    print("Det with numpy.linalg.det")
    print(np.linalg.det(A))
    print("Det with scipy.lu matrix decomposition")
    print(det1)
    print("Det with hand-made lu with float64")
    print(float(det2))
    print("Det with hand-made lu with xf64")
    print(det2)


if __name__ == '__main__':
    main()

