#!/usr/bin/python

#This is script for a function that takes in a yext file with a list of new tweets in new lines and compiles the list of words used and the number of times used
#This code is for the Insight Data Engineering Program in San Fransisco, CA

#Import Libraries for use in this method

import time
import os
import sys
import numpy

start_timer = time.clock()

#Rather than reading the entire file at the beginning, the best way is to read line by line. This will avoid running
#the risk of running out of memory. If processing tweets for the whole month, that is potentially a lot of memory to 
# for reading a file. But for this feature, it easier to read the whole and then process, rather than breaking it down.


#Read file input with Tweets after switching the directory to where the file exists
os.chdir('/Users/Thulani/Desktop/InsightCode/tweet_input')
tweets = open('tweets.txt', 'r')

#Get one line from the file and split into iterable words

os.chdir('/Users/Thulani/Desktop/InsightCode/tweet_output')
ft2 = open('ft2.txt', 'w')

unique = []
median = []

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

#Close files after processes
tweets.close()
ft2.close()
stop_timer = time.clock() - start_timer

print(stop_timer)


