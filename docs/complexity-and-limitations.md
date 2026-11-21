# Complexitate, cazuri de test si limite

## 1. Complexitatea Activity Selection

Fie (n) numarul de activitati.

| Etapa | Complexitate |
|---|---:|
| Copierea elementelor intr-o lista | (O(n)) |
| Sortarea dupa timpul de finalizare | (O(n \, log n)) |
| Parcurgerea si selectarea | (O(n)) |
| **Total** | **(O(n \, log n))** |

Sortarea domina timpul total. Daca activitatile sunt deja sortate dupa timpul de finalizare, parcurgerea greedy este (O(n)).

Implementarea returneaza lista activitatilor selectate si pastreaza o copie sortata. Prin urmare, memoria auxiliara este (O(n)). Lista rezultatului ocupa suplimentar (O(k)), unde (k \leq n), deci tot (O(n)) in cel mai rau caz.

## 2. De ce alegerea locala conteaza

Pentru Activity Selection, criteriul „finish cel mai devreme” lasa cat mai mult timp disponibil pentru activitatile urmatoare. Nu este suficient sa alegem o activitate scurta sau una care incepe devreme.

### Strategie alternativa: start cel mai devreme

Activitati:
- A = [1, 10)
- B = [2, 3)
- C = [3, 4)
- D = [4, 5)

Daca alegem activitatea care incepe cel mai devreme, alegem A si obtinem o singura activitate. Solutia optima este B, C, D, adica trei activitati compatibile.

### Strategie alternativa: durata cea mai mica

Activitati:
- A = [0, 4)
- B = [5, 9)
- S = [3, 6)

S are durata 3, iar A si B au durata 4. Daca alegem mai intai activitatea cea mai scurta, S se suprapune cu A si B, deci selectam una singura. Solutia optima este A si B, doua activitati compatibile.

Aceste exemple arata ca nu orice criteriu local conduce la maximul global.

## 3. Cand Greedy nu este optim: 0/1 Knapsack

Capacitatea rucsacului este 50. Obiectele nu pot fi fractionate.

| Obiect | Greutate | Valoare | Valoare / Greutate |
|---|---:|---:|---:|
| A | 10 | 60 | 6 |
| B | 20 | 100 | 5 |
| C | 30 | 120 | 4 |

Daca alegem descrescator dupa raportul valoare/greutate:
- alegem A (greutate 10, valoare 60);
- alegem B (greutate 20, valoare 100);
- C nu mai incape.

Rezultatul Greedy are valoarea 160 si greutatea 30.

Solutia optima pentru 0/1 Knapsack este B + C:
- greutate: 20 + 30 = 50;
- valoare: 100 + 120 = 220.

Deci criteriul raportului valoare/greutate nu garanteaza optimul in varianta 0/1.

**Distinctie:** pentru Fractional Knapsack, unde putem lua o fractiune dintr-un obiect, sortarea descrescatoare dupa raportul valoare/greutate este optima. In 0/1 Knapsack, obiectele sunt indivizibile, iar alegerea locala poate bloca o combinatie mai buna.

## 4. Se poate implementa mai bine?

Depinde de problema si de date:

- Daca activitatile nu sunt sortate, (O(n \log n)) este dominat de sortare.
- Daca intrarea este deja sortata dupa timpul de finalizare, putem obtine (O(n)).
- Daca datele vin in flux si nu pot fi sortate in avans, avem nevoie de o strategie adaptata; nu putem presupune ca stim deja urmatoarea activitate cu finalul cel mai mic.
- Pentru Activity Selection ponderata, trebuie schimbata abordarea; o formulare de programare dinamica este potrivita.
- Pentru 0/1 Knapsack, programarea dinamica poate rezolva exact problema in (O(nW)) timp si (O(W)) memorie cu optimizare spatiala, unde (W) este capacitatea intreaga. Aceasta este complexitate pseudo-polinomiala, nu polinomiala in numarul de biti necesari pentru a reprezenta (W).

## 5. Ce ar trebui demonstrat live

1. Un set nesortat de activitati, pentru a arata ca implementarea sorteaza.
2. Un caz in care activitatile se ating la capete (compatibilitate).
3. Un caz in care alegerea „start cel mai devreme” esueaza.
4. Un caz in care alegerea „durata minima” esueaza.
5. Contraexemplul 0/1 Knapsack: Greedy = 160, optim = 220.
