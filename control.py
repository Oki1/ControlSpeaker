#!/usr/bin/env python3
from sys import argv
from os import system as run
def youtube(query):
	quiet()
	run("sudo omxplayer --no-keys --loop \"\"$(youtube-dl -f bestaudio -g ytsearch:"+query+ ")\"")
otvstr = "sudo omxplayer --no-keys "
def otvoreniHit():
	quiet()
	run(otvstr + "\"http://proxima.shoutca.st:8357/;\"&")
def otvoreniHot():
	quiet()
	run(otvstr + "\"http://kepler.shoutca.st:8404/;\"&")
def otvoreniLuv():
	quiet()
	run(otvstr + "\"http://proxima.shoutca.st:8469/;\"&")
def quiet():
	run("sudo pkill \"youtbe-dl\"; sudo pkill \"omxplayer\"")

try:
	if(argv[1] == "-y"):
		youtube(argv[2])
	elif(argv[1] == "-0"):
		otvoreniHit()
	elif(argv[1] == "-1"):
		otvoreniHot()
	elif(argv[1] == "-2"):
		otvoreniLuv()
	elif(argv[1] == "-q"):
		quiet()
except:
	print("NO")
