#!/bin/bash
cd ../../brainbrew
brainbrew init ../scripts/import_deck/DopeRanatomy
brainbrew run recipes/source_to_anki.yaml

cd ../scripts/parsers
pwsh anatomie.ps1
