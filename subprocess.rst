=================================
Subprocesses and ``subprocess``
=================================

The :py:mod:`subprocess` module in Python is the standard library module that allows you to create, control, and interact with other processes. The generic helper call is :py:func:`subprocess.run`, which will block until the process is complete. There is a wide suite of keyword arguments that can also be provided

The central primitive is :py:class:`subprocess.Popen` which when instantiated will launch the process and it can then be manipulated in parallel.
