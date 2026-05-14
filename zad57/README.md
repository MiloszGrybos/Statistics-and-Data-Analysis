# Regression Model Comparison

## Overview
This script uses the Auto dataset to compare several regression models for predicting miles per gallon (`mpg`). It splits the data into training and validation sets, fits multiple models, and compares their generalization performance.

## What the code does

1. Loads `Auto.csv` and drops missing rows.
2. Converts `origin` to a categorical variable.
3. Splits the data into training and validation subsets.
4. Fits four different models:
   - `mpg ~ horsepower`
   - `mpg ~ weight + cylinders + displacement + origin`
   - `mpg ~ weight * horsepower`
   - `mpg ~ log(weight) + horsepower + horsepower^2`
5. Prints adjusted $R^2$ for the richer models.
6. Computes validation MSE for each model.

## Purpose
The goal is to compare model complexity and see whether adding more predictors, interactions, or nonlinear transformations improves prediction quality on unseen data.

## Notes
- Lower validation MSE indicates better generalization.
- Adjusted $R^2$ helps compare models with different numbers of predictors.
