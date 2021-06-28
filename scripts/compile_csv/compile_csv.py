import yaml
import os
import sys
import io
import glob
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Compile the cards into a CSV file.')
parser.add_argument("--card_dir", metavar="path", required=True, type=str, help="The directory with the YAML files. It will be processed recursively.")
parser.add_argument("--output", metavar="path", required=True, type=str, help="Path to the output file.")
parser.add_argument("--delimiter", metavar="char", type=str, default="	", help="The delimiter to use in the CSV file (default: tab character).")
parser.add_argument("--schema", metavar="path", type=str, default="0", help="Path to the card schema. If supplied, the script will print the CSV header (field names).")

args = parser.parse_args()

cardDir = args.card_dir
filePath = args.output

if args.schema != "":
	schema = eval(io.open(args.schema, mode="r", encoding="utf-8").read())
	header = []
	for val in schema:
		header.append(schema[val]["meta"]["fieldName"])
	with io.open(filePath, mode="a", encoding="utf-8") as csvFile:
		csvFile.write((args.delimiter).join(header) + '\n')

# cards = list(glob.iglob(cardDir + '**/*.yaml', recursive=True))
cards = list(glob.iglob(cardDir + '*.yaml', recursive=True))

for cardFile in tqdm(cards, desc="Compiling", unit="cards"):
	with io.open(cardFile, mode="r", encoding="utf-8") as stream:
		card = yaml.safe_load(stream)
	
	tags = ' '.join(card["tags"])
	card.pop("tags")

	csvLine = ""
	for field, val in card.items():
		csvLine += '"'+val.replace('"', '""')+'"'+args.delimiter
	csvLine += tags.replace('"', '""')

	with io.open(filePath, mode="a", encoding="utf-8") as csvFile:
		csvFile.write(csvLine + '\n')
