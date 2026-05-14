# Task 13 - Section 3.7 - ISL

## Overview
This script illustrates ordinary least squares (OLS) regression on simulated data and compares how the amount of noise affects the fitted line and confidence intervals.

The data are generated from the model:

$$y = -1 + 0.5x + \varepsilon$$

where $\varepsilon$ is Gaussian noise with different standard deviations.

## What the code does

1. Generates 100 random values of $x$ from a standard normal distribution.
2. Generates noise with three different scales.
3. Builds the response variable $y$ from the linear model above.
4. Adds a constant term with `sm.add_constant(x)` so the regression can estimate the intercept.
5. Fits an OLS model with `sm.OLS(y, X_sm).fit()`.
6. Prints the regression summary and confidence intervals.
7. Plots the noisy data, the true line, and the fitted OLS line.

## Noise scenarios
- Original noise: `scale_val = 0.5`
- Lower noise: `scale_val = 0.1`
- Higher noise: `scale_val = 1.41`

## Interpretation
Smaller noise leads to tighter confidence intervals and a fitted line that is closer to the true relationship. Larger noise increases uncertainty and makes the estimates less precise.
