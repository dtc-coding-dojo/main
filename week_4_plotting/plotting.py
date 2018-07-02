#this is a basic plotting script in python. We will first read in a csv, which is a table separated by commas. This way you can use this script to plot whatever spreadsheet you are working on by simply saving it as a csv. pandas is a python library that is used for dealing with tables. If you have experience with the programming language R, pandas is the in-house version of R ( with arguably less functionality). Ok so lets import pandas

import pandas as pd

#The other librabry that we need is matplotlib, which is the basic library for plotting in python. Most other plotting libraries are written in matpllotlib.
import matplotlib.pyplot as plt



#Ok so lets start by reading in a simple csv that I have written using pandas (note that we imported pandas as pd). Tables are called dataframes in pandas and are often abbreviated by df
df = pd.read_csv("./simple.csv")

#lets have a look at what the table looks like. It's a good idea to always check your input before plotting anything'
print df

#Lets look at some basic pandas commands
#With this simple command you can see what the title of the columns of your table are.
print list(df)

#This command will show you what the row names of your table are
print df.index

#With this command you can display only the column with the title value
print df.value

#Here, I have listed all the different plots you can create from a simple spreadsheet with one easy command in pandas. I recommend trying out all different plot typed by feeding it into the df.plot command as kind = "(plot type)"
plots = [ "line", "bar", "barh", "hist", "kde", "density", "area", "pie", "scatter", "hexbin"]

#So here we plot the spreadheed with df.plot. The plot we are creating here is a lineplot. With no extra commands given pandas will interpret every column as a separate data series, meaning it will plot the different columns in different colours in the same plot.
df.plot( kind = "line")

#Matplotlib plots always need the plt.show to indicate that we now would like to see the plot
plt.show()

#Instead of plotting every column individually you can also tell df.plot which values to take as x and y by indicating the column index. Remember that python starts counting at 0, so the first column is 0 second 1 and so on
df.plot(x = 0 , y = 1, kind = "hexbin")   

#Here we give titles to x and y axis
plt.xlabel("Predicted")
plt.ylabel("Truth")

#This will create a figure legend automatically
plt.legend()

#And now we save the plot as a png with the title example.png. We also display the plot straight after
plt.savefig("example.png")
plt.show()

#This is it for our very simple plotting using pandas and matplotlib. We will move on to way more interesting plots in the 3dplotting.py example.