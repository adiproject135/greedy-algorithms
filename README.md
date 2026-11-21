# Algoritmi Greedy: selectarea activitatilor

Proiect pentru prezentarea tehnicii **Greedy (algoritmi lacomi)**. Problema principala este **Activity Selection**: selectarea numarului maxim de activitati care nu se suprapun.

Proiectul contine explicatia teoretica, implementarea Python, teste automate si un notebook pentru demonstratia live. Mai include doua contraexemple care arata de ce nu orice alegere locala produce o solutie optima.

## Intrebarea centrala

Avem activitati cu momente de inceput si de final. Cum selectam cat mai multe activitati compatibile, folosind o strategie simpla si eficienta?

**Strategia Greedy:** la fiecare pas alegem activitatea compatibila care se termina cel mai devreme. Dupa alegere, eliminam din considerare activitatile care se suprapun cu ea.

## Structura repository-ului

```text
greedy-algorithms/
├── README.md
├── pyproject.toml
├── requirements.txt
├── src/
│   └── greedy_project/
│       ├── __init__.py
│       ├── activity_selection.py
│       └── knapsack_demo.py
├── tests/
│   ├── test_activity_selection.py
│   └── test_knapsack_demo.py
├── notebooks/
│   └── greedy_activity_selection.ipynb
└── docs/
    ├── theory.md
    ├── complexity-and-limitations.md
    ├── presentation-outline.md
    └── team-plan.md
```

## Rulare locala

Necesita Python 3.10 sau mai nou.

### 1. Testele automate

Din directorul principal al proiectului:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

### 2. Notebook-ul

Instalati dependintele pentru notebook:

```bash
python -m pip install -r requirements.txt
```

Porniti Jupyter:

```bash
jupyter notebook notebooks/greedy_activity_selection.ipynb
```

Rulati celulele in ordine, de sus in jos.

## Modelul matematic

O activitate este un interval `[start, finish)`, cu `start < finish`. Doua activitati consecutive sunt compatibile daca activitatea anterioara se termina cel tarziu cand incepe urmatoarea:

`finish_anterioara <= start_urmatoare`.

Alegerea activitatilor care se ating la capete este permisa. De exemplu, [1, 3) si [3, 5) nu se suprapun.

## Continutul demonstratiei

1. Explicarea tehnicii Greedy si a proprietatilor necesare pentru corectitudine.
2. Enuntul Activity Selection si strategia „cel mai devreme timp de finalizare”.
3. Implementarea si rularea pe un set de activitati.
4. Cazuri in care alte euristici (cel mai devreme start / durata cea mai mica) esueaza.
5. Contraexemplul 0/1 Knapsack: alegerea dupa raportul valoare/greutate nu garanteaza optimul.
6. Complexitate, limite si comparatie cu programarea dinamica.

## Contributii

Planul initial al echipei este in [docs/team-plan.md](docs/team-plan.md). Fiecare membru trebuie sa ruleze codul si sa poata explica deciziile algoritmice, nu doar partea pe care o prezinta.

## Referinte pentru documentare

- University of California, Davis, *Activity-selection problem*: https://www.cs.ucdavis.edu/~bai/ECS122A/Notes/ActivitySelect.pdf
- University of British Columbia, *Greedy Algorithms*: https://www.cs.ubc.ca/~liorma/cpsc320/files/greedy-algorithms-2x2.pdf
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms*, sectiunea despre problema selectarii activitatilor (consultati editia disponibila in biblioteca).

## Nota privind corectitudinea

Codul este o implementare didactica pentru problema prezentata, nu o solutie universala pentru orice problema de planificare. Problema ponderata (cand fiecare activitate are un profit) necesita o analiza diferita; regula „finish cel mai devreme” nu rezolva in general varianta ponderata.
