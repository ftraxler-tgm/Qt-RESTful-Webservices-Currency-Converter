# Qt-RESTful-Webservices-Currency-Converter

Representational State Transfer (REST) ist einen Architektur-Stil  für verteilte Systeme, welcher auf eine möglichst einfache Architektur  abzielt. RESTful Webservices erlauben den Zugriff auf Daten und  verwenden üblicherweise weit verbreitete Web-Standards wie HTTP, URIs  und JSON. Ein simples RESTful Webservice ist meist über eine bestimmte  URL erreichbar und liefert je nach übergebene GET-Parameter  unterschiedliche Daten im JSON-Format zurück.



Sie  wurden beauftragt, eine schlanke grafische Oberfläche für einen  Währungsumwandler zu schreiben, der es erlaubt, einen Betrag aus einer  Ursprungs-Währung in eine oder mehrere Zielwährungen umzuwandeln. Dabei  soll es möglich sein, sowohl Live-Kurse (RESTful Webservice) als auch  (fest hinterlegte) Offline-Daten zu verwenden. Sie müssen **kein eigenes RESTful Webservice implementieren**! Verwenden Sie ein kostenlos verfügbares Webservice, wie zum Beispiel folgendes Service der Europäischen Zentralbank: <https://exchangeratesapi.io/>



Verwenden Sie PyQt5 sowie das MVC-Pattern, um Ihr Programm sauber zu trennen (GUI, Controller, Model)!



GUI

- Die grafische Oberfläche erlaubt die Eingabe eines 

- - Betrags (Zahlen)
  - einer Ursprungswährung im 3-Zeichen-Format (z.B. "EUR") sowie 
  - einer oder mehrerer Zielwährungen (durch Komma getrennt, z.B. "GBP,USD")

- Es gibt drei Buttons: 

- - Ein Button zum Umrechnen, 
  - ein Button zum Schließen und 
  - einer zum Zurücksetzen der Eingaben

- In  einer Statusleiste (unten) wird angezeigt, ob die letzte Abfrage  fehlerfrei funktionierte und ggf. welcher Fehler aufgetreten ist

- In einem großen HTML-Textfeld wird die Ausgabe des Converter-Services angezeigt

- Über  eine Checkbox kann gesteuert werden, ob Live-Daten aus einem  REST-Service oder fest hinterlegte Daten verwendet werden sollen

- Die GUI wird über den Qt Designer und pyuic5 **generiert** - der generierte Code wird **nicht manuell verändert**

*Hinweis: Hat man die Packages **pyqt5** und **pyqt5-tools**  installiert, kann man grafische Oberflächen sehr einfach mit dem  Designer  (<Python>/Lib/site-packages/pqt5_tools/Qt/bin/designer.exe)  modellieren und über den Befehl **pyuic5** (<Python>/Scripts) in eine .py-Datei umwandeln*



**Model**

- Das Model bildet die Schnittstelle zum Webservice bzw. zu den lokal hinterlegten Daten

- Es gibt **zwei** Serivce-**Strategien** (eigene Klassen!):

- - Eine Strategie fragt ein Online-RESTful Service ab (Empfehlung: <https://exchangeratesapi.io/>) und wandelt das Ergebnis in (HTML-)Text um
  - Eine zweite Strategie verwendet lokal abgelegte (hardgecodete) Werte und liefert wieder das Ergebnis als (HTML-)Text zurück
  - Beide Klassen übernehmen den Betrag, die Ursprungswährung und die Zielwährung(en) als Parameter
  - Eine abstrakte Klasse fasst die Gemeinsamkeiten zusammen (in Python sind abstrakte Klassen mit abc.ABC möglich)

*Hinweis: Über das Python-Package **requests** können sehr einfach Webservice-Anfragen geschickt und über JSON in ein Dictionary umgewandelt werden:*

import requests

...

```
url = "https://api.exchangeratesapi.io/latest"
params = {"base": cur_from,
          "symbols": cur_to
          }
resp = requests.get(url, params=params)
if resp.status_code != 200:
    raise ValueError(output.format(resp.status_code))
output = resp.json()
```

**Controller**

- Der Controller ist der Einstiegspunkt für das Programm - er erzeugt die GUI und zeigt sie als Qt-Applikation an

- Er kümmert sich außerdem um das Event-Handling:

- - Zurücksetzen-Button (sofern nicht schon im Designer über Signals und Slots gelöst)

  - - Setzt alle Eingabe- und Ausgabefelder zurück

  - Exit-Button (sofern nicht schon im Designer über Signals und Slots gelöst)

  - - Schließt die Applikation

  - Umrechnen-Button

  - - Ermittelt  über die aktuell ausgewählte Strategie das Ergebnis der Umrechnung und  übergibt dabei den Betrag, die Ursprungs-Währung und die Ziel-Währung
    - Zeigt das Ergebnis im Ausgabefeld an und aktualisiert die Statusleiste

  - Checkbox

  - - Wechselt je nach Checked-Status die Strategie auf RESTful-Service bzw. lokales Service

**Abgabe**

- Dokumentierter und (manuell) getesteter Python-Code
- **HTML-Dokumentation** (z.B. Sphinx oder doxygen)