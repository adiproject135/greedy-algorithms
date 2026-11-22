"""Demonstratii Greedy: selectarea activitatilor si problema rucsacului 0/1."""

from itertools import combinations


# O activitate este reprezentata printr-un tuplu:
# (nume, inceput, sfarsit)


def selecteaza_activitati(activitati):
    """Selecteaza numarul maxim de activitati compatibile.

    Complexitate: O(n log n) pentru sortare si O(n) pentru parcurgere.
    """
    ordonate = sorted(activitati, key=lambda activitate: (activitate[2], activitate[1]))
    selectate = []
    ultimul_sfarsit = None

    for activitate in ordonate:
        if ultimul_sfarsit is None or activitate[1] >= ultimul_sfarsit:
            selectate.append(activitate)
            ultimul_sfarsit = activitate[2]

    return selectate


def selectie_compatibila(activitati):
    ordonate = sorted(activitati, key=lambda activitate: (activitate[1], activitate[2]))
    for i in range(1, len(ordonate)):
        if ordonate[i - 1][2] > ordonate[i][1]:
            return False
    return True


# Un obiect din rucsac este reprezentat printr-un tuplu:
# (nume, greutate, valoare)


def greedy_dupa_raport(obiecte, capacitate):
    """Alege obiectele dupa raportul valoare/greutate.

    Euristica nu garanteaza optimul pentru problema rucsacului 0/1.
    """
    ordonate = sorted(
        obiecte,
        key=lambda obiect: (-obiect[2] / obiect[1], obiect[1]),
    )
    alese = []
    greutate_folosita = 0

    for obiect in ordonate:
        if greutate_folosita + obiect[1] <= capacitate:
            alese.append(obiect)
            greutate_folosita += obiect[1]

    return alese


def solutie_optima_brutala(obiecte, capacitate):
    """Cauta solutia exacta prin enumerarea submultimilor (doar pentru exemple mici)."""
    cea_mai_buna = []
    valoare_maxima = 0
    greutate_minima = 0

    for dimensiune in range(len(obiecte) + 1):
        for submultime in combinations(obiecte, dimensiune):
            greutate = sum(obiect[1] for obiect in submultime)
            valoare = sum(obiect[2] for obiect in submultime)

            if greutate <= capacitate and (
                valoare > valoare_maxima
                or (valoare == valoare_maxima and greutate < greutate_minima)
            ):
                cea_mai_buna = list(submultime)
                valoare_maxima = valoare
                greutate_minima = greutate

    return cea_mai_buna


def greutate_totala(obiecte):
    return sum(obiect[1] for obiect in obiecte)


def valoare_totala(obiecte):
    return sum(obiect[2] for obiect in obiecte)
