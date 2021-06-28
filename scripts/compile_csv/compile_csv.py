import yaml
import os
import sys
import io
import glob

cardDir = sys.argv[1]
filePath = sys.argv[2]

for cardFile in glob.iglob(cardDir + '**/*.yaml', recursive=True):
	with io.open(cardFile, mode="r", encoding="utf-8") as stream:
		card = yaml.safe_load(stream)
	print ("Processing "+card["noteid"]+"...", end='\r')
	
	tags = ' '.join(card["tags"])
	card.pop("tags")

	csvLine = ""
	for field, val in card.items():
		csvLine += val+','
	csvLine += tags

	with io.open(filePath, mode="a", encoding="utf-8") as csvFile:
		csvFile.write(csvLine + '\n')
