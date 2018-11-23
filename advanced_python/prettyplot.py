import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6]
CO2_Conc = [250, 265, 272, 260, 300, 320, 389]
Temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

plt.plot(time, CO2_Conc, '--b', label = 'CO2')
plt.plot(time, Temp, '--r', label = 'Temperature')
plt.title("CO2 over time")
plt.xlabel("time")
plt.ylabel("CO2 concentration")
plt.legend()

plt.show()
