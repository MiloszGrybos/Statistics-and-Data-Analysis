# Task 33 - Power of a Two-Sided Z-Test

This folder contains a simulation and visualization script that compares **empirical** and **theoretical** power of a two-sided Z-test for the population mean.

## File

- `main.py` - runs Monte Carlo simulations, computes theoretical power, and generates plots.

## What the script does

1. Simulates samples from a normal distribution with parameters `(mu, sigma)`.
2. Performs a two-sided Z-test of:
   - `H0: mu = 200`
   - `H1: mu != 200`
3. Estimates empirical power from repeated simulations (`1000` repetitions).
4. Computes theoretical power using the normal CDF.
5. Plots:
   - empirical vs theoretical power for `n = 36`
   - theoretical power comparison for `n in {9, 36, 100}`

## Requirements

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

## Run

From this directory, run:

```bash
python main.py
```

Two plots will be displayed in separate windows.

## Notes

- The empirical power is random because it is based on simulation.
- Running the script multiple times may produce slightly different empirical curves.
