#!/bin/bash
read -p "Enter search term: " key
if grep -i "$key" "spotifycharts.csv"
then
	result=$(grep -i "$key" "spotifycharts.csv")
	echo "$result"
else
	echo "$key is not found in the file."
fi
