# Fundamente teoretice: algoritmii Greedy

## 1. Ce este o strategie Greedy?

Un algoritm Greedy construiește o soluție pas cu pas. La fiecare pas alege varianta care pare cea mai bună conform unui criteriu local, apoi păstrează alegerea și continuă cu problema rămasă.

Caracteristica definitorie este că algoritmul nu revizuiește, în mod normal, deciziile anterioare. Din acest motiv, faptul că o alegere este bună local **nu garantează** că soluția finală este optimă.

## 2. Două proprietăți importante

- **Greedy-choice property (proprietatea alegerii Greedy):** există o soluție optimă care conține alegerea locală făcută de algoritm.
- **Optimal substructure (substructura optimă):** după fixarea alegerii, partea rămasă a unei soluții optime este o soluție optimă pentru subproblema rămasă.

Aceste proprietăți trebuie demonstrate pentru problema concretă. Nu sunt proprietăți pe care orice problemă le are automat.

## 3. Problema Activity Selection

Avem un set de activități. Fiecare activitate $a_i$ are un timp de început $s_i$ și un timp de final $f_i$, cu $s_i < f_i$. Vrem un subset cu cardinalitate maximă, astfel încât activitățile selectate să nu se suprapună.

Două activități, $a_i$ și $a_j$, sunt compatibile dacă activitatea $a_i$ se termină înainte sau exact când începe activitatea $a_j$:

$$
f_i \leq s_j
$$

Folosim intervale semi-deschise $[s_i, f_i)$. Astfel, o activitate care se termină la ora 5 poate fi urmată de una care începe exact la ora 5.

### Strategia Greedy

1. Sortăm activitățile crescător după timpul de finalizare.
2. Alegem prima activitate din lista sortată.
3. Parcurgem activitățile în această ordine.
4. Selectăm o activitate numai dacă începe după sau exact la finalul ultimei activități selectate.
5. Continuăm până la epuizarea listei.

### Pseudocod

```text
SELECTARE-ACTIVITATI(A):
    sortează A crescător după timpul de finalizare
    S = listă vidă
    ultimul_final = -infinit

    pentru fiecare activitate a din A:
        dacă a.început >= ultimul_final:
            adaugă a în S
            ultimul_final = a.final

    returnează S
```

Inițializarea cu $-\infty$ permite selectarea primei activități din lista sortată.

## 4. De ce este corectă alegerea „finalizare cât mai devreme”?

Fie $g$ activitatea care se termină cel mai devreme dintre toate activitățile disponibile. Fie $O$ o soluție optimă, iar $a$ prima activitate din $O$, în ordinea cronologică.

Prin definiția lui $g$, avem:

$$
f_g \leq f_a
$$

Dacă $O$ începe cu $g$, nu avem nimic de demonstrat. Dacă începe cu altă activitate, o putem înlocui pe $a$ cu $g$:

- $g$ se termină cel târziu când se termină $a$;
- toate activitățile care urmau după $a$ rămân compatibile cu $g$;
- numărul activităților selectate nu se schimbă.

Prin urmare, există cel puțin o soluție optimă care începe cu alegerea Greedy $g$. Aceasta demonstrează proprietatea alegerii Greedy.

## 5. De ce putem rezolva problema rămasă la fel?

După alegerea lui $g$, eliminăm toate activitățile care încep înainte de $f_g$. Activitățile rămase formează aceeași problemă, dar cu mai puține activități.

Dacă partea rămasă nu ar fi optimă pentru subproblemă, am putea înlocui acea parte cu o soluție mai bună și am obține o soluție mai bună pentru problema inițială. Aceasta ar contrazice ipoteza că soluția inițială era optimă.

Așadar, subproblema are aceeași structură și poate fi rezolvată cu aceeași strategie. Împreună, proprietatea alegerii Greedy și substructura optimă justifică algoritmul.

## 6. Observație importantă

Greedy nu înseamnă „alege orice pare mai bun”. Criteriul trebuie justificat matematic pentru problema respectivă.

Pentru problema Activity Selection neponderată, alegerea activității care se termină cel mai devreme produce o soluție optimă. Pentru varianta ponderată, în care fiecare activitate are un profit și vrem să maximizăm profitul total, această regulă nu este în general suficientă; se folosește de obicei programarea dinamică.
