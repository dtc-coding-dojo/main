#seaborn is a more advanced plotting library that is written with pandas in mind as a basis. It can draw very advanced plots with very simple commands. You can modify all of the command with additional arguments which you can get from their webpage or simply by using google.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Seaborn comes with examle datasets shipped that we can use to display the plotting functions
planets = sns.load_dataset("planets")

#First let's have a look at the dataframe
print planets

#Here we generate a list of years between 2000 and 2015. Using this range we will plot a factorplot, which counts the number of datapoints in a category and displays the amount of points as height of a barplot. Here our category is years and our datapoints are the planets
years = np.arange(2000, 2015)
g = sns.factorplot(x="year", data=planets, kind="count")
g.set_xticklabels(step=2)
plt.show()

#Let's load another dataset and look at it
gammas = sns.load_dataset("gammas")
print gammas

#now we plot a timescale plot which follows the gamma values over time. There are three different lines in this plot which are the three categories defined in the column ROI. The time is given in the column timepoint. The unit will be used to calculate errors around the line and the value gives the y-values of the line
sns.tsplot(data=gammas, time="timepoint", unit="subject",
           condition="ROI", value="BOLD signal")
plt.show()


#Next we're going to draw a histogram. For this we first need some data. The following two line will generate a hundred datapoints all normally distributed around 0 with the standard deviation of one
rs = np.random.RandomState(10)
d = rs.normal(size=100)

#This plot will create a simple blue histogram
sns.distplot(d, kde=False, color="blue")
plt.show()

#Now we want to draw 4 different histograms all in the same plot. Therefore we need to initiate a figure with 4 different fields which we do with subplots. The 2,2 denotes we want 2 rows and 2 columns of plots. The figsize denotes the figure size and the sharex makes all plots share the same x axis
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)

#The first histogram is the same as we plotted last time. With the ax=axes[ 0, 0] we tell this plot to gow in the first row and first column so into the upper right corner
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])

#This is a density plot which is like a histogram but with a smooth curve drawn over it. Also we plot a "rug" meaning that every datapoint is also plotted with a vertical bar on the x axis. This plot will go into the upper right corner
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])

#This is the same as before but without the rug plot and with the area under the density plot coloured in, which will go into the lower left corner
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])

#This is a histogram and a density plot over each other. This plot will show up on the lower right
sns.distplot(d, color="m", ax=axes[1, 1])
plt.show()


#Let's load another dataset and look at it
tips = sns.load_dataset("tips")
print tips

#Here we generate a boxplot using the total_bill column as a y-value and the day as an x-value
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

#These are violinplots which are very similar to boxplots but additionally to the boxplots there are hiistograms plotted verically on top of the boxplot. This way we can see the distribution of the data
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

#We will use the brain_netowrks dataset next
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
print df

#Seaborn can very easily plot heatmaps with this simple command
sns.heatmap(df)
plt.show()

#And with the annot=true option we can plot the actual data values onto the heatmap
sns.heatmap(df, annot = True)
plt.show()

#A clustermap is a heatmap technically where the rows and columns get grouped (or clustered) by similarity. The clustermap then draws trees on top of the rows and columns to show the grouping of the columns
sns.clustermap(df)
plt.show()


#Here we load the iris dataset
df = sns.load_dataset("iris")
print df

#Lets now do a scattermatrix which is a good way to explore any kind of data. It will simply plot every column against every other column and itself toreveal trends within the data (i.e. correlation)
#Here we create a pairgrid, which is a square shaped matrix with the number of columns as x and y. So if we have 4 columns as an input our pairgrid has 4 rows and 4 columns resulting in 16 fields.
g = sns.PairGrid(df, diag_sharey=False)
#Now we can fill this grid with plots. As the columns function as both x and y value the diagonal will be the column against itself. Here we want density plots of the points which is basically a smoother histogram. A histogram is displaying on the y-axis how many datapoints you have of each x-value.
g.map_diag(sns.kdeplot, lw=3)
#Now we want the upper triangle of our plot to be scatterplots to see whether there are trends within our data.
g.map_upper(plt.scatter)
#As we already have scatterplots in the upper triangle we can go for something in the lower triangle (keep in mind this is a square like matrix where columns and rows are the same, so we have every cell twice except the diagonal). Here we can plot a kernel density plot which is a way to display datapoints in a scatterplot as density, so where there are more points you have higher density. 
#You will notice that the command for density and kerneld density plots are the same. Seaborn will automatically draw a density plot if x and y are the same and a kernel density plot if they differ
g.map_lower(sns.kdeplot)
plt.show()

#Now we generate a few random points again this time using a gammy distribution instead of a normal distribution and also generate some normalised y values.
rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)

#This is a scatterplot which also plots a histogram above the x and y axis. Additionally there is a pearson coefficient and a p-value
sns.jointplot(x, y, kind="scatter")
plt.show()

#the same scatterplot now has a regression line drawn through the scatterplot and a density plot added to the histogram
sns.jointplot(x, y, kind="reg")
plt.show()

#Here the scatterplot gets substituted by hexplot
sns.jointplot(x, y, kind="hex")
plt.show()