///// SystemFailed Licht-Setup
- ein kurzes Manual


/// Intro

In diesem Dokument soll beschrieben werden, wie das Licht-Setup für die Performance System Failed aufgebaut ist.

Zur DMX-Erzeugung wird Chamsys MagicQ im Zusammenhang mit einem Snakesys B4 Artnet-Node verwendet.
MagicQ läuft auf dem Lichtrechner und als weiteres Bedien-Interface werden zwei Midi-Controller verwendet.
Zur Integration der Midi-Controller gibt es ein Touchdesigner-Script, das die eingehenden Midi-Werte in OSC-Messages übersetzt. Diese OSC-Messages werden in unterschiedlicher Weise in MagicQ ausgewertet.

Das zentrale Elment der Lichtsteuerung ist das Touchdesigner-Script lightingRig.toe.
Per UDP-Stream (touchIn) vom Haupt-Touchdesigner-Patch der Show werden die die relevanten Trackerpositionen, die mit Highlights beleuchtet werden sollen, gefüttert.
Im Script wird dann entschieden, welche Lampen mit welchen Parametern (Farbe, Zoom, ...) die Highlights beleuchten sollen und wiederum per OSC und Artnet wird MagicQ ferngesteuert.


/// MagicQ-MIDI-Interfacing

...



/// lightingRig

...

