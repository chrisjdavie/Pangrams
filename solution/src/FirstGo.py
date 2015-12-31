'''
Solving the hackerrank Pangrams puzzle

------------------------------

Problem Statement

Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format

Input consists of a string s.

Constraints 
Length of s can be at most 103 (1<=|s|<=103) and it may contain spaces, lower case and upper case letters. Lower-case and upper-case instances of a letter are considered the same.

Output Format

Output a line containing pangram if s is a pangram, otherwise output not pangram.

------------------------------

Created on 31 Dec 2015

@author: chris
'''

import string

inputString = set(raw_input().strip().lower())
abc = set(string.ascii_lowercase)
if abc.issubset(inputString):
    print "pangram"
else:
    print "not pangram"