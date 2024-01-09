[![DOI](https://zenodo.org/badge/736356201.svg)](https://zenodo.org/doi/10.5281/zenodo.10436874)

## How to Package and Publish Your Python Codes #
This workshop gives the overview of how to prepare all the documentation and codes to package and publish your python codes.


## Install Packages to Run Workshop Codes #
Change directory to the folder of the repo named `PythonPackageWorkshop`
```
cd <.../PythonPackageWorkshop>
```

Install Package named `package`
```
pip install -e .
```

## Usage

```python
import numpy as np
from package.rescale import rescale

# rescales over 0 to 1
rescale(np.linspace(0, 100, 5))
```

## License
[![License](https://img.shields.io/badge/license-BSD-green.svg)](https://opensource.org/licenses/BSD-3-Clause)
