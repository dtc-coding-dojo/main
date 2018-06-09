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
The simplest way to store biological sequences of any kind is fasta.Fasta files usually end in .fa or .faa for amino acids and .fnt for nucleotides.  The format itself is nothing more than a header line initiated by a ">" sign followed by a line break and the sequence like this:

```
>Sequence1
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
>Sequence2
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG
AGTCCTCCTACGGACTGCGATGACTACGTACGATCGTCGACTGGCTACGTCAGACTCGACATCATGCGAATCATG

```
This way we can store a sheer unlimited amount of sequences in one simple file format which is the starting point of any sequence analysis endeavour.

### First steps in analysis
Before diving straight into comparing sequences it is a good starting point to look at what information is available about your sequences. Often in bioinformatics we forget about the bio and focus on the informatics, but just because we can do something with a computer doesn't mean it makes sense from a biological perspective. UniprotKB for example has a very comprehensive database with loads of different forms of annotations about sequences. If you're lucky your fasta header contains some form of sequence identifier which can be fed straight into the UniprotKB search bar. For the more unfortunate amongst us there is a BLAST option. BLAST which stands for Basic local alignment search tool is a way to look through any kind of sequence database given any kind of sequence. Its like going into a library with a ripped out page and BLAST is the librarian pointing out which book it came from. In a similar fashion we can take our sequence balst it against all of the UniprotKB and get the most relevant sequence. The main criteria of a good match in BLAST is the expect -value (e-value). The e-value tells you how many matches within the database you expect to see by chance when searching a database. So the lower the e-value the better your match is and the more certain you can be it is not only a random hit.

Really informative sequence features that are stored on UniprotKB (and other databases) is for example the GO term. GO stands for gene ontology and is a way of guessing which function the gene has within the organism. GO terms are hierarchical and depending on what level the particular GO-term is they can be very broad like which metabolic proces it is involved in to very specific functions like binding specific ions. The GO-term can also denote which cellular component your gene is localised. GO is in general very informative but has to be taken with a grain of salt. Often similar sequences are assigned the same GO-terms just because it is assumed similar sequences will do similar things in organisms. This is however a huge simplification, because localisation within the cell and small but important mutations can lead to an entirely different functions. As a heuristic, if your particular sequence is a well research protein like human haemoglobin for example, the GO terms should be very good. If you are looking at a protein from a not well researched genome and the BLAST hit only returns a close relative from a different species, you probably should not pay too much attention to the GO term

Another thing that is very helpful to look at is the domains. Domains are the building blocks of functions in genes. If the gene was a lego house the domains are the lego blocks. There is a limited amount of domains in all domains of life but almost limitless potential to combine them. By clicking and looking at the descriptions of domains on UniprotKB you can get a very good guess at what functions different parts of your gene fulfil. If two genes have the exact same domains in the same succession there is a good chance at them having similar functions overall. There are different domain databases of which PFam is probably the most widely used. There are two subdatabases within PFAM A and B. A are the more well descibed protein domains whereas B is still very experimental. In general you should be a bit suspicous of domains from Pfam B.

Once you have explored the information available on your sequence you can head into the first step of creating a tree.

### The Alignment
Alignments are created to see which parts of the sequence are homologous, meaning aligned nucleotides or amino acids are thought have originated from the same nucleotide or amino acids. If you think of the alingment as a matrix all columns present positions which are homologous. If there are diffferent nucleotides or amino acids in one column there was a mutation at this position. If there was a stretch of sequence added or deleted (an insertion or deletion) you introduce gaps (marked by hyphens) into the alignment.

Aligning a set of sequences is a matter of great debate. There are a lot of different opinions out there on what to use where and what counts as a good and bad alignment. A few things up front. Choosing the appropriate aligner depends on what kind of data you have. If you have a lot of sequences (>400) or very long sequences (>1000 bp) I would personally choose Pasta which is a highly efficient aligner. If you want to emphasize insertion and deletion events you should use PRANK which introduces lots of gaps into your sequence. For everything else I would probably use MAFFT. A quick note on how to install most packages in a linux environment. To install MAFFT you would type in (also all other programs described in this post can be downloaded like this):

```sudo apt-get install mafft```

MAFFT is fairly easy ot use and well maintained. It also has a --auto argument which sets parameters of the alignment itself by estimating them from the data. On the command line you would use MAFFT like this:
``` mafft --auto input.fa --thread (number of cores your computer has)   > alignment.fa```
which is a good middle gourn between being very fast and being very thorough. If you want to force MAFFT to be more thorough you can use something like:
 ```mafft --maxiterate 1000 --globalpair  input.fa  > alignment.fa``` 
This will give you an alignment in fasta format which you can easily look at in a text editor but I would seriously recommend looking at it through an alignment viewer. There are again a few opinions out there on what the best alignment vewer is. I usually use JalView which is fairly basic. JalView has a GUI (meaning a graphical user interface) which makes it easier to handle. Load your alignment into JalView (>File>Input alignment) and give it some colouring (>Colour>Percentage Identity). Here you want to check whether your alignment is good enough to create a tree from. What you are hoping for is a lot of identity (a lot of dark shaded blue) and few gaps (little white). For example this is a very good alignment


<p style="text-align:center;"> <img class="center" height="600" src="{{ "../alignment.png" | absolute_url }}" alt="" /> </p>






## This is a test header
this is a  [test hyperlink](https://google.co.uk/). 

this is test code ```hello i am code``` 

### This is a test subheader
this is more test messages
