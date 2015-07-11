#!/usr/bin/python

#This is script for a function that takes in a yext file with a list of new tweets in new lines 
# and compiles the list of words used and the number of times used

#This code is for the Insight Data Engineering Program in San Fransisco, CA

#Import Libraries for use in this method

import time
import os

# start timer
start_timer = time.clock()


#Read file input with Tweets after switching the directory to where the file exists
#Read files from specified $PATH. tweets is for reading, ft2 and ft3 is for writing.

os.chdir('/Users/Thulani/Desktop/Tweeter-Challenge-Thulani/tweet_input')
tweets = open('tweets.txt', 'r')

os.chdir('/Users/Thulani/Desktop/Tweeter-Challenge-Thulani/tweet_output')
ft1 = open('ft1.txt', 'w')
ft3 = open('ft3.txt', 'w')

#Get one line from the file and split into iterable words
# Make sure to take care of the edge case when the end of the file is encountered

#Initialize word count dictionary 
wordcount = {}

while True:
    try:
        d = tweets.next()
        words = d.split()
        for word in words:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

    except StopIteration:
        break



#Do sorting at the end. Save sometime, such that I dont have to do the sorting so many times
# Sort the counted words
for word in sorted(wordcount):
    ft1.write( "%s\t\t %d\n" % (word, wordcount[word]))

stop_timer = time.clock() - start_timer

ft3.write( "Time (in seconds) to order and count words tweeted: %10.6f\n" % (stop_timer))

#Close files after processes
tweets.close()
ft1.close()




