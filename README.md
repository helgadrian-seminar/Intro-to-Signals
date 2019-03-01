# Intro-to-Signals

## Outline
- Library docs
- Interrogating timeseries data
- Modeling with synthetic data

## Library docs for this tutorial
- [numpy.fft](https://docs.scipy.org/doc/numpy/reference/routines.fft.html)
- [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [numpy.correlate](https://docs.scipy.org/doc/numpy/reference/generated/numpy.correlate.html)

## A first example
Goals:
- Reinforce I/O and visualization concepts
- Learn how to interrogate a signal using python's scipy and numpy libraries

## Do it on your own
For the three remaining timeseries:
- Read in the signal on your own
- Identify the dominant frequency/period
- Speculate on what type of process produced each signal

Notes:
- Signal two is in nondimensional time
- Each discrete value in signal three is a monthly average
- Signals one and four have notes in a .md file in their directories

Challenges:
- Can you demean signal 3?
- What difference did it make?
- Can you perform an autocorrelation on signal 3?
- Did you learn anything?

## Modeling with Synthetic Data
- Synthetic data generation
- How does this relate to the central limit theorem?
- Application: generate seafloor data
