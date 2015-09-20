import wave
import sys
# assignment 3


def getinfo(wf,bit):
	print bit+'bit'
	print "channel:", wf.getnchannels() 
	print "framerate",wf.getframerate() 
	print "frames:",wf.getnframes() 
	print "width:",wf.getsampwidth()

wf= wave.open('sample.wav','rb')
getinfo(wf,'16')
wf= wave.open('sample8bit.wav','rb')
getinfo(wf,'8')
wf= wave.open('sample32bit.wav','rb')
getinfo(wf,'32')
