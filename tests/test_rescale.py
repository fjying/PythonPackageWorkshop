import numpy as np
from package.rescale import rescale


def test_rescale():
    np.testing.assert_allclose(
        rescale(np.linspace(0, 100, 5)),
        np.array([0.0, 0.25, 0.5, 0.75, 1.0]),
    )

