Bevor mit Kalibrierung gestartet werden kann, MQ settings kontrollieren:

Damit tracker empfangen werden müssen folgende Einstellungen aktiviert sein:

SETUP -> View Settings -> Network

Zeilen

OSC mode: Tx and Rx

Tracker rx: MQ Track

# Kalibrierung der Scheinwerferpositionen \\

(von h\*ns in Lindenfels Aug21)

Um die bewegten Scheinwerfer im Chamsys mit der automatisierten Positionierung (Ausrichtung) auf xyz-Koordinaten (zB Tracker) nutzen zu können, müssen sie dort im Patch mit den 6 Werten x,y,z und rotX, rotY und rotZ ausgestattet werden.

## Chamsys Info

* (PATCH->VIEW VIS): Attach Objects ist für die Trussen zuständig, unter Vis Heads sind die MH angehängt
* !!! Bei Chamsys ist die y-Achse die Höhe (die idR „z“ genannt“ wird, z wiederum ist die negative y-Achse) !!!
* Tracker Setup ist hier: MACRO -> VIEW AUTOM -> VIEW TRACKERS
* scheinwerfer 5cm unter truss
* scheinwerfer in MQ an Truss attached

## Hardware anbringen

* Scheinwerfer gleichmäßig auf dem Rig verteilen
  * erster und letzter Spickie hängen über den Atzors (30cm außerhalb der Spielfeld Kante)
* Scheinwerferposition so exakt wie möglich ausmessen (für diese Abhandlung gehe ich davon aus, dass die beiden Spike-Trussen in x-Richtung verlaufen, also zB Truss1: z=0m, x=0m...16m, y=5,4m und Truss2: z=-9m, x=0m...16m, y=5,4m)\
  (cm-Genauigkeit verwenden - mm-Genauigkeit ist in der magicq-Tabelle nicht sichtbar)

## Vorgehensweise zur Kalibrierung der 6 Werte

### Truss Höhe eingeben

Menü: PATCH->VIEW VIS->Attach Objects

* Truss 1 (Spielfeld Koordinatensystem: oben / FOH Sichtachse: links)
  * Höhe vom Boden bis Truss Unterkante messen und bei Y Pos eintragen (in Meter)
  * ggf. Z Rot einstellen, falls die Truss nicht exakt parallel zum Boden hängt
* Truss 2 (Spielfeld Koordinatensystem: unten / FOH Sichtachse: rechts)
  * Höhe vom Boden bis Truss Unterkante messen und bei Y Pos eintragen (in Meter)
  * ggf. Z Rot einstellen, falls die Truss nicht exakt parallel zum Boden hängt

### ~~LightCalib Tool verwenden~~

* ~~gemessene Positionen in einer Tabelle ablegen~~
* ~~(gelotete/gelaserte) Markierungen der Scheinwerfer-Positionen am Boden vornehmen~~
* ~~mit lightcalib-Touchdesigner-Patch Tracker für alle dieser Positionen und die Mitte des Feldes anlegen~~
  * ~~Viewer Window über rechtsclick "View as Perform Window" öffnen~~
  * ~~gemessene Positionen der Movingheads in trackers.tsv übernehmen~~
  * ~~trackers.tsv wird im lightcalib Tool geladen (irgendwie müssen halt die Positionen in die Tabelle)~~
  * ~~Port: 6549~~

## Woher kommen welche Werte und wohin damit?

### X Pos und Z Pos

* x und z gegen die 0,0-Ecke des Spielfeldes messen und in MagiQ übertragen VIEW VIS -> Vis Heads: X Pos, Z Pos
  * known bug: bei Änderung der x-, y- und z-Werte werden diese zwar im Visualizer direkt übernommen; um die Änderung aber auch in der Berechnung der pan/tilt-Werte berücksichtigt zu bekommen, muss einmal ENTER gedrückt werden, während der Cursor irgendwo in der ersten Spalte der Tabelle steht

## Tilt Offset

Da die Movingheads immer so nen kleinen Schuss weg haben: Zum Einstellen alle MH langsam rotieren lassen und den Tilt Offset (patch - view heads) so einstellen, dass der Mittelpunkt stimmt

## X Rot

* sollte 0 sein, da am Anfang der Scheinwerfer am Haken händisch PERFEKT auf die Markierung ausgerichtet wurde!
* ansonsten per X Rot auf senkrecht drunter liegenden Punkt

### Z Rot

* Head auf pan/tilt="centre" positionieren und reales Scheinwerfergehäuse oben an der Truss von Leiter/Genie/Truss bestmöglichst zur Markierung ausrichten (um das Rohr drehen UND Scheinwerfer um den Haken, so dass parallel zum Truss)
  * es wurde beobachtet, dass die Lotrechtheit beim Festziehen des C-Hakens verlorengeht
  * entweder einseitig etwas drunter klemmen -> Z Rot = 0,
  * oder diese Drehung im Patch ausgleichen (wenn auf drunterliegenden Tracker positioniert) PATCH->VIEW VIS->Vis Heads-> Z Rot (keine anderen Werte anfassen!)

### Y Pos und Y Rot

* Y Pos per reales Truss-Unterkanten-maß in Attach Objects setzen (evtl. auch eine Z Rot für die Truss, wenn sie nicht waagerecht hängt)
* Head auf gegenüberliegenden Tracker positionieren
* Abweichung in x-Richtung mit dem Y Rot-Wert ausgleichen
* Abweichung des realen Spots von der Markierung in z-Richtung mit dem y Pos-Wert ausgleichen (ENTER DRÜCKEN IN 1.SPALTE oder VISUALIZER OFFEN HABEN!!!) (der funktionierende Wert entspricht dem Hängepunkt am Scheinwerfer - ohne Haken - 5cm unter Truss. Kommentar: vielleicht ist es aber auch der Rotationsmittelpunkt)

### 

---

## Known BUGS

Anmerkung zur Arbeit an Max’ MQ80:

* bei Änderunger der Rotationen, werden diese direkt im Visualizer und auch bei der Berechnung der pan/tilt-Werte berücksichtigt
* die pan/tilt-Berechnung kommt auch nicht damit klar, dass andere Objekte (als die Tracker) bewegt werden. Die Berechnung funktioniert leider NICHT für bewegte Scheinwerfer (an bewegten Trussen gehängt) und für auf bewegte MagicVis-Objekte fokussierte Scheinwerfer