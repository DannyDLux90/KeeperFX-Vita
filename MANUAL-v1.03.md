# KeeperFX Vita 1.03 — LiveArea Handbuch (aktualisierte Steuerung)

Das **finale Handbuch-Update** aktualisiert ausschließlich die in der Vita-Bubble enthaltenen Seiten unter `sce_sys/manual/`. Die finale, auf Hardware getestete RC4-Spielversion bleibt bytegleich erhalten.

## Ingame-Tastenbelegung

| Eingabe | Funktion |
|---|---|
| **L / R** | Vorherigen bzw. nächsten der fünf Reiter öffnen: Info, Räume, Zauber, Fallen/Türen, Kreaturen. |
| **Steuerkreuz** | In der aktiven Ingame-Seitenleiste zwischen verwendbaren Schaltflächen navigieren. |
| **Gelber Rahmen** | Zeigt das aktuelle Auswahlziel an. |
| **X (Cross)** | Ausgewählten Eintrag durch normalen GUI-Klick aktivieren. |
| **Kreaturen-Reiter** | Steuerkreuz wählt **Kreaturenporträts direkt**, X wählt die Kreatur. Die Tätigkeitsfilter bleiben per Touch bedienbar. |
| **Linker Stick** | Im laufenden Spiel die Kamera bewegen. |
| **Rechter Stick** | Freien Mauszeiger bewegen. |
| **O (Circle)** | Rechtsklick. |
| **SELECT** | Karte öffnen. |
| **START** | Escape / Spielmenü. |
| **Quadrat / Dreieck** | Leertaste / Tab. |

Im Hauptmenü bewegen linker Stick bzw. Steuerkreuz den Mauszeiger. Die Seitenleistensteuerung gilt für das laufende Spiel bei aktiver Seitenleiste, nicht für Intro/Frontend/Dialoge.

## Inhalt des aktualisierten Handbuchs

Alle Seiten haben die unveränderte Bildauflösung **960 × 544, PNG RGBA**:

1. Schnellstart
2. Tasten & Sticks (aktuelle 1.03-Belegung)
3. **Menüs & Kreaturen (neu)**
4. Front-Touch (alte Seite 3)
5. LAN / Direct-IP (alte Seite 4)
6. Daten & Fehlerhilfe (alte Seite 5)

Die Originalseiten wurden mit angepasster Seitennummerierung übernommen. Netzwerkfunktionen auf Seite 5 sind historisch dokumentiert; Multiplayer war kein Bestandteil des finalen RC4-Hardware-Akzeptanztests.

## Artefakte und Integrität

**Empfohlene aktualisierte VPK:** `KeeperFX-Vita-v1.03-FINAL-MANUAL-UPDATE-no-game-data.vpk`

| Artefakt | SHA-256 |
|---|---|
| Ursprüngliche finale v1.03 VPK (RC4, Referenz) | `d2b051f0fadf4e84f2feaded6b3a78aafee6f968da6f2fc6856ba6738c74cb7d` |
| Finale VPK mit korrigiertem Handbuch | `21f73fe8f8f223b3f40ce291da9544c956a66a858954b66fd2a9aeff78cb8a1d` |
| Aktualisiertes Source-ZIP | `1a05668965e33831d1b5ea8bec7d930769f125bc1dd2c0ecc5a5269ba8f85e3b` |
| Aktualisiertes Workspace-ZIP | `d425a71bd0f3019155f0c07bc268a3c94cb925fa30b748facf25a5163c8cdb33` |

**Maschinencode nicht verändert:** `eboot.bin` hat in beiden VPKs den SHA-256 `668d2937d2bdf4b2e297e28d772cd7165461698b9a1650e5adc07711f59c31d8`. Auch Titelkennung, LiveArea-XML, Icon, Shader, Sound und Game-Data-Platzhalter sind bytegenau gleich.

Die vollständigen Source- und Workspace-Archive sowie die VPK werden als separate Artefakte bereitgestellt und sind **nicht** als Binärdateien in diesem GitHub-Repository enthalten. Der finale C/C++-Quellpatch von 1.03 bleibt unverändert.

**Prüfstatus:** PNG-Maße, zusammenhängende Nummern 001–006, ZIP/VPK-Integrität, VPK-Dateivergleich und binäre Gleichheit des Programms sind bestätigt. Ob das neue Handbuch auf einer echten PS Vita korrekt dargestellt wird, ist noch nicht getestet.
