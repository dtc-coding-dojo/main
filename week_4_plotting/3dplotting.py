import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
df = pd.read_csv("./hour.csv")

print df


fig = plt.figure()

plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

x = df.temp
y = df.atemp
z = df.hum


sc = ax.scatter(x,y,z,  c=y, edgecolor='face', cmap = "Spectral")

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


colors = [sc.cmap(sc.norm(i)) for i in range( len(x))]

plt.title("3D Plot")
plt.show()