# Overfitting Analysis with Polynomial Regression

## Overview
This program demonstrates the phenomenon of overfitting by fitting polynomial regression models of increasing degree to a noisy sinusoidal function and comparing training error with cross-validation error.

## How it works

### Data Generation
- Generate 200 random samples uniformly distributed in [0, 1]
- True underlying function: $y = \sin(2\pi x)$
- Add Gaussian noise with mean 0 and standard deviation 0.3

### Model Pipeline
For each polynomial degree d (1 to 39):
1. Create a polynomial feature expansion (degree d)
2. Fit a linear regression model
3. Evaluate using 5-fold cross-validation
4. Calculate training set error

### Metrics
- **Training MSE (red line)**: Mean squared error on the training data
- **Cross-Validation MSE (blue line)**: Mean squared error estimated via 5-fold cross-validation

## Key Observations

The plot reveals the classic overfitting behavior:
- **Underfitting (low degrees)**: Both training and validation errors are high as the model is too simple
- **Good fit (intermediate degrees)**: Both errors decrease; validation error closely follows training error
- **Overfitting (high degrees)**: Training error continues to decrease while validation error increases, indicating the model memorizes noise in the training data rather than learning the true pattern

The gap between the two curves shows the overfitting effect - a larger gap indicates worse generalization to unseen data.
