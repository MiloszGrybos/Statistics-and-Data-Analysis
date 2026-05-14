import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

D = list(range(1, 21))
N = 10000
v_exact = []
v_monte_carlo = []

for d in D:
    v_d = (np.pi ** (d / 2)) / gamma(d / 2 + 1)
    v_exact.append(v_d)

    X = np.random.uniform(-1, 1, size=(N, d))

    norm = np.linalg.norm(X, axis=1)
    inside = np.sum(norm <= 1)
    
    v_mc = (inside / N) * (2**d)
    v_monte_carlo.append(v_mc)

plt.figure(figsize=(10, 6))
plt.yscale('log')

plt.plot(D, v_exact, label='Analytical formula', color='blue', linewidth=2)
plt.plot(D, v_monte_carlo, 'o', label='Monte Carlo method', color='red', markersize=4)

plt.xlabel('Dimension (d)')
plt.ylabel('Volume (log scale)')
plt.title('Volume of hypersphere with radius 1 as a function of dimension')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()