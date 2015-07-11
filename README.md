Tweeter-Challenge-Thulani
==========================

This program count the number of times each word has been used and the calculates the median number of unique words per tweet
This is a self contained program, written using a mac OS

This is achieved through the two source files, tweeted_words.py and median_unique.py

	Added features:
ft3 = This feature shows the number of tweets that have been processed. In addition, more to the code writer, it shows how long the computation took. It will also show the most frequently used word. This can be used to determine what news of hash tags are trending. This can be done both at the tweet level, or the tweet batch. Both ways will be implemented.

	Other considerations:
there are two instances on both programs [4 total] that refer to a $PATH to a directory. For the program to run properly, these will need to be updated to reflect the current place the repo is located. 


	Considerations:
It is essential to manage program memory. Processing a file at once is not a smart way of going about this program, mainly
because the file might be big enough to clogg the entire memory. As a result, I tried to my best to load files and then process line by line. This should theoretically improve compuatational time. 

Loops are very notorious in increasing computation time. Avoiding loops is the ideal approach, but I wasnt very successful in doing that. Given more time, I would really like to hammer down and remove loops as much as possible

Recursive programing and functions are way better in improving computational time. I was also very unsuccessful in this front as well. Using this approach is guaranteed to eliminate loops. 


