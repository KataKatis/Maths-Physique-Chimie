import matplotlib.pyplot as plt

""" Question d """

C = [0.789, 0.623, 0.499, 0.394, 0.310, 0.249, 0.155, 0.124, 0.098, 0.0618, 0.0245]  # Concentration [réactif]
v = [0.332, 0.248, 0.210, 0.168, 0.122, 0.104, 0.062, 0.052, 0.0362, 0.01865, 0.0075]  # Vitesse de disparition du réactif
plt.plot(C, v)

plt.title("Vitesse de disparition du réactif en fonction de [réactif]", fontsize=25)
plt.xlabel("[réactif] (mol/L)", fontsize=25)
plt.ylabel("Vitesse de disparition du réactif (mol/L/h)", fontsize=25)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

plt.show()
