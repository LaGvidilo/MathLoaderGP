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
		self.img_t1 = Image.new(mode="RGB",size=(self.sizecube,self.sizecube))
		self.img_t0 = Image.new(mode="RGB",size=(self.sizecube,self.sizecube))
		self.temps=0
	def set(self,d1,d2,value):
		self.img_t0.putpixel((d1,d2),(int(value),int(value),int(value)))
	def setother(self,d1,d2,value):
		self.img_t1.putpixel((d1,d2),(int(value),int(value),int(value)))
	def drawOn(self,x,y,v=1.0,step_other=0.5,redim=None):
		for ivi in np.arange(0,v+0.1,step_other):
			self.setother(x,y,ivi)
			if redim!=None:
				imcopy = deepcopy(self.img_t0)
				imcopy.resize(redim)
				imcopy.save("gen1/"+"img_"+str(int(ivi))+"_"+str(self.temps)+".png")
			else:
				self.img_t1.save("gen1/"+"img_"+str(int(ivi))+"_"+str(self.temps)+".png")
			self.temps+=1
		self.set(x, y, v)
		if redim!=None:
			imcopy = deepcopy(self.img_t0)
			imcopy.resize(redim)
			imcopy.save("gen0/"+"img_"+str(self.temps)+".png")
		else:
			self.img_t0.save("gen0/"+"img_"+str(self.temps)+".png")
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
