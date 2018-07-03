#Here we will create some cooler graphs like a 3D scatter plot. Again we need pandas and matplotlib but also the Axes3D object from the mpl_toolkits library. If you don't have this lirbary install it by using pip install mpl_toolkits'
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#lets read in the table for this plot and then look at it
df = pd.read_csv("./hour.csv")
print df

#Here we start a new figure and pass it to the variable fig
fig = plt.figure()

#This figure is then passed to our Axes3d object to make it a three dimensional plot
ax = Axes3D(fig)

plt.cla()

#From the spreadsheet we now take three different columns to use as x, y and z
x = df.temp
y = df.atemp
z = df.hum

#now we create the scatterplot using our x y and z. The plot is then coloured by the values for y
sc = ax.scatter(x,y,z,  c=y)


#Here we set the labels for the axes and give the plot a title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("3D Plot")

#Now lets look at the plot. In the interactive view we can also turn around the plot using the mouse
plt.show()

