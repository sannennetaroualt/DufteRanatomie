# Deckmanagement
### In diesem Dokument halte ich fest, wie ich das Deck im- bzw. exportiere.

Der Import- und Exportprozess basiert auf [Brainbrew](https://github.com/ohare93/brain-brew) und [CrowdAnki](https://github.com/Stvad/CrowdAnki).
Die Skripte wurden in PowerShell, Python und bash geschrieben.

## Import
1. Deck via CrowdAnki exportieren.
2. Durch Export generierten Ordner in scripts/import_deck bewegen
3. `sh import.sh`

## Compile CSV
1. Über Github-Actions auf "run workflow".
2. Inhalt der exportierten data.zip in scripts/patch_deck bewegen
3. `sh patch.sh`
