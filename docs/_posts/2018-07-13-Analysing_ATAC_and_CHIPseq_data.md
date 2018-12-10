---
layout: post
title:  "Analysis of CHIP and ATAC sequencing data"
date:   2018-07-13
excerpt: "Masterclass"
image: "/images/chipseq.png"
---

## Analysis of CHIP/ATAC sequencing data

#### Initial analysis
This is fairly straight forward, but often time consuming if using a laptop.

1. QC Fastqc file
2. Trim Reads
3. Align Reads
4. Filter alignment
5. Peak call alignment files

#### Downstream Analysis
This is less straightforward, but often quicker than the initial analysis using a laptop.

1. Visualise peaks to get a feel for your data
2. Differential Peaks
3. Gene enrichment analysis
4. Motif enrichment analysis

#### ATAC sequencing briefly
Finds areas of open chromatin, uses nuclei as raw material, hyperactive transposase enzyme cuts between nucleosomes and simultaneously tags DNA. Tagged DNA is amplified then sequenced; areas of open DNA will be enriched with reads.

#### CHIP-seq briefly
ChIP-seq combines chromatin immunoprecipitation (ChIP) with DNA sequencing. DNA is cross linked to protein, and then sheered. Antibodies immunoprecipitate and the unlink protein, the DNA can then be purified and sequenced. Areas of DNA with protein bound will be enriched with reads.

#### Minimum Laptop/Desktop specs to carry out analysis
* At least 8Gb RAM, swap/virtual memory will not work instead
* At least 30Gb hard drive space
* Reasonable processor, a slow processor will not prevent you from analysing, but it will take ages!
* If doing on a laptop make sure all alignment files are binary (.bam) files
* Linux installed, I recommend dual boot

#### Using a Cluster
This can be far quicker; particularly for the first alignment step and all programs are usually already installed on the cluster. However, it can be less flexible if you want to run programs not already installed, you will likely have to ask the system administrator to install them. Cluster access can be expensive, but some departments have their own computer cluster you can use. It is often not needed for a one off analysis, but may be necessary to analyse multiple experiments.

#### Programs required
To begin the analysis you should have at least the following programs installed:

1. Alignment: Bowtie2
2. Filtering: Samtools/Bamtools
3. Peak Calling: Macs2 (Needs Python)
4. Integrated Genome Browser (Needs Java)
5. Downstream Analysis: Homer (Needs Perl)

#### Output from Illumina NextSeq
An Illumina NextSeq machine will output data from the 4 flow cells lanes that your sample is run over. If running 'paired end', this will generate 8 Fastq files, a forward and reverse for each lane.

## The Initial Analysis

#### Trimming Reads
This is needed to remove barcode sequences from Fastq reads, although the sequencer often does this for you now. If it is needed you can use:

