#!/bin/bash

#This script runs the programes to determine unique tweets together with median for a page of tweets.

# Change directory to the where the source code is located
cd /Users/Thulani/Desktop/Tweeter-Challenge-Thulani/src

# Remember the working directory 
path=$(cd -) 

# Compile and run the following python programs

python words_tweeted.py

python median_unique.py

# Change back to the directory you originally were.

cd $path
