import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

X = np.random.uniform(0, 1, size=(200, 1))
e = np.random.normal(0, 0.3, size=(200, 1))
y = np.sin(2 * np.pi * X) + e

mse_cv = []
mse_train = []
D = list(range(1, 40))

for d in D:
    model = make_pipeline(PolynomialFeatures(d), LinearRegression())
    
    wyniki_cv = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    mse_cv.append(np.mean(-wyniki_cv))
    
    model.fit(X, y)
    y_pred = model.predict(X)
    blad_treningowy = mean_squared_error(y, y_pred)
    mse_train.append(blad_treningowy)

plt.figure(figsize=(10, 6))
plt.plot(D, mse_cv, label='Cross-Validation MSE', color='blue', linewidth=2, marker='o')
plt.plot(D, mse_train, label='Training MSE', color='red', linewidth=2, marker='o')

plt.xlabel('Polynomial Degree (d)')
plt.ylabel('MSE Error')
plt.title('Overfitting Analysis')

plt.ylim(0, 0.5) 
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()