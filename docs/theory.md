# Fundamente teoretice: algoritmii Greedy

## 1. Ce este o strategie Greedy?

Un algoritm Greedy construieste o solutie pas cu pas. La fiecare pas alege varianta care pare cea mai buna conform unui criteriu local, apoi pastreaza alegerea si continua cu problema ramasa.

Caracteristica definitorie este ca algoritmul nu revizuieste in mod normal deciziile anterioare. Din acest motiv, faptul ca o alegere este buna local **nu garanteaza** ca solutia finala este optima.

## 2. Doua proprietati importante

- **Greedy-choice property:** exista o solutie optima care contine alegerea locala facuta de algoritm.
- **Optimal substructure:** dupa fixarea alegerii, partea ramasa a unei solutii optime este o solutie optima pentru subproblema ramasa.

Aceste proprietati trebuie demonstrate pentru problema concreta. Nu sunt proprietati pe care orice problema le are automat.

## 3. Problema Activity Selection

Avem un set de activitati. Fiecare activitate (a_i) are un timp de inceput (s_i) si un timp de final (f_i), cu (s_i < f_i). Vrem un subset cu cardinalitate maxima, astfel incat activitatile selectate sa nu se suprapuna.

Doua activitati consecutive (a_i) si (a_j) sunt compatibile daca:

[
f_i \leq s_j
]

Folosim intervale semi-deschise ([s_i, f_i)), deci o activitate care se termina la ora 5 poate fi urmata de una care incepe exact la ora 5.

### Strategia Greedy

1. Sortam activitatile crescator dupa timpul de finalizare.
2. Alegem prima activitate.
3. Parcurgem activitatile in aceasta ordine.
4. Selectam o activitate numai daca incepe dupa sau exact la finalul ultimei activitati selectate.
5. Continuam pana la epuizarea listei.

### Pseudocod

```text
GREEDY-ACTIVITY-SELECTION(A):
    sorteaza A crescator dupa timpul de finalizare
    S = lista vida
    ultimul_final = -infinit

    pentru fiecare activitate a din A:
        daca a.start >= ultimul_final:
            adauga a in S
            ultimul_final = a.finish

    returneaza S
```

## 4. De ce este corecta alegerea „finish cel mai devreme”?

Fie (g) activitatea care se termina cel mai devreme dintre toate activitatile disponibile. Fie (O) o solutie optima, iar (a) prima activitate din (O), in ordinea cronologica.

Prin definitie, (g.finish \leq a.finish).

Daca (O) incepe cu (a), nu avem nimic de demonstrat. Daca incepe cu alta activitate, o putem inlocui pe (a) cu (g):

- (g) se termina cel tarziu cand se termina (a);
- toate activitatile care urmau dupa (a) raman compatibile cu (g);
- numarul activitatilor selectate nu se schimba.

Prin urmare, exista cel putin o solutie optima care incepe cu alegerea Greedy (g). Aceasta este proprietatea alegerii Greedy.

## 5. De ce putem rezolva problema ramasa la fel?

Dupa alegerea lui (g), eliminam toate activitatile care incep inainte de (g.finish). Cele ramase formeaza aceeasi problema, dar cu mai putine activitati.

Daca partea ramasa nu ar fi optima pentru subproblema, am putea inlocui acea parte cu una mai buna si am obtine o solutie mai buna pentru problema initiala. Contradictie cu faptul ca solutia initiala era optima.

Asadar, subproblema are aceeasi structura si poate fi rezolvata cu aceeasi strategie. Impreuna, proprietatea alegerii Greedy si structura optima a subproblemei justifica algoritmul.

## 6. Observatie importanta

Greedy nu inseamna „alege orice pare mai bun”. Criteriul trebuie justificat matematic pentru problema respectiva.

Pentru Activity Selection neponderata, alegerea activitatii care se termina cel mai devreme este optima. Pentru varianta ponderata, in care fiecare activitate are un profit si vrem profit total maxim, aceasta regula nu este in general suficienta; se foloseste de obicei programare dinamica.
