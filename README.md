# Final Project – Bundesliga Elo Rating

## Projektüberblick

In diesem Projekt wird ein Elo-Rating-Modell für die 1. Bundesliga implementiert und analysiert.  
Untersucht werden die Saisons 2023/24 und 2024/25.

Ziel ist es zu prüfen, wie gut ein Elo-basiertes Modell Spielausgänge vorhersagen kann und wie sich Teamstärken im Saisonverlauf entwickeln.

---

## Fragestellung

- Wie gut sagt ein Elo-Modell Spielausgänge im Vergleich zu einer einfachen Baseline voraus?
- Unterscheiden sich die Ergebnisse zwischen den beiden Saisons?
- Hat ein Heimvorteil einen messbaren Einfluss auf die Vorhersagequalität?

---

## Daten

Verwendet werden öffentlich zugängliche Bundesliga-Spieldaten (z. B. OpenLigaDB).  
Berücksichtigt werden unter anderem Heim-/Auswärtsteam, Tore und Spieltag.

---

## Installation

```bash
uv pip install -e .