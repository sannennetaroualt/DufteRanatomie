#!/bin/bash
cp data-csv/data.csv ../../brainbrew/src/data/data.csv
rm ../../brainbrew/src/data/DopeRanatomy-Anatomy.csv
mv ../../brainbrew/src/data/data.csv ../../brainbrew/src/data/DopeRanatomy-Anatomy.csv

cd ../../brainbrew

brainbrew run recipes/source_to_anki.yaml

rm ../DufteRanatomie.json
cp build/DopeRanatomy/deck.json ../DufteRanatomie.json
