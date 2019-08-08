from invoke import task


@task
def check(c):
    c.run("pylint target.py")
    c.run("black --check target.py")
