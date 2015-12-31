'''
Pythonic code golfing it up, inspired by https://www.hackerrank.com/caikehe
in the hackerrank forums

Created on 31 Dec 2015

@author: chris
'''
import string
print ["not pangram","pangram"][set(string.ascii_lowercase).issubset(raw_input().strip().lower())]