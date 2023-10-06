import matplotlib.pyplot as plt

Delta_t = 0.03  # Delta est condidéré comme petit

N = 400

t = [i * Delta_t for i in range(N)]
C = [0.0] * N

# Données de l'énoncé :
C[0] = 1.000
k = 0.464

for i in range(N-1):
    C[i+1] = C[i] - (t[i+1] - t[i]) * k * C[i]  # Nouvelle concentration = concentration * (1 - delta_t * k)

plt.plot(t, C)
plt.xlabel("Temps (h)")
plt.ylabel("Concentration molaire  du réactif (mol/L)")
plt.show()

t_mes = [i/2 for i in range(11)] + [6, 8, 10]
C_mes = [1.000, 0.789, 0.623, 0.499, 0.394, 0.310, 0.249, 0.197, 0.155, 0.124, 0.098, 0.0618, 0.0245, 0.0095]
plt.plot(t_mes, C_mes, "+", markersize=12)
plt.xlabel("Temps (h)")
plt.ylabel("Concentration molaire  du réactif (mol/L)")
plt.show()


plt.plot(t, C)
plt.plot(t_mes, C_mes, "+", markersize=12)
plt.xlabel("Temps (h)")
plt.ylabel("Concentration molaire  du réactif (mol/L)")
plt.show()
