# Homework 7  
You can use the docker file in this folder to open a Redis database in a running container in the background, while you execute the get_ncbi_genbank_records.py script to search and retrieve records from the NCBI protein database (using an input search term) that are written to an output TXT file.  
## How to start up the Redis container  
With the docker-compose.yml file in your working directory, run the following in your command line: ```docker compose up -d```. This runs the service in the docker compose file in a container in the background (opening the redis database to be accessed).  
## Running the script  
Given a command-line input loglevel (using ```-l```), output file name (```-o```), and search term (```s```) (all of which have default values if you do not specify), this script searches the NCBI protein database and uses found IDs to retrieve records that are saved to the Redis database and then retrieved from Redis to be written to a TXT file.  
First run the following in your command line to make the script executable without invoking the python3 interpreter:  
```bash
chmod u+x get_ncbi_genbank_records.py
```  
Then call the script with command line inputs (will use default values if not specified). Example command:  
```bash
./get_ncbi_genbank_records.py -l INFO -o genbank_records.txt -s 'Arabidopsis thaliana AND AT5G10140'
```  
## Closing the Redis container  
Once you finish running the script, stop and remove the container using ```docker compose down```.