#coding: utf-8
import numpy as np

f  = open("1to255.csv", "w")
f.write("x0,y\n")
print (len(np.arange(0,1,0.00391))," IS LEN OF SAMPLE.")
y=0
for i in np.arange(0,1,0.00391):
	print (i*100.0,"%")
	f.write(str(i)+","+str(y)+"\n")
	y+=1
f.close()