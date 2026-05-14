# Hypersphere Volume Analysis

## Overview
This program compares the volume of a unit hypersphere (radius 1) computed using an analytical formula with estimates obtained through Monte Carlo simulation, across different dimensions.

## How it works

### Analytical Formula
The exact volume of a unit hypersphere in d-dimensional space is given by:

$$V_d = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)}$$

where $\Gamma$ is the Gamma function.

### Monte Carlo Method
To estimate the volume:
1. Generate N random points uniformly distributed in a d-dimensional cube with side length 2 (range [-1, 1])
2. Count how many points fall inside the hypersphere (distance ≤ 1 from origin)
3. The fraction of points inside multiplied by the cube's volume (2^d) gives an estimate of the hypersphere volume

## Results
The program:
- Computes exact volumes for dimensions 1 through 20 using the analytical formula
- Estimates volumes using 10,000 Monte Carlo samples per dimension
- Plots both results on a logarithmic scale for visualization

The logarithmic scale reveals the curse of dimensionality: as dimensions increase, the volume of the hypersphere becomes a smaller and smaller fraction of the enclosing hypercube.
