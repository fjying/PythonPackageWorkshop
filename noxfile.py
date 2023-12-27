# contents of noxfile.py
import nox

@nox.session
def tests(session):
    session.install("numpy", "pytest") # Create temporary virtual environment to run test
    session.install(".") # install package of home directory
    session.run("pytest")