import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def run_simulation(scale_val, title):
    rng = np.random.default_rng(1)
    x = rng.normal(loc=0.0, scale=1.0, size=100)
    eps = rng.normal(loc=0.0, scale=scale_val, size=100)
    y = -1 + 0.5 * x + eps

    X_sm = sm.add_constant(x)
    model = sm.OLS(y, X_sm).fit()

    print(model.summary())

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.6, label="Dane zebrane (z szumem)")
    plt.plot(x, -1 + 0.5 * x, color="red", linewidth=2, label="Prawdziwa linia (Y = -1 + 0.5X)")
    plt.plot(x, model.fittedvalues, color="black", linestyle="--", linewidth=2, label="Wyliczona linia (MNK)")

    plt.title(f"Wykres: {title}")
    plt.xlabel("Zmienna X")
    plt.ylabel("Zmienna Y")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    return model

model_original = run_simulation(scale_val=0.5, title="Oryginalny szum")

model_less = run_simulation(scale_val=0.1, title="Mniej szumu")

model_more = run_simulation(scale_val=1.41, title="Więcej szumu")

print("j)")
print("\n--- 1. Model z MAŁĄ ilością szumu ---")
print("Przedziały są najwęższe. Model jest bardzo pewny swoich estymacji.")
print(model_less.conf_int())

print("\n--- 2. Model z ORYGINALNĄ ilością szumu ---")
print("Przedziały są umiarkowane.")
print(model_original.conf_int())

print("\n--- 3. Model z DUŻĄ ilością szumu ---")
print("Przedziały są bardzo szerokie. Szum wprowadza dużą niepewność.")
print(model_more.conf_int())