#!/bin/bash
echo "This script will download today's list of top songs from SpotifyCharts."
echo "Please note, this will overwrite the any existing files of the same name."
wget https://spotifycharts.com/regional/global/daily/latest/download -O spotifycharts.csv
