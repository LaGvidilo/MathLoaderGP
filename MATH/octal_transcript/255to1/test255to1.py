#coding: utf-8

import gplearn.GP as gp


program = gp.GP_SymReg()
program.load(filepath="255to1.model")
for i in range(0,256):
	print(program.predict([i*1.0]))


"""
255 to 1 is the model


and 1 to 255:
	round(255*x)

because: 255*0.00391 == 1
"""