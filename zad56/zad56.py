import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
x1 = rng.uniform(0, 1, size=100)
x2 = 0.5 * x1 + rng.normal(size=100) / 10
y = 2 + 2 * x1 + 0.3 * x2 + rng.normal(size=100)

print("PART (a): TRUE POPULATION MODEL")
print("Y = 2 + 2*x1 + 0.3*x2 + e")
print("beta_0= 2")
print("beta_1  = 2")
print("beta_2  = 0.3")

print("PART (b): CORRELATION & PLOT")
correlation = np.corrcoef(x1, x2)[0, 1]
print(f"Correlation between x1 and x2: {correlation:.4f}")

plt.figure(figsize=(8, 5))
plt.scatter(x1, x2, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title(f"Part (b): Relationship between x1 and x2 (Correlation: {correlation:.2f})")
plt.grid(True, alpha=0.3)
plt.show()

print("PART (c): MULTIPLE REGRESSION (Y ~ x1 + x2)")
X_c = sm.add_constant(np.column_stack((x1, x2)))
model_c = sm.OLS(y, X_c).fit()
print(model_c.summary())

print("PART (d): SIMPLE REGRESSION (Y ~ x1)")
X_d = sm.add_constant(x1)
model_d = sm.OLS(y, X_d).fit()
print(model_d.summary())

print("PART (e): SIMPLE REGRESSION (Y ~ x2)")
X_e = sm.add_constant(x2)
model_e = sm.OLS(y, X_e).fit()
print(model_e.summary())

x1_new = np.concatenate([x1, [0.1]])
x2_new = np.concatenate([x2, [0.8]])
y_new = np.concatenate([y, [6]])

print("\n--- Refitted Model (c): Multiple Regression with Outlier ---")
X_c_new = sm.add_constant(np.column_stack((x1_new, x2_new)))
model_c_new = sm.OLS(y_new, X_c_new).fit()
print(model_c_new.summary())

print("\n--- Refitted Model (d): Simple Regression (x1) with Outlier ---")
X_d_new = sm.add_constant(x1_new)
model_d_new = sm.OLS(y_new, X_d_new).fit()
print(model_d_new.summary())

print("\n--- Refitted Model (e): Simple Regression (x2) with Outlier ---")
X_e_new = sm.add_constant(x2_new)
model_e_new = sm.OLS(y_new, X_e_new).fit()
print(model_e_new.summary())
