---
layout: post
title:  "From Fasta to Phylogentic Tree"
date:   2018-05-08
excerpt: ""
image: "../phylogenetic_intro.png"
---
### The Problem
Often when trying to analyse sequences of any kind you will find yourself interested in the relatedness between them. From trying to infer relatedness between species or trying to figure out which genes have a common origin, a lot of information can be drawn from the pure amino acid or nucleotide sequences. One of the best and most intuitive way of displaying relationships between sequences is a phylogenetic tree, which is exactly what we're trying to produe in this session.

### The Data
The simplest way to store biological sequences of any kind is fasta. Which is nothing more than a header line initiated by a ">" sign followed by a line break and the sequence like this:

```
>Sequence1
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
>Sequence2
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG

```
This way we can store a sheer unlimited amount of sequences in one simple file format which is the starting point of any sequence analysis endeavour.




## This is a test header
this is a  [test hyperlink](https://google.co.uk/). 

this is test code ```hello i am code``` 

### This is a test subheader
this is more test messages
