## CISC 3140
## Kevin Wong
## Lab 5

### Task 1
Description: Using a Linux terminal, extract information from a structured data format.  
1. First step is to get the website html code into a .txt file so it doesn't clog up the terminal.  
    `curl https://spotifycharts.com/regional -o spotifycharts.txt`  
2. Second, we use `grep` function to find the `csv` keyword in order to get the correct url for the CSV file.  
    `grep csv spotifycharts.txt`  
4. After that we just append the url onto the original website and run a wget command, adding a -O to output it to a .csv file.  
    `wget https://spotifycharts.com/regional/global/daily/latest/download -O spotifycharts.csv`  

### Task 2
Description: Combine Task 1 with an automate shell script.
I have created two shell scripts. Run using the following command:  
`./ShellScriptName`

Following are the two scripts:  
downloadSpotifyCharts.sh:  
```bash
#!/bin/bash
echo "This script will download today's list of top songs from SpotifyCharts."
echo "Please note, this will overwrite the any existing files of the same name."
# runs wget to download csv from link then uses -O to output to a local file
wget https://spotifycharts.com/regional/global/daily/latest/download -O spotifycharts.csv
```  
search.sh:  
```bash
#!/bin/bash
# asks user for key input
read -p "Enter search term: " key
if grep -i "$key" "spotifycharts.csv" # checks if key is in file
then
    # if key is in file, finds all instances and outputs to terminal
	result=$(grep -i "$key" "spotifycharts.csv")
	echo "$result"
else
    # if key not found, displays following
	echo "$key is not found in the file."
fi
```
