# Algoritmi Greedy: Activity Selection

Proiect pentru prezentarea tehnicii **Greedy (algoritmi lacomi)**. Problema principala este **Activity Selection**: selectarea numarului maxim de activitati care nu se suprapun.

Proiectul contine explicatia teoretica si un notebook autonom pentru implementare si demonstratia live. Toate functiile Python sunt definite direct in notebook, fara module proprii sau fisiere Python separate.

## Structura proiectului

```text
greedy-algorithms/
├── README.md
├── requirements.txt
├── notebooks/
│   └── greedy_activity_selection.ipynb
└── docs/
    ├── theory.md
    ├── complexity-and-limitations.md
    ├── presentation-outline.md
    └── team-plan.md
```

## Rulare

Necesita Python 3.10 sau mai nou.

Instalati dependintele pentru notebook:

```bash
python -m pip install -r requirements.txt
```

Porniti Jupyter din directorul principal al proiectului:

```bash
jupyter notebook notebooks/greedy_activity_selection.ipynb
```

Rulati celulele in ordine, de sus in jos. Implementarile si datele de test sunt definite direct in notebook. Nu este necesar niciun import din fisiere ale proiectului.

## Problema principala

Fiecare activitate are un moment de inceput si unul de final. Vrem sa selectam cat mai multe activitati care nu se suprapun.

**Strategia Greedy:** la fiecare pas alegem activitatea compatibila care se termina cel mai devreme. Dupa alegere, ignoram activitatile care se suprapun cu ea.

Doua activitati consecutive sunt compatibile daca activitatea anterioara se termina cel tarziu cand incepe urmatoarea: `finish_anterioara <= start_urmatoare`.

## Continutul demonstratiei

1. Explicarea tehnicii Greedy si a proprietatilor necesare pentru corectitudine.
2. Enuntul Activity Selection si strategia „cel mai devreme timp de finalizare”.
3. Implementarea si rularea pe un set de activitati.
4. Contraexemple pentru euristicile „cel mai devreme start” si „durata cea mai mica”.
5. Contraexemplul 0/1 Knapsack: alegerea dupa raportul valoare/greutate nu garanteaza optimul.
6. Complexitate, limite si comparatie cu programarea dinamica.

## Contributii

Planul echipei este in [docs/team-plan.md](docs/team-plan.md). Fiecare membru trebuie sa poata explica deciziile algoritmice, nu doar partea pe care o prezinta.

## Referinte

- University of California, Davis, *Activity-selection problem*: https://www.cs.ucdavis.edu/~bai/ECS122A/Notes/ActivitySelect.pdf
- University of British Columbia, *Greedy Algorithms*: https://www.cs.ubc.ca/~liorma/cpsc320/files/greedy-algorithms-2x2.pdf
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, sectiunea despre problema selectarii activitatilor.

## Nota privind corectitudinea

Regula „finish cel mai devreme” este optima pentru problema Activity Selection neponderata. Problema ponderata si alte probleme de optimizare pot necesita strategii diferite, precum programarea dinamica.
