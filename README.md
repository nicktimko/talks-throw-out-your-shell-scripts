# Throw Out (Your) Shell Scripts

One of the most common secondary languages used by Python developers is some variant of shell script (`sh`, `bash`, `cmd.exe`, or PowerShell). But why torture yourself with poor design decisions from the 70's when you know Python?

This talk will cover how to command and control subprocesses using the standard library `subprocess` module to do everything you can with Bash, and more. Additionally we will look at Invoke and Nox, two task runners that can function like Make, which simplify subprocess execution at the cost of some flexibility.

We will motivate the need with two usecases: wrapping and adding configuration to a 3rd party binary, and weaving together a CI toolchain.

## Slides

* [PyCon Ireland 2019][slides-pyconie19]
* [ChiPy August 2019][slides-chipy]

[slides-chipy]: https://docs.google.com/presentation/d/1v5z4f-FQkS-bQYE-Xv5SvA6cyaTiqlxs2w2CI1yZcAU/edit?usp=sharing
[slides-pyconie19]: https://docs.google.com/presentation/d/1QhityesFQJDCIZAhE0_GRKlwzc3gdoV3N_ev69neucI/edit?usp=sharing

## Revision @ Presentation

* [`9156e4350`](https://github.com/nicktimko/talks-throw-out-your-shell-scripts/commit/9156e4350bdf1e37e07a50b8adb8c756ccc43b2b) - PyCon Ireland 2019 (2019 October 13)
* [`47e4c81ea`](https://github.com/nicktimko/talks-throw-out-your-shell-scripts/commit/47e4c81ea8e5798cc1675bea98187b2a911f0194) - ChiPy August Monthly Meeting (2019 August 8)
