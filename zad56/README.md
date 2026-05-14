# Task 14 - Section 3.7 - ISL

## Overview
This script demonstrates multiple linear regression with two correlated predictors and shows how the results change after adding an outlier.

The data are generated from the model:

$$y = 2 + 2x_1 + 0.3x_2 + e$$

where $e$ is random noise.

## What the code does

1. Generates 100 random values of `x1` from a uniform distribution on [0, 1].
2. Generates `x2` so that it is correlated with `x1`.
3. Builds the response variable `y` from the population model above.
4. Computes and prints the correlation between `x1` and `x2`.
5. Fits three regression models:
   - `y ~ x1 + x2`
   - `y ~ x1`
   - `y ~ x2`
6. Adds an outlier and refits the same models to show its effect.
7. Plots the relationship between `x1` and `x2`.

## Interpretation
The script illustrates how correlation between predictors can affect regression estimates and how a single outlier can influence fitted coefficients and model summaries.
