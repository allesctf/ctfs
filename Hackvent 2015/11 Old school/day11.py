#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

mapping = { '000000': ' ', 
'000001': '1', 
'000010': '2', 
'000011': '3', 
'000100': '4', 
'000101': '5', 
'000110': '6', 
'000111': '7', 
'001000': '8', 
'001001': '9', 
'001010': ':', 
'001011': '#', 
'001100': '@', 
'001101': '\'', 
'001110': '=', 
'001111': '"', 
'010000': '0', 
'010001': '/', 
'010010': 'S', 
'010011': 'T', 
'010100': 'U', 
'010101': 'V', 
'010110': 'W', 
'010111': 'X', 
'011000': 'Y', 
'011001': 'Z', 
'011010': '&', 
'011011': ',', 
'011100': '%', 
'011101': '_', 
'011110': '>', 
'011111': '?', 
'100000': '-', 
'100001': 'J', 
'100010': 'K', 
'100011': 'L', 
'100100': 'M', 
'100101': 'N', 
'100110': 'O', 
'100111': 'P', 
'101000': 'Q', 
'101001': 'R', 
'101010': '!', 
'101011': '$', 
'101100': '*', 
'101101': ')', 
'101110': ';', 
'101111': '�', 
'110000': '', 
'110001': 'A', 
'110010': 'B', 
'110011': 'C', 
'110100': 'D', 
'110101': 'E', 
'110110': 'F', 
'110111': 'G', 
'111000': 'H', 
'111001': 'I', 
'111010': '�', 
'111011': '.', 
'111100': '<', 
'111101': '(', 
'111110': '+', 
'111111': '|' }

cols = (77,95,114,130,148,165,183,200,217,235,252,270,287,304,321,340,357,374,391,409,427,444,460,479,495,513,532,547,565,582)
rows1 = (182,199,217,234,252,269)
rows2 = (288,305,323,339,356,373)
rows3 = (390,408,427,444,462,478)

line1 = ''
line2 = ''
line3 = ''

img = Image.open('PunchCard_11.png', 'r')

for x in cols:
	col = ''
	for y in rows1:
		(r,g,b,a) = img.getpixel((x,y))
		if a==255:
			col += '0'
		else:
			col += '1'
	line1 += mapping[col]
print line1

for x in cols:
	col = ''
	for y in rows2:
		(r,g,b,a) = img.getpixel((x,y))
		if a==255:
			col += '0'
		else:
			col += '1'
	line2 += mapping[col]
print line2

for x in cols:
	col = ''
	for y in rows3:
		(r,g,b,a) = img.getpixel((x,y))
		if a==255:
			col += '0'
		else:
			col += '1'
	line3 += mapping[col]
print line3

print '\n' + line2[:4].upper() + '-' + line2[5:9].lower() + '-' + line2[10:14].upper() + '-' + line2[15:19].lower() + '-' + line2[20:24].upper() + '-' + line2[25:].lower()