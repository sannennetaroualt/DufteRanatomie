# Allgemeines zum Projekt DufteRanatomie
Ziel des Projekts ist eine Übersetzung des Anatomie-Decks [DopeRanatomy](https://old.reddit.com/r/medicalschoolanki/comments/gx128c/fully_tagged_dope_anatomy/) ins Deutsche.

Um das ganze für die Organisatoren möglichst reibungslos zu gestalten, wird der Inhalt über diese Github-Repository verwaltet. Das erlaubt es allen, die zum Projekt beitragen wollen parallel zueinander zu arbeiten, Änderungen des Decks genau zu dokumentieren und zwischenzuspeichern, falls man auf eine ältere Version downgraden möchte.

Alle können den Status ihrer Vorschläge jeder Zeit überprüfen. Weiterhin sollten mit diesem System regelmäßigere Releases möglich sein.

# Guidelines
## Allgemeines
Updates zum Deck umfassen zur Zeit:
* Übersetzung
* Rechtschreib-/Grammatikfehler
* Inhaltliche Fehler
* Wortwahl (bei Unklarheiten)

Einschränkungen:
* ! Der Inhalt des Originals soll keinesfalls verloren gehen!
* ! Das hinzufügen neuer Karten ist zur Zeit nicht vorgesehen.
* ! Bei Übersetzungen könnt ihr gerne auch neue, relevante Inhalte hinzufügen.
* ! Wenn du deinen Karten Medien (Bilder, Audio, etc.) hinzufügst, solltest du diese den Projektleitern zukommen lassen. Andernfalls sind diese in zukünftigen Deck-Releases nicht enthalten. Was Verwaltung von Medien angeht, werden wir uns nochmal was eleganteres überlegen.

## Schema der Übersetzung
Jedes Feld soll in der ersten Zeile den Alltagsnamen (bspw. "Linke Kammer") und in der Zweiten den Fachbegriff nach Terminologia Anatomica (bspw. "Ventriculus sinister"). Wenn es keinen Alltagsbegriff gibt, dann nur den Fachbegriff in einer Zeile.

Before:

```
  1a: 'Liver'
  ```
After:
```
  1a: 'Leber<br>Hepar'
  ```
(Hierbei ist <br> ein HTML-Tag für einen Zeilenumbruch.)

Gib bei einem Vorschlag als Quellenangabe wenn möglich entweder [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Main_Page), [TA](http://terminologia-anatomica.org/en/) oder [Amboss](https://www.amboss.com/de) an.

# Cheatsheet
1. Click auf den Errata-Button
2. Bearbeite die Karte
3. New Branch -> "Propose Changes"
4. Formular ausfüllen -> "Create Pull Request"

# Editor
Alle Karten des Dope-Ranatomy-Decks, die am oberen rechten Bildrand einen "Errata"-Button haben sind Teil dieses Collabs.
Ein Click auf diesen Button führt dich, wenn du in Github eingeloggt bist, zu einem Editor. Das ganze sollte Plattformunabhängig funktionieren.
Wenn du bei Click auf den Errata-Button einen 404-Fehler bekommst, bearbeitest du höchstwahrscheinlich eine Karte, die nicht Teil des Decks ist.

Du kannst auch manuell nach einer Karte suchen, indem du im Suchfenster die Note ID der Karte einfügst. Der Inhalt jeder Karte ist in einer .yaml Textdatei gespeichert, die nach der Note ID benannt ist.

## Bearbeiten einer Karte
<p align="center"><kbd><img width="800" alt="Screenshot 2021-06-29 at 15 18 47" src="https://user-images.githubusercontent.com/85392967/123748307-02c23f00-d8ef-11eb-9137-f7c8ab85eafd.png"></kbd></p>

Im Editor siehst du Inhalte der Felder im Format:
```
  Feldname1: 'Inhalt des <b>ersten Flelds</b> mit HTML-Tags'
  Feldname2: 'Inhalt des zweiten Felds'
  ```
... wobei die Elemente in eckigen Klammern Textformattinerung im HTML-Format darstellen. (In diesem Fall, <b>fett</b> = **fett**).

Damit Formattierung (**fett**, _kursiv_, Zeilenumbrüche, etc.) nicht verloren gehen, musst du den Text als HTML aus dem Anki-Editor kopieren, und in die Gänsefüßchen des betreffenden Feldes eintragen:
```
  Feldname1: 'Inhalt des <b>ersten Felds</b> mit HTML-Tags'
  Feldname2: 'Inhalt des zweiten Felds'
  ```

### HTML-Quelltext aus Anki-Desktop
Hierfür musst du den Anki-Editor (Taste E beim reviewen) öffnen und auf den Sandwichbutton clicken:

<p align="center"><img width="800" alt="Screenshot 2021-06-29 at 15 30 17" src="https://user-images.githubusercontent.com/85392967/123748735-909e2a00-d8ef-11eb-9dad-c65a37e429a7.png"></p>

Wähle hier den Reiter "Edit HTML" und kopiere den Inhalt des sich öffnenden Fensters:

<p align="center"><img width="800" alt="Screenshot 2021-06-29 at 15 37 57" src="https://user-images.githubusercontent.com/85392967/123749127-0b674500-d8f0-11eb-86ab-a72571ab1704.png"></p>

### HTML-Quelltext aus Anki-iOS
Hier geht das etwas einfacher.
Du kannst im Editor durch Click auf den "</>"-Button zwischen HTML und Normalansicht wechseln.

<p align="center" float="left"><kbd>
  <img src="https://user-images.githubusercontent.com/85392967/123753766-2ab4a100-d8f5-11eb-8f63-f9670638ec59.jpeg" width="350" />
  <img src="https://user-images.githubusercontent.com/85392967/123753916-4cae2380-d8f5-11eb-8c41-1e3cb9c19f0e.jpeg" width="350" />
  </kbd></p>

## Tags
Bei Tags brauchst du dir keine Gedanken um Formattierung machen. Diese haben keine HTML-Tags.
Tags sind aufgeteilt in einen Tag pro Zeile im Format:
```
  - 'Parent::Child::Leberkas'
  ```
Um neue Tags hinzuzufügen, könnt ihr einfach eine neue Zeile nach dem selben Schema hinzufügen.

# Einreichen der Änderung
Wenn du zum Ende der Seite scrollst, kannst du die Änderung einreichen. Im unteren Beispiel habe ich einen neuen Tag hinzugefügt.
Wähle die Option "New Branch" und clicke anschließend auf Propose Changes. Du brauchst die anderen Felder nicht zu bearbeiten.

<p align="center"><kbd><img width="800" alt="Screenshot 2021-06-29 at 16 01 44" src="https://user-images.githubusercontent.com/85392967/123752482-c80ed580-d8f3-11eb-8b84-8d02345f4bc6.png"></kbd></p>

Im nächsten Bildschirm ist ein Formular, in dem du deinen Vorschlag kategorisieren, Quellen hinzufügen oder eine kurze Erklärung einfügen kannst.

<p align="center"><kbd><img width="800" alt="Screenshot 2021-06-29 at 16 03 58" src="https://user-images.githubusercontent.com/85392967/123752773-19b76000-d8f4-11eb-8566-37f7eda42469.png"></kbd></p>

Wenn du das ganze einreichst, sieht das ganze für uns so aus:

<p align="center"><kbd><img width="800" alt="Screenshot 2021-06-29 at 16 08 01" src="https://user-images.githubusercontent.com/85392967/123753256-9b0ef280-d8f4-11eb-9f4f-116922fe45ce.png"></kbd></p>

Das wars dann auch schon!
