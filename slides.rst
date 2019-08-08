=====================
Slide Outline
=====================


The Problem
=====================

1. Shells have extremely limited types (strings are the only widely supported type)
1. Shells excel at common, but a narrow set of tasks.
1. Syntax is tricky
1. Shells are inconsistent across platforms.
    * Most full-featured Linux distros have Bash 4.x
    * macOS 10.14 and earlier has Bash 3.x.
    * macOS 10.15 has ``zsh``
    * Minimal distros (e.g. Alpine) will only have ``sh``


The Solution
=====================

When developing a Python app, you'll have Python: use it! Python will not be as succinct as your typical Shell script, but will be infinitely more manageable.

Process I/O Crash-course
-------------------------------

Input to one-off processes commonly include:

1. Arguments ``sys.argv``
2. Standard Input (File Descriptor 0) ``input()``
3. The Working Directory ``os.getcwd()``
4. Environment variables ``os.environ``
5. Files (specified via argument or in a predefined location) ``open(...)``

Output comes in the form of:

1. Standard Output (File Descriptor 1) ``print()``
2. Standard Error (File Descriptor 2) ``print(..., file=sys.stderr)``
3. An exit code (an integer from 0 to 255) ``sys.exit(n)``
4. Files ``open(...)``

Long-lived services will often use sockets or other inter-process communication (IPC) methods; we won't cover that here.


Lets Build: A Toolchain
--------------------------

1. Find and control the Python of your choice
2. Execute `python -m venv` (PATH must be set correctly)
3. Execute `pip install -r requirements.txt` (PATH *and* working directory must be set correctly)
4. Execute `pylint target.py` (PATH, WD, exit codes)


Full-Cloth solutions
=====================

1.


Summary
=====================
