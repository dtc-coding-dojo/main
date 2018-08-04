---
layout: post
title:  "Machine Learning for Beginners"
date:   2018-06-29
excerpt: "Masterclass"
image: "/images/proatterminal.jpg"
---

### Machine Learning: Blessing or Curse for Science?
Machine Learning (ML), similar to Artificial Intelligence (AI) and Deep Learning has become somewhat of a buzzword in todays which people pass around without necessarily understanding what it means. So what are these terms in relation to ML. Artificial Intelligence can be any intelligence displayed by a machine as opposed to living beings. ML is a subdivision of AI and Deep learning is in turn a subdivision of ML. Deep learning is a special type of artificial neural network which is particularily "deep", meaning that is hat lots of layers.

Conceptually ML is not more than a statistical procedure that improves its own accuracy without the need anyone to interfere. This is both a blessing and a curse, because the accuracy improvements can be hard or impossible to understand, which is especially dangerous for us as scientists who want to understand what we're doing. Machine Learning is a hammer which makes everything sort of look like a nail. Due to the frenzy of a lot of hammer wielders and the black box nature of ML applications you will encounter a lot of researchers who are opposed to using ML in our research.I have heard one professor call it "the worst thing that ever happened to science", due to how quckly accurate results can be achieved without the need to understand the underlying theory or even how the analysis works. As with any powerful tool we have to use it wisely and understand it thoroughly in order to make proper use of it. So let's try to understand what the whole craze is about ML.

The term Machine Learning was coined in 1959 by a statistician in the field of Artifical Intelligence. The concept itself is quite old, but only the recent emergence of computers powerful enough to implement the complex algorithms ML uses has brought about the coming of age of ML applications.  Since it's conception ML has diverged from the frequentist (observing and counting) approach of statistics to a more computer science grounded trial and error procedure. With growing computing prowess there is no need anymore to think carefully about which parameters might be optimal for a certain problem we can just try out all of them and see which one does best. Which is prtly why it is criticised in science as we don't have to think how fast for example certain populations migrate, we can simply try out all possible migration rates and see what describes nature the best. ML can make a pretty complacent scientist.


### What is Machine Learning?
However mysterious it might be to the beholder, ML is no black magic. ML is an information lever, it can generate a lot of knowledge from a little knowledge. The more information you put in, the more information ML will put out, which is an important concept to remember when looking at what to feed into the ML. The goal of any ML approach is to make a prediction. Whatever flavour you will use the principle is always to learn underlying structures from as much data as possible (a process called training) and apply that knowledge on new unseen data (a process called generalisation). The data used in training can be labelled so that the algorithm can learn how to differentiate between these labels by learning the characteristics of that class. This is called supervised ML. The unsupervised counter-part deals with unlabelled data to try understand underlying priniciples of how the data was generated. Sticking with the concept of ML as a lever, if there are labels of your data available, they should always be used. In line with this concept there is semi-supervised learning in which there is some labeled data and some unlabeled data, so the information that is contained in the few labels is not lost to unsupervised learning.

Overall supervised and unsupervised learning are the two flavours in which ML comes, which can both do 4 basic tasks:

1. **Classification** divides data into different groups. In training classes are learned by the ML algorithm to then try to divide new unseen data into the classes seen in training. A typical classification task is spam filtering, where the two classes are spam and non-spam. Classification  supervised ML task.

2. **Regression** learns the relationship between variables and apply this knowledge to new unseen variables. It can therefore predict the change in a variable that is given to the algorithm. This is often use in finance to do market predictions

3. **Clustering** is similar to classification in that it tries to group data. The difference is that classification re 

4. **Dimensionality Reduction** 

Quite often one ML technique can handle multiple of these tasks. A simple linear regression for example can do both a regression and a classification.
