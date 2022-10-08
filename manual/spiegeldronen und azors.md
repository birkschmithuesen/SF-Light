1. höhe festlegen und kegelwinkel bestimmen,
2. kegelwinkel anhand von abstand von spiegel und blech einstellen (eventuell Zeichnung einfügen)
3. vier mal zwei Hängepunkte pro drohne schaffen, 1-2 meter vor und hinter position der azor
4. azor-positionen fixieren (möglichst unter spikie)
5. kreuzlaser so einrichten, dass er genau unter dem punkt steht, wo drohne hängen soll (unterster punkt vom gestell auf kreuz-laser - selbe achse wie mitte azor (ca. 25cm außerhalb des spielfeldrands)
6. drohne hängen, die vier hängepunkte des oberen punkts einhängen, höhe mit disto-laser am untersten punkt des gestells abmessen - gucken, dass alle federn der kegel-spiegel voll ausgefahren sind
7. an den vier unteren hängepunkten drohne mit hilfe von wasserwaage gerade richten
8. azor neben drohne auf diese richten (position: spine0, beam: azor beam)
   1. für position spine0 die azor so ausrichten, dass beams genau in die jeweiligen spiegeldreiecke passen siehe foto
   2. drohnen so ausrichten, dass man mit der drehung eines spiegels (und dem nachrichten der aze) die spikies auf der eigenen seite und den kegel gegenüber treffen kann schritte dazu:
      1. feinjustage der hängung -> runder metallstab paralell zum spielfeldrand, und wasserwaage
      2. winkel der aufhängung der kegel ändern
      3. eventuell auch kegelwinkel nochmal nachmessen und justieren
9. Drohnen an Strom anschließen, dabei auf verpolung achten - wenn LED rot leuchten verpolung richtig
   1. einen kegel anwählen - beam page 4 control kanal -> auf 255 (homing) 3 sekunden, wenn er los dreht, wieder auf 0, 
   2. wenn er gestoppt hat: mit pan (pos) kanal so einstellen, dass der gegenüberliegende Kegel zentriert im beam ist die beste der drei seiten vom kegel suchen
   3. set zero pos: control kanal auf 127 - nach 3 sek wieder aus also auf 0, über pos kanal auf 0, dann soll es auf richtige position fahren
   4. azor einzeln von spine0 aus mit pan/tilt so einstellen, dass keine facetten getroffen werden und das dreieck oben im schatten sichbar ist (spine1) und die facetten komplett getroffen werden pos gegenüber von spine1 ist spine2
   5. spikie drohnen presets (beispiel drohne 1, azor 201)
      1. drohne1 und azor201 anwählen und auf pos. sp1
      2. nur drohne anwählen und so gut wie möglich auf spikie 101 ausrichten
      3. nur azor anwählen und siehe oben idealstes ideal wäre, wenn beam direkt auf linse spikie zeigt wenn spikie auf mirror pos (vis objekt) gerichtet -> azor wird im pan nicht auf spikie sondern auf spiegel ausgerichtet, im tilt aus spikie
      4. palette mit beiden angewählt updaten
      5. die nächsten sp positionen von sp1 pos ausgehend einstellen