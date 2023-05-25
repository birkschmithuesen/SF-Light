## Grundfunktion

Jede Box verbraucht 4 x 4 Adressen - pro Kanal RGBW.


## Konnektivität

Die Box verbindet sich automatisch mit dem letzten konfigurierten WiFi. 

Wenn die Box die konfigurierte Verbindung findet, bezieht sie die IP-Adresse per DHCP. Auf dieser IP-Adresse lässt sich das Konfigurations-Web-Interface erreichen.
Die IP-Adresse wird per ArtPollReply kommuniziert und lässt sich zB im MagicQ unter SETUP->VIEW DMX I/O->NET MANAGER->VIEW ART-NET finden.

Wenn das konfigurierte WiFi nicht erreichbar ist, wird ein eigener AP aufgemacht (SSID: TiA LED Dimmer #X, Passwort: 12345678).
Bei Verbindung mit diesem WiFi sollte sich das Konfigurationsinterface direkt öffnen.


## Konfiguration per Webinterface

### Configure WiFi
Das gewünschte WiFi konfigurieren.
(Nach Klick dauerts etwas bis die vorhandenen SSIDs gescannt wurden und angezeigt werden.)

### Setup
Es lässt sich Startadresse und Artnet-Universum einstellen.

Die Einstellung fürs Artnet-Subnet wird nicht berücksichtigt. Es hört nur auf Subnet 0.

(Evtl. ist irgendwo bei den Adressen was mit "Start der Zählung bei 1" vs "Start bei 0" - kann mich nicht mehr genau erinnern - Also im Zweifel mal die Nachbaradresse ausprobieren ;)

