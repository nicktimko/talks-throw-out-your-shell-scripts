.. Throw Out Shell Scripts documentation master file, created by
   sphinx-quickstart on Sun Apr  7 19:31:52 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TOSS: Throw Out (Your) Shell Scripts
================================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    so100
    packages

The Competitors
=========================

Bash: The Language
----------------------

One base type: character strings. Arrays available, but as Unix commands are all about chaining them together with pipes, newline- or null-delimited "arrays" are more common as those can be interpreted by other commands.

Shell strengths: process forking, stream management
Shell weaknesses: types, logic, syntax

If you need to pipe...

Where needed, you can stitch together multiple processes...


PowerShell
-------------------
Has types, interactive help, all-in-all pretty nice. Only available on Windows.


Primary Uses
==================

* Wholesale replacement of scripts. The scripts may be direct shell scripts or Makefiles. Common script usage:
    * Tie together multiple executables
    * Perform a bunch of file/path manipulations

* Wrapping a confusing/awful interface to another program
    * ``os.exec*`` functions if you want to just do something at the start
    * The program may also be ordinarily fine, but say you wanted to run it several times with different parameters, or save a set of parameters as a default.

The standard library packages in Python that can replicate much of the basic functionality that shell scripts generally provide are the ``os``, ``pathlib``, ``shutil``, and ``subprocess`` packages.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
