#!/usr/bin/env python
# -*- coding: utf-8
#
# The python challenge 1
# WebSite : http://www.pythonchallenge.com/pc/def/map.html
# Translate this string follow rule [k -> M , O -> Q, E->G ]
# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
# 
# alpha  = a  ,b  ,c  ,d  ,e  ,f  ,g  ,h  ,i  ,j  ,k  ,l  ,m  ,n  ,o  ,p  ,q  ,r  ,s  ,t  ,u  ,v  ,w  ,x  ,y  ,z  
# ASCII  = 97 ,98 ,99 ,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122
#
# String need to be translated
string =r"g fmnc wms bgblr rpylqjyrc gr zw fylb.rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# create alpha map dictionary
#alpha_dic = {}
#for i in range(97,123):
#	if i < 121:
#		count = i + 2
#	else:
#		count = i - 24
#	char = chr(i)
#	alpha_dic[char] = count
#
#
# translation string
newstring = ""
for s in string:
	if s >="a" and s <="x":
		newstring += chr(ord(s) + 2)
	elif s >="y" and s <= "z":
		newstring += chr(ord(s) - 24)
	else:
		newstring += s

#print alpha_dic
print newstring

#http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans
intab = ""
for i in range(97,123):
	char = chr(i)
	intab += char

outtab = ""
for o in range(97,123):
	if o < 121:
		count = o + 2
		outtab +=chr(count)
	else:
		count = o - 24
		outtab +=chr(count)

url_str = "map"
trans = maketrans(intab,outtab)
print "Next challenge go to http://www.pythonchallenge.com/pc/def/%s.html" % (url_str.translate(trans))


