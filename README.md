# DufteRanatomie

## Guidelines
Updates zum Deck umfassen zur Zeit:
* Übersetzung
* Rechtschreib-/Grammatikfehler
* Inhaltliche Fehler
* Wortwahl (bei Unklarheiten)

Das hinzufügen neuer Karten ist nicht vorgesehen. Bei Übersetzungen könnt ihr gerne neue, relevante Inhalte hinzufügen. Der Inhalt des Originals soll keinesfalls verloren gehen!

## Editor
Alle Karten des Dope-Ranatomy-Decks, die am oberen rechten Bildrand einen "Errata"-Button haben sind Teil dieses Collabs.
Ein Click auf diesen Button führt dich zu einem Editor. Das ganze sollte Plattformunabhängig funktionieren.
Wenn du bei Click auf den Errata-Button einen 404-Fehler bekommst, bist du nicht in Github eingeloggt, oder bearbeitest eine Karte, die nicht Teil des Decks ist.

### Bearbeiten einer Karte
<img width="800" alt="Screenshot 2021-06-29 at 15 18 47" src="https://user-images.githubusercontent.com/85392967/123748307-02c23f00-d8ef-11eb-9137-f7c8ab85eafd.png">

Im Editor siehst du Inhalte der Felder im Format:
```
  Feldname: 'Inhalt des <b>Flelds</b> mit HTML-Tags'
  ```
... wobei die Elemente in eckigen Klammern Textformattinerung im HTML-Format darstellen. (In diesem Fall, <b>fett</b> = **fett**).

Damit Formattierung (**fett**, _kursiv_, Zeilenumbrüche, etc.) nicht verloren gehen, musst du den Text als HTML aus dem Anki-Editor kopieren, und in die Gänsefüßchen des betreffenden Feldes eintragen:
```
  Feldname: 'Inhalt des <b>Felds</b> mit HTML-Tags'
  ```

#### HTML-Quelltext aus Anki-Desktop
Hierfür musst du den Anki-Editor (Taste E beim reviewen) öffnen und auf den Sandwichbutton clicken:

<img width="800" alt="Screenshot 2021-06-29 at 15 30 17" src="https://user-images.githubusercontent.com/85392967/123748735-909e2a00-d8ef-11eb-9dad-c65a37e429a7.png">

Wähle hier den Reiter "Edit HTML" und kopiere den Inhalt des sich öffnenden Fensters:

<img width="800" alt="Screenshot 2021-06-29 at 15 37 57" src="https://user-images.githubusercontent.com/85392967/123749127-0b674500-d8f0-11eb-86ab-a72571ab1704.png">

#### HTML-Quelltext aus Anki-iOS
Hier geht das etwas einfacher.
Du kannst im Editor durch Click auf den "</>"-Button zwischen HTML und Normalansicht wechseln.

Text         |  HTML
:-------------------------:|:-------------------------:
![IMG_7895](https://user-images.githubusercontent.com/85392967/123753766-2ab4a100-d8f5-11eb-8f63-f9670638ec59.jpeg)  |  ![IMG_7896](https://user-images.githubusercontent.com/85392967/123753916-4cae2380-d8f5-11eb-8c41-1e3cb9c19f0e.jpeg)


### Tags
Bei Tags brauchst du dir keine Gedanken um Formattierung machen. Diese haben keine HTML-Tags.
Tags sind aufgeteilt in einen Tag pro Zeile im Format:
```
  - 'Parent::Child::Leberkas'
  ```
Um neue Tags hinzuzufügen, könnt ihr einfach eine neue Zeile nach dem selben Schema hinzufügen.

## Einreichen der Änderung
Wenn du zum Ende der Seite scrollst, kannst du die Änderung einreichen. Im unteren Beispiel habe ich einen neuen Tag hinzugefügt.
Wähle die Option "New Branch" und clicke anschließend auf Propose Changes. Du brauchst die anderen Felder nicht zu bearbeiten.

<img width="800" alt="Screenshot 2021-06-29 at 16 01 44" src="https://user-images.githubusercontent.com/85392967/123752482-c80ed580-d8f3-11eb-8b84-8d02345f4bc6.png">

Im nächsten Bildschirm ist ein Formular, in dem du deinen Vorschlag kategorisieren, Quellen hinzufügen oder eine kurze Erklärung einfügen kannst.

<img width="800" alt="Screenshot 2021-06-29 at 16 03 58" src="https://user-images.githubusercontent.com/85392967/123752773-19b76000-d8f4-11eb-8566-37f7eda42469.png">

Wenn du das ganze einreichst, sieht das ganze für uns so aus:

<img width="800" alt="Screenshot 2021-06-29 at 16 08 01" src="https://user-images.githubusercontent.com/85392967/123753256-9b0ef280-d8f4-11eb-9f4f-116922fe45ce.png">

Das wars dann auch schon!
