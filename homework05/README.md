# Homework 5  
The mmcif_summary.py script parses an MMCIF file and creates summary information regarding residues for each chain of the structure, then writes the summary to a JSON file.  
The script can be run directly using the python interpreter, file name, and preferred log level information, or it can be run by importing the file within another Python file and calling the main function (either way make sure constants have correct values before running). Examples shown below:  
```bash
# runs the script directly at debug log level
python3 mmcif_summary.py -l DEBUG

# runs the script directly at info log level
python3 mmcif_summary.py --loglevel INFO

# import the file and run the main function within another file
import mmcif_summary
mmcif_summary.main()
```  
## Input File  
The input file can be retrieved by downloading from the URL (using "wget" in terminal) and unzipping the downloaded zip file (using "gunzip"), as shown below:  
```bash
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz
```  

