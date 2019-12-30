#!/usr/bin/env python3
from sys import argv
from os import system as run
try:
	if(argv[1] == "-y"):
		run("sudo omxplayer --loop --vol -2500 \"$(youtube-dl -f bestaudio -g ytsearch:"+argv[2]+ ")\"")
	elif(argv[1] == "-o"):
		run("sudo omxplayer --vol -2500 http://proxima.shoutca.st:8357/;")
	elif(argv[1] == "-s"): 
		run("sudo pkill \"youtube-dl\"; sudo pkill -INT \"omxplayer\"")
	elif(argv[1] == "-h"):
		print("""-y + search term to play youtube video
-o to play otvoreni radio
-h print help(current command""")
except:
	print("""-y + search term to play youtube video
-o to play otvoreni radio
-h print help(current command""")
