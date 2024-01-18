# contents of noxfile.py
import nox

# Create Test Session; The Test Session would create a temporary virtual environment
@nox.session
def tests(session):
    session.install("numpy", "pytest") # pip install numpy and pytest
    session.install(".") # Install Our Package: pip install .
    session.run("pytest") # Would automatically go to tests folder to run python file for test