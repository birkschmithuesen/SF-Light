# Einrichtung der Spikies

(Version Frankfurt Okt22 von h\*ns)

## Intro

In diesem Dokument geht es um die Einrichtung und Kalibrierung der Spikies der Show SystemFailed.

Um die bewegten Scheinwerfer im Chamsys mit der automatisierten Positionierung (Ausrichtung) auf xyz-Koordinaten (zB Tracker) nutzen zu können, müssen sie dort im Patch mit den 6 Werten x,y,z und rotX, rotY und rotZ korrekt ausgestattet werden.

Die 16 Scheinwerfer hängen gleichverteilt an zwei Trussen ausserhalb der Längsseiten des Spielfeldes.
Die ideale Höhe der Trussen hängt von der Spielfeldbreite ab. Die Linsen der Scheinwerfer sollten nicht tiefer kommen als die Hälfte und nicht höher als etwa 60% der Breite.

## Chamsys Info

* (PATCH->VIEW VIS): Attach Objects "Truss 1" und "Truss 2" sind für die Trussen zuständig, für jeden Spikie gibt es wiederum ein weiteres Attach Object "spikieX". Unter Vis Heads sind die Spikies dann daran angehängt
  * die Positionen werden bei den Attach Objects eingestellt, die Rotationen an den vis Heads
* !!! Bei Chamsys ist die y-Achse die Höhe (die idR „z“ genannt“ wird, z wiederum ist die negative y-Achse) !!!
* Tracker Setup ist hier: MACRO -> VIEW AUTOM -> VIEW TRACKERS
* Zur korrekten Berechnung der Pan/Tilt-Werte müssen die y Pos der Scheinwerfer 10cm unter Trusshöhe liegen

## Geräte hängen

Die Scheinwerfer werden an jeder Truss gleichverteilt aufgehängt. Das erste und letzte Gerät sollte etwa 20 bis 40 cm in Längsrichtung ausserhalb des Spielfeldes positioniert sein. (Die Azors unten im Idealfall genau drunter.)
_Mögliches Vorgehen: Spielfeldlänge durch 7 teilen, aufrunden auf "handhabbares Mass" und checken, ob Gesamtlänge im Bereich Spielfeldlänge + 40...80cm._
Die exakten Positionen kollidieren oft mit den Trussbraces und -Verbindern. Einfach nächstbeste Position wählen und später im Patch korrigieren.

## Positionen einmessen

* die Trusshöhe wird gemessen und im MagicQ-Vis Patch bei den **Attach Objects** eingetragen:
  
  * Trusshöhe bei den Objekten "Truss1" und "Truss2" als Y Pos 
  * ggf. z Rot einstellen, falls die Truss nicht exakt parallel zum Boden hängt

* die tatsächlichen Positionen der Spikies werden mit Kreuzlinienlaser gelotet und am Boden markiert und so exakt wie möglich vermessen

* Positionen im MagicQ-Vis Patch bei den **Attach Objects** eingetragen: (für diese Abhandlung gehe ich davon aus, dass die beiden Spike-Trussen in x-Richtung verlaufen, also zB Truss1: z=0m, x=0m...16m, y=5,4m und Truss2: z=-9m, x=0m...16m, y=5,4m)  
  
  * x- und y-Werte der Spikiepositionen bei den Einzeltrussen "spikieX" als x Pos und -1 mal z Pos. 
  * known bug: bei Änderung der x-, y- und z-Werte werden diese zwar im Visualizer direkt übernommen; um die Änderung aber auch in der Berechnung der pan/tilt-Werte berücksichtigt zu bekommen, muss einmal ENTER gedrückt werden, während der Cursor irgendwo in der ersten Spalte der Tabelle steht

* Positionen auch in die TD-config-Tabelle spikie_pos.tsv eintragen, damit die Abstände und damit Zoom-Stufen korrekt berechnet werden können

* Dabei gleich alle Rot der Vis Heads resetten.

* Die Attach Objects bot1...bot16 sollten nun auch die richtigen x und z Pos haben. y Pos manuell auf 0 setzen.

## Fernsteuerung

Um die folgende Kalibrierung zügig zu machen, am besten das Lichtpult fernsteuern. Entweder per Chamsys-Netzwerk-Session oder anyDesk nutzen zur Fernsteuerung des Lichtrechners.

## Tilt-Offset

Da die Movingheads immer so nen kleinen Schuss weg haben: Zum Justieren der Tilt-Mittelstellung alle MH auf Position center und per panctrl-channel langsam rotieren lassen und den Tilt Offset TO (patch - view heads) so einstellen, dass der Mittelpunkt stimmt (der Lichtpunkt dreht sich in sich dann ohne eiern).
Zur Annäherung an den korrekten Wert zunächst das Vorzeichen ermitteln: grosse Werte (zB 2°/-2°) eingeben und schauen ob sich das Eiern in die selbe Richtung verstärkt oder in die andere Richtung umschlägt. Das Vorzeichen mit Richtungsänderung ist zu verwenden.
Dort in 0.1-Schritten angleichen bis minimales eiern erreicht ist.
(Schade: In der Tabelle sehen wir keine Nachkommastellen, sie werden aber berücksichtigt.)

## Hardware justieren

Alle Spikies nun in Position center stellen und am Gerät/Haken bestmöglich ausrichten.
(dieser Punkt könnte wahrscheinlich auch weggelassen werden und komplett per vis-patch-Korrekturen bzw Position-Paletten gemacht werden)

## Z Rot und X Rot

_x Rot = Drehung um die Längsrichtung der Truss_
_z Rot = Drehung "gegen den Haken", also die Richtung, die sich am Scheinwerfer/Haken NICHT einstellen lässt_

* spikies per Position Palette auf die jeweils darunterliegende Markierung "botX" positionieren 
* mit Angleichung von z Rot und x Rot beim jeweilige Vis Head zentrieren.

## Y Rot

_Drehung um die senkrechte Achse (wie Scheinwerfer-Pan)_

* spikie auf Positions Palette der Markierung gegenüber ("botX") richten 
* die Abweichung in Längsrichtung (x-Richtung) des Spielfeldes mit y Rot vom Vis Head angleichen. 
* x Rot darf auch nochmal nachgestellt werden... (Dann natürlich checken, was bei senkrechter Positionierung passiert)
