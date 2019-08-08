from invoke import task


SOURCE_DIR = "."
BUILD_DIR = "_build"


@task
def html(c, live=False):
    if not live:
        c.run(f"sphinx-build -M html {SOURCE_DIR} {BUILD_DIR}")
    else:
        c.run(
            "sphinx-autobuild "
            "--port 9876 "
            '--ignore ".git/*" '
            "-b html "
            f"{SOURCE_DIR} "
            f"{BUILD_DIR}/html"
        )


@task
def update(c):
    pass
