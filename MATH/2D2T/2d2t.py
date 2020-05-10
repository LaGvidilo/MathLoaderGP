#coding: utf-8
from copy import deepcopy
import numpy as np
from PIL import Image
import random
from statistics import mean
import json
class TimeSpace_2d4t:
	def __init__(self,sizecube=128):
		self.sizecube = sizecube
		self.cube = {0:[[0 for i in range(0,sizecube)] for j in range(0,sizecube)]}
		self.othertemporal = deepcopy(self.cube)
	def set(self,d1,d2,t1,value):
		self.cube[t1] = [[0 for i in range(0,self.sizecube)] for j in range(0,self.sizecube)]
		self.cube[t1][d1][d2] = value
	def setother(self,d1,d2,t1,value):
		self.othertemporal[t1] = [[0 for i in range(0,self.sizecube)] for j in range(0,self.sizecube)]
		self.othertemporal[t1][d1][d2] = value
	def drawOn(self,x,y,v=1.0,step_other=0.1):
		timespace = {}
		temps = 0 
		for ivi in np.arange(0,v,step_other):
			self.setother(x,y,temps,ivi)
			timespace[temps] = self.othertemporal
			temps+=1	
		self.set(x, y, temps, ivi)
		return timespace
	def copyDrawFromImage(self,filepath,jsonpath="out1.json"):
		f = open(jsonpath,'w')
		im = Image.open(filepath)
		im.resize((self.sizecube,self.sizecube))
		xs,ys = im.size
		for x in range(0,xs):
			for y in range(0,ys):
				print ((x/(1.0*xs))*100.0,"%  [",(y/(1.0*ys))*100.0,"%] - ",(((x+1)*(y+1)/(1.0*((1+xs)*(1+ys))))*100.0))
				a,b,c = im.getpixel((x,y))
				v = mean([a,b,c])#Grayscale mode
				f.write(json.dumps(self.drawOn(x,y,v))+"\n")
				timespace=""
		f.close()
	def printDrawFromJson(self,filepath="out.json"):
		f = open(filepath,'r')
		i=0
		timespace = json.loads(f.readline())
		for temps,data in timespace.items():
			i+=1
			for t in data.keys(): 
				print ((i/(len(timespace)*1.0))*100.0,"% :")
				print ("Write...: "+"generated-"+str(temps)+"_t_is_"+str(t)+".png")
				im = Image.new(mode="RGB",size=(self.sizecube,self.sizecube))
				for x in range(0,self.sizecube):
					for y in range(0,self.sizecube):
						im.putpixel((int(x),int(y)),(int(data[t][x][y]*255),int(data[t][x][y]*255),int(data[t][x][y]*255)))
				im.save("gen/generated-"+str(temps)+"_t_is_"+str(t)+".png")
				im.close()
		f.close()


""" TEST """
"""
#GENERATOR
print ("Creation de la dimension...")
ts = TimeSpace_2d4t(16)
print ("Copie de l'image dans l'espace temps...")
ts.copyDrawFromImage("pic.jpg")
"""

#DECODER
print ("Creation de la dimension...")
ts = TimeSpace_2d4t(16)
ts.printDrawFromJson()