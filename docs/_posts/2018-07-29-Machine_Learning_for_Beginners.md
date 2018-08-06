---
layout: post
title:  "Machine Learning for Beginners"
date:   2018-06-29
excerpt: "Masterclass"
image: "/images/ml_logo.png"
---

### Machine Learning: Blessing or Curse for Science?
Machine Learning (ML), similar to Artificial Intelligence (AI) and Deep Learning has become somewhat of a buzzword in todays which people pass around without necessarily understanding what it means. So what are these terms in relation to ML. Artificial Intelligence can be any intelligence displayed by a machine as opposed to living beings. ML is a subdivision of AI and Deep learning is in turn a subdivision of ML. Deep learning is a special type of artificial neural network which is particularily "deep", meaning that is hat lots of layers.

Conceptually ML is not more than a statistical procedure that improves its own accuracy without the need anyone to interfere. This is both a blessing and a curse, because the accuracy improvements can be hard or impossible to understand, which is especially dangerous for us as scientists who want to understand what we're doing. Machine Learning is a hammer which makes everything sort of look like a nail. Due to the frenzy of a lot of hammer wielders and the black box nature of ML applications you will encounter a lot of researchers who are opposed to using ML in our research.I have heard one professor call it "the worst thing that ever happened to science", due to how quckly accurate results can be achieved without the need to understand the underlying theory or even how the analysis works. As with any powerful tool we have to use it wisely and understand it thoroughly in order to make proper use of it. So let's try to understand what the whole craze is about ML.

The term Machine Learning was coined in 1959 by a statistician in the field of Artifical Intelligence. The concept itself is quite old, but only the recent emergence of computers powerful enough to implement the complex algorithms ML uses has brought about the coming of age of ML applications.  Since it's conception ML has diverged from the frequentist (observing and counting) approach of statistics to a more computer science grounded trial and error procedure. With growing computing prowess there is no need anymore to think carefully about which parameters might be optimal for a certain problem we can just try out all of them and see which one does best. Which is prtly why it is criticised in science as we don't have to think how fast for example certain populations migrate, we can simply try out all possible migration rates and see what describes nature the best. ML can make a pretty complacent scientist.


### What is Machine Learning?
However mysterious it might be to the beholder, ML is no black magic. ML is an information lever, it can generate a lot of knowledge from a little knowledge. The more information you put in, the more information ML will put out, which is an important concept to remember when looking at what to feed into the ML. The goal of any ML approach is to make a prediction. Whatever flavour you will use the principle is always to learn underlying structures from as much data as possible (a process called training) and apply that knowledge on new unseen data (a process called generalisation). The data used in training can be labelled so that the algorithm can learn how to differentiate between these labels by learning the characteristics of that class. This is called supervised ML. The unsupervised counter-part deals with unlabelled data to try understand underlying priniciples of how the data was generated. Sticking with the concept of ML as a lever, if there are labels of your data available, they should always be used. In line with this concept there is semi-supervised learning in which there is some labeled data and some unlabeled data, so the information that is contained in the few labels is not lost to unsupervised learning.

Data is often fed to machine learning in spreadsheets. Some are alread formulated in spreadsheets but in problems like image recognition there is some thought necessary to put the problem into a table. The process of extracting features from an object into a ML usable form is called feature extraction and can be quite demanding. There are different types of data to consider, for example there is binary (True and False often expressed in 0 and 1) count (1, 2, 5), categorical (red, white, blue), real-valued (0.3, 1.4, 6.7) which don't necessarily mix well. Also often data has to be scaled so the different columns are comparable. If one feature is measured in cm and another in km, the cm column is more likely to have huge variation and therefore contributes much more to decision making. Scaling could easily be achieved to both columns by making the biggest value =1 and the smallest = 0 and modify values in between arcodingly (min-max-scaling). 

