import enum

from invoke import task


class PyLintExitCode(enum.IntFlag):
    # http://pylint.pycqa.org/en/latest/user_guide/run.html#exit-codes
    FATAL = 1
    ERROR = 2
    WARNING = 4
    REFACTOR = 8
    CONVENTION = 16
    USAGE = 32


@task
def check(c):
    result = c.run("pylint target.py", warn=True)

    die_on_pylint_codes = (
        PyLintExitCode.FATAL | PyLintExitCode.ERROR | PyLintExitCode.USAGE
    )
    if result.exited & die_on_pylint_codes:
        return 1

    c.run("black --check target.py")
