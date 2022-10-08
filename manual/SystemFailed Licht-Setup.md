# SystemFailed Licht-Setup
- ein kurzes Manual


## Intro

In diesem Dokument soll beschrieben werden, wie das Licht-Setup für die Performance System Failed aufgebaut ist.

Zur DMX-Erzeugung wird Chamsys MagicQ im Zusammenhang mit einem Snakesys B4 Artnet-Node verwendet.
MagicQ läuft auf dem Lichtrechner und als weiteres Bedien-Interface werden zwei Midi-Controller verwendet.
Zur Integration der Midi-Controller gibt es ein Touchdesigner-Script, das die eingehenden Midi-Werte in OSC-Messages übersetzt. Diese OSC-Messages werden in unterschiedlicher Weise in MagicQ ausgewertet.

Das zentrale Elment der Lichtsteuerung ist das Touchdesigner-Script lightingRig.toe.
Per UDP-Stream (touchIn) vom Haupt-Touchdesigner-Patch der Show werden die die relevanten Trackerpositionen, die mit Highlights beleuchtet werden sollen, gefüttert.
Im Script wird dann entschieden, welche Lampen mit welchen Parametern (Farbe, Zoom, ...) die Highlights beleuchten sollen und wiederum per OSC und Artnet wird MagicQ ferngesteuert.


## MagicQ-MIDI-Interfacing

### Troubleshooting

Fehler: Beim Start wird der Korg nicht erkannt, TD hat ein anderes Korg device gelistet.
Lösung: Dialogs -> MIDI Device Mapper -> Device Mappings -> das richtige In Device wählen



## lightingRig

lightingRig.toe ist ein Touchdesigner-Patch, der "highlight"daten vom Haupt Touchdesigner-Patch des Stückes bekommt und MagicQ entsprechend fernsteuert. 
In diesen Daten wird neben Koordinaten unter anderem auch der angeforderte "Highlightcue" gesendet. Dieser gibt an, ob der Highlight zB eine Freeze-Violation oder ein Performer-Highlight ist. 
Der entsprechende Look ist in der Tabelle config/dat_cue_table.csv abgelegt und kann dort editiert werden.


### Troubleshooting

Fehler: Highlights sind nicht sichtbar
Lösung: HighlightChannel von MagicQ kommt nicht bei TD an, weil nicht hochgezogen, oder DMX vom MQ nicht bei TD ankommt

Fehler: DMX vom MagicQ kommt nicht bei TD an
Lösung: Setup DMX IO
Lösung: DMX-Receiver von TD funktioniert nicht richtig (im Balkendiagramm ist keine Änderung sichtbar, wenn die HLSpikie-Kanäle verändert werden) - Local Address hin und herstellen

Fehler: TDactivation reagiert nicht, obwohl DMX ankommt
Lösung: Re-Init-all-Button (dann aber auch nochmal reset highlights)
