#coding: utf-8


import gplearn.GP as GP
import json

""" CODE DE LOADING DU JSON """
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
	assert isinstance(x, str)
	return x


def from_none(x: Any) -> Any:
	assert x is None
	return x


def from_union(fs, x):
	for f in fs:
		try:
			return f(x)
		except:
			pass
	assert False


def from_int(x: Any) -> int:
	assert isinstance(x, int) and not isinstance(x, bool)
	return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
	assert isinstance(x, list)
	return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
	assert isinstance(x, c)
	return cast(Any, x).to_dict()


@dataclass
class WelcomeElement:
	path: Optional[str] = None
	name: Optional[str] = None
	number_x: Optional[int] = None
	number_y: Optional[int] = None
	model_path: Optional[str] = None
	loader_path: Optional[str] = None

	@staticmethod
	def from_dict(obj: Any) -> 'WelcomeElement':
		assert isinstance(obj, dict)
		path = from_union([from_str, from_none], obj.get("path"))
		name = from_union([from_str, from_none], obj.get("name"))
		number_x = from_union([from_int, from_none], obj.get("number_x"))
		number_y = from_union([from_int, from_none], obj.get("number_y"))
		model_path = from_union([from_str, from_none], obj.get("model_path"))
		loader_path = from_union([from_str, from_none], obj.get("loader_path"))
		return WelcomeElement(path, name, number_x, number_y, model_path, loader_path)

	def to_dict(self) -> dict:
		result: dict = {}
		result["path"] = from_union([from_str, from_none], self.path)
		result["name"] = from_union([from_str, from_none], self.name)
		result["number_x"] = from_union([from_int, from_none], self.number_x)
		result["number_y"] = from_union([from_int, from_none], self.number_y)
		result["model_path"] = from_union([from_str, from_none], self.model_path)
		result["loader_path"] = from_union([from_str, from_none], self.loader_path)
		return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
	return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
	return from_list(lambda x: to_class(WelcomeElement, x), x)


""" FIN DE DEP LOADING DU JSON """

def readFile(filepath):
	f = open(filepath, 'r')
	data = f.read()
	f.close()
	return data

result = welcome_from_dict(json.loads(readFile("index_MATH.json")))
libslist={}
print ("LOAD MATHS MODULES...")
for i in result:
	print (i.to_dict()["name"],i.to_dict()["model_path"], "LOAD...")
	libslist[i.to_dict()["name"]] = GP.GP_SymReg()
	libslist[i.to_dict()["name"]].load(i.to_dict()["model_path"])
print("Done.")


def special_function(name,args=[]):
	return libslist[name].predict(args)
	
"""
#Exemple 255to1	
print (special_function("255to1",[128]))

#Exemple divfactuniv_RFP


#Exemple nzabs
print (special_function("nzabs",[0]))
print (special_function("nzabs",[-58]))
print (special_function("nzabs",[42]))

#Exemple pos-flat-convertor


#Exemple rules_models


#Exemple warplumiere

 
"""