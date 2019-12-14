import numpy as np

import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)

#applying cos on the x
y = np.cos(x)

plt.plot(x,y)

plt.show()

print("ok plotted")

# comparison and plots

y1= x*3 #linear

y2 = np.log(y1) #log

plt.plot(x,y1)
plt.plot(x,y2)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title('Linear Vs. Log')

plt.legend(['Linear', 'Log'])

plt.show()

#insert images into plots
# import imageio
#
# img = imageio.imread("some_path")
#
# plt.imshow(img)
# plt.show()
