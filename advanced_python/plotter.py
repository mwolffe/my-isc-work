import matplotlib.pyplot as plt

#single line plot
#plt.plot([1,2,3,4])
#plt.show()

#double line plot
times = [0, 0.25, 0.5, 0.75]
plt.plot(times, [1,2,3,4])
plt.plot(times, [0,0.5,1,1.2], 'g--',  times, [1,2,3,4], 'r') #g-- green dashed
plt.show()
