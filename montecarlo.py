# Monte Carlo Simulation pour le prix d'une option européenne
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
S0 = 100       # Prix initial
K = 105        # Strike
T = 1          # Maturité
r = 0.05       # Taux sans risque
sigma = 0.2    # Volatilité
n_simulations = 100000

# Simulation Monte Carlo
np.random.seed(42)
Z = np.random.standard_normal(n_simulations)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# Payoff call européen
payoff = np.maximum(ST - K, 0)

# Prix actualisé
C0 = np.exp(-r * T) * np.mean(payoff)
print(f"Prix de l'option call (Monte Carlo) : {C0:.2f}")

# Histogramme
plt.hist(ST, bins=50, alpha=0.6, color='blue', label='Prix final simulé')
plt.axvline(K, color='red', linestyle='--', label='Strike')
plt.title("Distribution des prix simulés à maturité")
plt.xlabel("Prix de l'action")
plt.ylabel("Fréquence")
plt.legend()
plt.show()
