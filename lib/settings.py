#!/usr/bin/env python3


# domain = True
# subscollect = ""
# urlcollect = ""
# url= ""
# maxpages = 10
# pipeline = ""

# threads = 1

# test = False
subscollect = ""
urlcollect = ""
pipeline = ""
url = ""
test = False
domain = True
threads = 1
header = {}
maxpages = 100
robots = False
proxy = {}
timeout = 0

def init():
    global pipeline 
    global threads 
    global subscollect
    global urlcollect
    global test
    global url
    global maxpages
    global header
    global robots
    global proxy
    global timeout