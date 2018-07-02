import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#planets = sns.load_dataset("planets")

#print planets

#years = np.arange(2000, 2015)

#g = sns.factorplot(x="year", data=planets, kind="count",
                   #palette="BuPu", size=6, aspect=1.5, order=years)
#g.set_xticklabels(step=2)

#plt.show()






#gammas = sns.load_dataset("gammas")

#print gammas

## Plot the response with standard error
#sns.tsplot(data=gammas, time="timepoint", unit="subject",
           #condition="ROI", value="BOLD signal")

#plt.show()



#df = sns.load_dataset("iris")

#print df

#g = sns.PairGrid(df, diag_sharey=False)
#g.map_lower(sns.kdeplot, cmap="Blues_d")
#g.map_upper(plt.scatter)
#g.map_diag(sns.kdeplot, lw=3)

#plt.show()






#rs = np.random.RandomState(10)
#d = rs.normal(size=100)
#sns.distplot(d, kde=False, color="b")
#plt.show()






#f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
#sns.distplot(d, kde=False, color="b", ax=axes[0, 0])
#sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])
#sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
#sns.distplot(d, color="m", ax=axes[1, 1])
#plt.show()






#df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)
#print df
#sns.kdeplot(df)
#plt.show()

#sns.heatmap(df)
#plt.show()

#sns.heatmap(df, annot = True)
#plt.show()

#sns.clustermap(df)
#plt.show()







tips = sns.load_dataset("tips")

print tips

sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()



iris = sns.load_dataset("iris")

print iris

# "Melt" the dataset to "long-form" or "tidy" representation
iris = pd.melt(iris, "species", var_name="measurement")

# Draw a categorical scatterplot to show each observation
sns.swarmplot(x="measurement", y="value", hue="species", data=iris)








sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True,
               inner="quart", palette={"Male": "b", "Female": "y"})
plt.show()





rs = np.random.RandomState(11)
x = rs.gamma(2, size=1000)
y = -.5 * x + rs.normal(size=1000)


sns.jointplot(x, y, kind="scatter")
plt.show()

sns.jointplot(x, y, kind="reg")
plt.show()


sns.jointplot(x, y, kind="hex")
plt.show()