import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package
x = np.arange(0, 3 * np.pi, 0.1) # create x array of angels from range 0 to 3*3.14
y = np.sin(x) # create y array of sine values of angles from x array
plt.plot(x, y) # plot grah 
plt.title(" Graphical Representation of sine function")
plt.xlabel("x axis ")
plt.ylabel("y axis ")
plt.show() # show plotted graph
