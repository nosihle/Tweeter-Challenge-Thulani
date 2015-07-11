#!/usr/bin/python

#This is script for a function that takes in a text file with a list of new tweets in new lines and compiles the number 
# of unique words in a tweet. It then calculates the median number of words and the number of tweets processed.

#This code is for the Insight Data Engineering Program in San Fransisco, CA

#Import Libraries for use in this method

import time
import os
import numpy

# set timer to keep track of the time that has elapsed
start_timer = time.clock()


#Read files from specified $PATH. tweets is for reading, ft2 is for writing and ft3 is for appending.
os.chdir('/Users/Thulani/Desktop/Tweeter-Challenge-Thulani/tweet_input')
tweets = open('tweets.txt', 'r')

os.chdir('/Users/Thulani/Desktop/Tweeter-Challenge-Thulani/tweet_output')
ft2 = open('ft2.txt', 'w')
ft3 = open('ft3.txt', 'a')

# Initialize arrays for number of unique words per tweets and the median.
unique = []
median = []


# This block gets the next line from tweets, count the words for that line, 
# calculates the unique words for that tweet by looking at the size of the dictionary/array.
# The median is then calculated using the elements of the unique words. Median is written to file as it comes.
# This block is exited when the end of file is encountered.

# It is important to re-initialize the wordcount everytime at the beginning of the next loop. 
while True:
    wordcount = {}
    try:
        d = tweets.next()
        words = d.split()
        for word in words:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
        unique.append(len(wordcount))

        new_entry = numpy.median(numpy.array(unique))

        ft2.write( "%s\n" % (new_entry))

        median.append(numpy.median(numpy.array(unique)))

    except StopIteration:
        break

stop_timer = time.clock() - start_timer

# Write the number of tweets that have been processed, the time it took to run the median_unique.py
ft3.write( "Time (seconds) to process words per tweet: %10.6f\n" % (stop_timer))
ft3.write( "The number of tweets processed: %d\n" % (len(median)))

#Close files after processes to free up memory
tweets.close()
ft2.close()
ft3.close()


