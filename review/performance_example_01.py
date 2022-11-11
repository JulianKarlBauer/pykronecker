import numpy as np
import perfplot
import pykronecker
import pylops

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

# "In the first scenario, the Kronecker product is constructed from two of matrices of size (400 × 400) and (500 × 500)""


def setup_func(n):
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)

    return (a, b, pylops.MatrixMult(a), pylops.MatrixMult(b))


def cast_to_array(a):
    if isinstance(a, np.ndarray):
        return a
    elif isinstance(a, pykronecker.operators.KroneckerProduct):
        return a.to_array()
    elif isinstance(a, pylops.basicoperators.kronecker.Kronecker):
        return a.todense()
    else:
        raise Exception("Unknown type")


def check_func(first, second):
    return np.allclose(cast_to_array(first), cast_to_array(second), atol=1e-2)


perfplot.live(
    setup=setup_func,  # or setup=np.random.rand
    kernels=[
        lambda a, b, a_pylop, b_pylop: np.kron(a, b),
        lambda a, b, a_pylop, b_pylop: pykronecker.KroneckerProduct([a, b]),
        lambda a, b, a_pylop, b_pylop: pylops.Kronecker(a_pylop, b_pylop),
    ],
    labels=["np.kron", "pykronecker", "pylops.Kronecker"],
    # n_range=[2**k for k in range(7)],  # possible up to 7
    # n_range=[10, 30, 50, 70, 90, 110, 120],  # equality check prohibits high n
    n_range=[10, 30, 50, 70, 90, 110, 120, 130, 150],  # possible up to 7
    xlabel="Dimension of square matrices",
    logx=False,
    logy=True,
    #
    # Checks are expensive
    equality_check=None,
    # equality_check=check_func,  # set to None to disable "correctness" assertion
)
