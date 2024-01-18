import numpy as np
from packageworkshop.rescale import rescale

def test_rescale():
    np.testing.assert_allclose(
        rescale(np.linspace(0, 100, 5)), # Rescales [0.,  25.,  50.,  75., 100.] from 0 to 1.
        np.array([0.0, 0.25, 0.5, 0.75, 1.0]), # Compare the function output with the analytical output to check codes
    )

