import yaml
import io
import sys
import glob
from cerberus import Validator
from tqdm import tqdm

cardDir = sys.argv[1]
schema = sys.argv[2]

schema = eval(io.open(schema, mode="r", encoding="utf-8").read())
v = Validator(schema)

failed = 0
errors = {}

cards = list(glob.iglob(cardDir + '**/*.yaml', recursive=True))

for cardFile in tqdm(cards, desc="Validating", unit="cards"):
	with io.open(cardFile, mode="r", encoding="utf-8") as stream:
		card = yaml.safe_load(stream)
	if not v.validate(card, schema):
		failed += 1
		errors[cardFile] = str(v.errors)

if failed == 0:
	print("Success. Validated "+str(len(cards))+" cards.")
else:
	for card, error in errors.items():
		print("Validation for card "+card+" failed. Fix the following:")
		print(error+"\n")
	sys.exit("Validation failed. "+str(failed)+" cards had issues, check the log to see the details.")