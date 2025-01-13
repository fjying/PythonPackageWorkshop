[![DOI](https://zenodo.org/badge/736356201.svg)](https://zenodo.org/doi/10.5281/zenodo.10436874)

## How to Package and Publish Your Python Codes #
This workshop gives the overview of how to prepare all the documentation and codes to package and publish your python codes.

## Create and Activate New Package Environment to Manage Packages 
### Choose either Conda Environment or Python Environment
### Conda Envirionment
```
conda create -n pythonpackageworkshop python=3.9
conda activate pythonpackageworkshop
```

### Python Environment
```
mkdir ~/packageenvs
cd ~/packageenvs
python -m venv pythonpackageworkshop
source pythonpackageworkshop/bin/activate
```

## Change Directory to the Repo Folder #
Change directory to the folder of the repo `PythonPackageWorkshop`
```
cd <.../PythonPackageWorkshop>
```

## Install Package named `packageworkshop` and its dependencies
```
pip install -e .
```

## Usage
```python
import numpy as np
from packageworkshop.rescale import rescale

# rescales over 0 to 1
rescale(np.linspace(0, 100, 5))
```

## License
[![License](https://img.shields.io/badge/license-BSD-green.svg)](https://opensource.org/licenses/BSD-3-Clause)
