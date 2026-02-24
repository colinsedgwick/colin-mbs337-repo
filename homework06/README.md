# Homework 6  
The files in this folder allow you to create an image from which you can run containers that execute scripts related to processing FASTA, FASTQ, and mmCIF file data.  
## Building the image from a Dockerfile  
While the Dockerfile is in your working directory, run the following code to build the image using the instructions in the Dockerfile.  
```bash
docker build -t <dockerhubusername>/<code>:<version> ./
```  
## Where to get the input files  
Using the commands below allows you to download and unzip the input files used to generate the output in the output_files folder.  
```bash
# FASTA file  
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz  
gunzip immune_proteins.fasta.gz  
  
# FASTQ file  
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz  
gunzip sample1_rawReads.fastq.gz  
  
# mmCIF file  
wget https://files.rcsb.org/download/4HHB.cif.gz  
gunzip 4HHB.cif.gz  
```
## Running containerized code from outside the container  
Below is information regarding how to run containerized code outside the container from the command line. Here is an example for reference:  
```bash
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) colinsedgwick/homework06:1.0 fasta_stats.py -l INFO -f /data/immune_proteins.fasta -o /data/immune_proteins_stats.txt
```  
An image to run the container from must be specified in the docker run command. ``` --rm ``` is used to remove the container after it is run.  
### Mounting data inside the container at runtime  
Using ``` -v $PWD:/data``` in you docker run command allows you to mount the input data from your working directory into /data within the container.  
### Running containerized code as specific user to avoid permission issues  
Running the containerized code without specifying the user will cause the owner of all generated output files to be root, which can cause permission issues. You can specify the user and group ID namespace to yours using ``` -u $(id -u):$(id -g)``` in your docker run command.  
### Parameters for each script  
Each script takes specified parameters such as the path of the input file to be used in the execution of the script. Following the path of the script to be run, you can specify the parameter shorthand (e.g. ``` -f ```) followed by the value (e.g. ``` script.py ```). Here are the available parameters for each script:  
#### fasta_stats.py  
```bash
# loglevel 
-l
# input FASTA file
-f
# output TXT file
-o
```  
#### fasta_filter.py
```bash
# loglevel 
-l
# input FASTA file
-f
# output FASTA file
-o
# minimum length of protein to filter by
-m
```  
#### fastq_filter.py
```bash
# loglevel 
-l
# input FASTQ file
-f
# output FASTQ file
-o
# minimum average Phred score to filter by
-m
# encoding used for Phred scores
-e
```  
#### mmcif_summary.py
```bash
# loglevel 
-l
# input mmCIF file
-m
# output JSON file
-o
```  
## Output files and where to find them  
The expected output files for running the containerized code on the given input files includes a TXT file of summary stats of the input FASTA file for fasta_stats.py, a FASTA file of proteins filtered for length from the input FASTA file for fasta_filter.py, a FASTQ file of sequencing reads filtered for average Phred score from the input FASTQ file for fastq_filter.py, and a JSON file containing summary stats of each chain within a protein structure from an input mmCIF file for mmcif_summary.py.  
Each of these output files can be be found within your working directory after running the containerized code, as the working directory is mounted to /data within the container using the docker run command ``` -v $PWD:/data ``` .