The resulting table is usually organised in a way that rows are samples of your data, whereas columns are features, which are also called dimensions. You  will encounter someone speaking with dread of high-dimensional data. High-dimensional data is nothing more than a spreadsheet with a lot of columns and the dread usually comes from something that's called the curse of dimensionality. This ominous phrase refers to the common problem of dadta becoming sparse in high dimensions, meaning that there are only few non-zero values present, complicating analysis. With growing dimensionality, data analysis quickly becomes a needle in a haystack problem.

Overall supervised and unsupervised learning are the two flavours in which ML comes, which are each used for two basic purposes respectively:

* Supervised Machine Learning
..* **Classification** divides data into different groups. In training data all samples with the same labeled constitute one class. The algorithm learns the specific characteristics of one class by looking at the data. New unseen data is then divided into the classes seen in training. A typical classification task is spam filtering, where the two labels are spam and non-spam. In two dimensional space the border between classes which is used to group new data is called decision boundary.

..* **Regression** learns the relationship between variables in training and apply this knowledge to new unseen variables. It can therefore predict the change in a variable that is given to the algorithm. For example different labels can be time points.This is often use in finance to do market predictions

* Unsupervised Machine Learning
..* **Clustering** is similar to classification in that it tries to group data by looking at the relationship between samples. However it operates without the information given to classification through the presence of labels. Clustering can be used to assign labels to every sample in a given cluster. These can then be used for supervised ML.

..* **Dimensionality Reduction** is a measure that can reduce the burden of having very high-dimensional data. Dimensionality reduction tries to capture the information contained in high-dimensional space as good as possible in lower dimesnional space. In practice this means it boils your table with 60000 columns down to 50 columns, without losing a lot of information. This not only makes everything quicker, but can also reduce noise in the data-set.

 Noise is everything in the data which doesn't help solving the problem at hand and can be a big problem. Fitting a ML too well on the noise specific to your data-set will make it unlikely to perform well on unseen data, which is a problem called overfitting. Essentially your model has too many parameters and is so fine-tuned on your specific set of observations, every new observation with new unseen random noise will throw off your model. You have fitted a model too well on the data.  The opposite is an underfitted model where the underlying structure of the data is not captured, so your model was not fit well enough and probably has too few parameters. 

In order to see how well your model performs, there are multiple different measures. When looking at classification the simplest is accuracy. How many of the labels are assigned correctly. However when one imagines unbalanced class problems like cancer, accuracy quickly becomes useless. Where 99.9 percent have the class no cancer, every predictor which just says no cancer every time will achieve 99.9 accuracy but is useless as a model. Therefore multiple scorers have been designed which are applicable depending on the underlying problem. To understand ML performance scorers one first has to understand the concepts of True positive, False positive, True negative and False negative:
* **True positives (TP)**, where the sample is predicted as a certain label by the model and truly has this label in the training data.
* **True Negatives (TN)**, where the sample is not predicted as a certain label and truly does not have this label.
* **False Positives (FP)**, where the sample is predicted as a certain label, but does not truly have that label.
* **False Negatives (FN)**, where the sample is not predicted as a certain label, but truly has that label.

The concept is easier to understand in a Figure:

<p style="text-align:center;"> <img class="center" width="900" src="{{ "../images/tptn.png" | absolute_url }}" alt="" /> </p>

A perfect classifier would have only TP and TN and we would be at the end of optimisation. However this is rarely the case in reality and trying to increase one desirable number like TN often ends up also increasing FP. So different trade-offs have to be calibrated carefully to achieve an optimal score for your problem. There are multiple scorers available to be optimised:

<p style="text-align:center;"> <img class="center" width="900" src="{{ "../images/ml_scorers.png" | absolute_url }}" alt="" /> </p>

There is not one optimal scorer for every task. Precision for example should be looked at when you want to make sure that of what you have predicted 

Quite often one ML technique can handle multiple of these tasks. A simple linear regression for example can do both a regression and a classification.
