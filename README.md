# Throw Out (Your) Shell Scripts

One of the most common secondary languages used by Python developers is some variant of shell script (`sh`, `bash`, `cmd.exe`, or PowerShell). But why torture yourself with poor design decisions from the 70's when you know Python?

This talk will cover how to command and control subprocesses using the standard library `subprocess` module to do everything you can with Bash, and more. Additionally we will look at Invoke and Nox, two task runners that can function like Make, which simplify subprocess execution at the cost of some flexibility.

We will motivate the need with two usecases: wrapping and adding configuration to a 3rd party binary, and weaving together a CI toolchain.


## Revision @ Presentation

* `000000000` - ChiPy August Monthly Meeting (2019 August 8)
