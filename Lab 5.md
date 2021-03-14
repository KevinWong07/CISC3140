## CISC 3140
## Kevin Wong
## Lab 5

### Task 1
Description: Using a Linux terminal, extract information from a structured data format.  
1. First step is to get the website html code into a .txt file so it doesn't clog up the terminal.  
    `curl https://spotifycharts.com/regional -o spotifycharts.txt`  
2. Second, we use `grep` function to file the `csv` keyword in order to get the correct url for the CSV file.  
    `grep csv spotifycharts.txt`  
4. After that we just append the url onto the original website and run a wget command, adding a -O to output it to a .csv file.  
    `wget https://spotifycharts.com/regional/global/daily/latest/download -O spotifycharts.csv`  
