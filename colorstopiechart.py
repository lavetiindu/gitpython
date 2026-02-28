import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["c", "hotpink", "b", "m"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 