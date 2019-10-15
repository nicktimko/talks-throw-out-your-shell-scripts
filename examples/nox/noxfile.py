import nox


@nox.session
def test(session):
    print("greetings world")
    session.run("echo", "hello!")
    session.run("python", "-V")
    session.run("pip", "list")
