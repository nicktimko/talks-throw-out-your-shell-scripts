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


Bash: The Language
----------------------

One base type: character strings. Arrays available, but as Unix commands are all about chaining them together with pipes, newline- or null-delimited "arrays" are more common as those can be interpreted by other commands.

Shell strengths: process forking, stream management
Shell weaknesses: types, logic, syntax

If you need to pipe Where needed, you can stitch together multiple


Three Uses:

* Wholesale replacement of scripts
* Wrapping a confusing/awful interface to another program
    * ``os.exec*`` functions if you want to just do something at the start



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
