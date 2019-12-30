#!/usr/bin/env python3
from sys import argv
import os
if(argv[1] == "-y"):
	os.system("sudo omxplayer --loop --vol -2500 \"$(youtube-dl -f bestaudio -g ytsearch:"+argv[2]+ ")\"")
elif(argv[1] == "-o"):
	os.system("sudo omxplayer --vol -2500 http://proxima.shoutca.st:8357/;")
elif(argv[1] == "-s"):
	os.system("sudo pkill \"youtube-dl\"; sudo pkill -INT \"omxplayer\"")