[Cutadapt](http://cutadapt.readthedocs.io/en/stable/index.html) a python program

#### Aligning Reads
This step will align your reads from the Fastq files to the reference genome, this allows you to see which genes your reads are located near to.
To do this use [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml).
It's a very fast C++ program, although it will still take quite a while on a laptop depending on your processor.

Use the following command for paired end reads:

```
bowtie 2 -p 4 -x /home/steve/bowtie/mouse/mm10 -1 path/to/forward/alignment -2 path/to/reverse/alignment | samtools view -bS - > alignment1.bam
```

-p This allows you to select the number of processor threads you want to run, use more to speed up the alignment, but if you use too many you may crash your computer or make it un-useable until the alignment has completed
-x This is the link to the reference genome that you will have installed when installing bowtie2
-1 This is the path to the forward Fastq file
-2 This is the path to the reverse Fastq file
| samtools view -bS - > alignment1.bam This final command pipes all output to the program Samtools to convert the output to binary, this saves hard drive space and helps speed up the filtering steps.

You will have to carry out a separate alignment for each lane, and then merge:

```
bamtools merge -in alignement1.bam -in alignement2.bam -in alignement3.bam -in alignement4.bam -out 4lanesmerged.bam
```

#### Fitering the Alignments
The aligned reads are then filtered, this is required to remove any hits to mitochondrial DNA, any duplicates from the amplification step of library preparation, and any reads that are not properly paired or aligned.
Use [Bamtools](https://github.com/pezmaster31/bamtools) and [Samtools](https://github.com/samtools/samtools) for this.

Remove mitochondrial reads:
```
samtools view -b filtered_temp.bam chr1 chr2 chr3 chr4 chr5 chr6 chr7 chr8 chr9 chr10 chr11 chr12 chr13 chr14 chr15 chr16 chr17 chr18 chr19 chX chY > filtered_temp2.bam
```

Remove non-mapped:
```
bamtools filter -isMapped true -in filtered2_temp.bam -out filtered_temp.bam
```

Remove non-paired:
```
 bamtools filter -isPaired true -in filtered_temp.bam -out filtered2_temp.bam
```

Remove Duplicates:
```
bamtools filter -isDuplicate false -in sorted_alignment.bam -out filtered_temp.bam
```

You will probably notice a recycle the same temporary files, if any of the filtering steps give an error, it may require you to index and sort the .bam first; this can be done with the following command using Bamtools:

```
bamtools sort -in alignment.bam -out sorted_alignment.bam
bamtools index -in sorted_alignment.bam
```

#### Peak Calling
Lots of programs will do this, but due to the complexity of this process, none of them do it particularly well. However, [MACS2](http://liulab.dfci.harvard.edu/MACS/) is usually considered to be the best of them.

For ATAC use:
```
Macs2 callpeak -t alignment.bam -f BAM -n peakfile
```
For CHIP use:
```
CHIP: Macs2 callpeak -t alignment.bam -c background.bam -f BAM -n peakfile
```

-t is your treated file
-c is the CHIP backgroud file
-f is file type, this will be be BAM if you have kept your alignments in binary form
-n is the output file name, this will be in .bed format

#### This completes the initial alignment, at this point you should now have:

1. Filtered alignment files, in the binary .bam format.
2. A peak called filed in .bed file format (This is small so does not need to be binary)

#### Pipeline
You should have noticed that the initial analysis, although time consuming is quite straightforward, to that end it is possible to write a simple script in Perl or Python to automate the process. Or if you're more familiar with Linux, a shell script is perfect for this! Just simply call each program in turn with the correct command, by doing this you can leave your laptop running each program in turn over night. 

## Downstream Analysis
This is when we begin to get an idea of whether the experiment has worked!!

#### Visualise in Genome Browser,
This is a good first step to see if your experiment has worked, you can visualise the coverage of your .bam files, and hopefully you should see the nice peaks that are associated with ATAC/CHIP data.
The [Integrated Genome Browser](http://bioviz.org/) can be installed locally.

#### Differential Peaks
This essentially forms the basis of the downstream analysis; you are hoping to find peaks in your treated data that are not present in your control/background data. This indicates for ATAC that an area of DNA has opened in the treated sample, and indicates an open transcription factor binding site in CHIP.

[Homer](http://homer.ucsd.edu/homer/) is a good place to start for this, as is relatively simple to use, and will carry out a basic differential analysis of your peaks. It is a little less useful for more complex data sets involving multiple replicates and treatments. Once you’re happy with Homer, I would then move to [DiffBind](https://bioconductor.org/packages/release/bioc/html/DiffBind.html) an R program from the [Bioconductor package](https://bioconductor.org/).

## Homer
You first need to make [Homer tag directories](http://homer.ucsd.edu/homer/ngs/tagDir.html), these are like .bam files that have been sorted, unfortunately Homer does not accept sorted .BAM files at present but he hopes to in the future. To make the tag directories:

One for your treated sample and one for the background/control:
```
makeTagDirectory /home/tagdirectory /home/treated_alignment_file1 (/home/treated_alignment file 2)
makeTagDirectory /home/tagdirectory /home/control_alignment_file1 (/home/control_alignment_file 2)
```

The first argument is the location where you wish the tag directory to be located, you can create this directory beforehand if you want, and the second argument is the location of your .bam file. It is possible to add multiple .bam files to the tag directory; this can be useful for pooling replicates or .bam files from different sequencing lanes if you did not merge previously.

You can then use the tag directories with your peak file to look for differential peaks:


```
getDifferentialPeaks /home/treated.bed /home/treated_tag_directory /home/background_tag_directory > differentialpeaks
```

This will output a Homer differential peak file, it is essentially the same as a normal .bed file but with some extra columns, one column is the p-value for each peak, this is useful to see where your best peaks are located. Homer looks at the location of each peak, and calculates the p-value from the difference in the number of aligned reads in the background vs the treated.

#### Gene enrichment analysis
Now that you have a differential peak file, you can use this to see which genes are enriched in your treated sample, first you need to annotate the peaks in the file; HOMER can help us to do this:


```
annotatePeaks.pl differentialpeaks.txt genome   > geneannotated.txt
```
You need ensure you have installed the correct genome for whatever species your sample is from.


This outputs a text file containing lots of information about the genes located near to your peaks. The text file can be opened in open office, and your gene list can be extracted. I usually copy the gene list into a new text file, so it's ready to be uploaded onto websites, or to be used by another program. I copy the entrez gene identifiers because it's a number, so cannot be misinterpreted by websites, and is also species specific.

To begin a gene enrichment analysis, the website [DAVID](https://david.ncifcrf.gov/) is an easy place to start, simply click on start analysis, copy your gene list, select entrez gene identifier, and then submit. Once the gene list has been accepted, click on 'Functional Annotation Tool' to begin the analysis, there's a nice big arrow above this! This will give you lots of output, including; gene ontology, pathway analysis, tissue expression, protein domain analysis, I suggest you just have a play around with the different links; the pathway analysis is quite useful as you can get it to output a nice figure.

If you want to use your differential peak file in another program, you will have to convert it from Homer format back to a normal .bed file; this can be done simply with the following command:


```
pos2bed.pl differentialpeaks.txt > differentialpeaks.bed
```


#### Motif enrichment analysis
Homer is one of the better programs for Motif analysis; you can either submit your gene list to Homer, or the differential peak file itself. Homer will search in the promoter regions around your gene of interest to see what motifs are present and if they appear enriched, it will perform a De Novo motif analysis, as well as searching for already known motifs. 
The commands:

Gene list:
```
findMotifs.pl genelist.txt <promoter set> /home/motifs
```
You need to ensure you have installed the promoter set for whatever species you are searching within, the last parameter is the output directory.

For a peak file:
```
findMotifsGenome.pl differentialpeaks.txt genome /home/motifs
```
The genome should already have been installed for the annotation step.


#### Finished!! Or nearly! This should give you a good start to your analysis; this is as far as I have got with mine, so please email me with any suggestion or corrections for this page steven.walsh@biodtp.ox.ac.uk. Hope this helps you get started!!

#### Other useful programs
Here are a couple of other useful programs for analysing CHIP/ATAC seq:

[Picard](https://broadinstitute.github.io/picard/) You need Java installed to run this, but it has loads of handy tools.

[bedtools](http://bedtools.readthedocs.io/en/latest/) This is written in C++ so should install easily.


Written by Steven Walsh
