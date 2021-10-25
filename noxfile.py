import nox@nox.session(python=["3.7", "3.8"])
def lint(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")@nox.session
