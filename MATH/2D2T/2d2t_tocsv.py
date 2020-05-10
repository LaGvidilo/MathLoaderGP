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
		self.temps=0
		self.csvfile = open("2d2t.csv","w")
		self.csvfilet1 = open("2d2t_t1.csv","w")
		self.csvfilet0 = open("2d2t_t0.csv","w")
	def drawOn(self,x,y,v=1.0,step_other=0.5,redim=None):
		for ivi in np.arange(0,v+0.1,step_other):
			self.csvfile.write(",".join(map(str,[self.temps,x,y,ivi,v]))+"\n")
			self.csvfilet1.write(",".join(map(str,[self.temps,x,y,ivi]))+"\n")
			self.temps+=1
		self.csvfilet0.write(",".join(map(str,[self.temps,x,y,v]))+"\n")
		self.temps+=1
	def copyDrawFromImage(self,filepath,redim=None):
		im = Image.open(filepath)
		im.resize((self.sizecube,self.sizecube))
		xs,ys = im.size
		for x in range(0,xs):
			for y in range(0,ys):
				print ((x/(1.0*xs))*100.0,"%  [",(y/(1.0*ys))*100.0,"%] - ",(((x+1)*(y+1)/(1.0*((1+xs)*(1+ys))))*100.0))
				a,b,c = im.getpixel((x,y))
				v = mean([a,b,c])
				self.drawOn(x,y,v,redim=redim)


""" TEST """

#GENERATOR
print ("Creation de la dimension...")
ts = TimeSpace_2d4t(256)
print ("Copie de l'image dans l'espace temps...")
ts.copyDrawFromImage("IMG1.jpg",redim=None)
