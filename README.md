# Final Project – Bundesliga Elo Rating

## Projektüberblick

In diesem Projekt wird ein Elo Rating Modell für die 1. Bundesliga umgesetzt und analysiert.

Untersucht werden die Saisons 2023/24 und 2024/25.  
Ziel ist es, die Entwicklung von Teamstärken im Saisonverlauf zu analysieren und zu prüfen, inwiefern sich Spielausgänge mit einem Elo Modell beschreiben lassen.

Neben einer gemeinsamen Auswertung beider Saisons werden die Spielzeiten auch getrennt betrachtet, um Unterschiede besser erkennen zu können.

---

## Fragestellung

Im Rahmen des Projekts werden folgende Fragen untersucht:

- Wie entwickeln sich die Elo Werte der Teams über die Saison hinweg?
- Wie gut lässt sich die tatsächliche Leistung der Teams durch das Elo Modell abbilden?
- Gibt es erkennbare Unterschiede zwischen den beiden Saisons?
- Inwiefern hat der Heimvorteil Einfluss auf die Ergebnisse?

---

## Daten

Für die Analyse werden Spieltagsdaten der 1. Bundesliga aus den Saisons 2023/24 und 2024/25 verwendet.

Die Daten liegen als CSV Dateien vor und enthalten unter anderem:

- Datum
- Heimteam und Auswärtsteam
- Tore beider Teams
- Spielergebnis

Die Datensätze wurden lokal eingebunden und im Projekt weiterverarbeitet.

---

## Umsetzung

Das Projekt ist in mehrere Schritte unterteilt:

1. Einlesen und Aufbereitung der Daten mit pandas  
2. Erste deskriptive Analyse und Visualisierung  
3. Implementierung des Elo Modells  
4. Anwendung des Modells auf alle Spiele  
5. Vergleich der Ergebnisse zwischen den Saisons  

---

## Installation

```bash
uv pip install -e .