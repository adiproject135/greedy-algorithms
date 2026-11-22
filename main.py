"""Demonstratii Greedy: selectarea activitatilor si problema rucsacului 0/1."""

from dataclasses import dataclass
from itertools import combinations


# Problema selectarii activitatilor
@dataclass(frozen=True)
class Activitate:
    nume: str
    inceput: int
    sfarsit: int


def selecteaza_activitati(activitati):
    """Selecteaza numarul maxim de activitati compatibile.

    Complexitate: O(n log n) pentru sortare si O(n) pentru parcurgere.
    """
    ordonate = sorted(
        activitati,
        key=lambda activitate: (
            activitate.sfarsit,
            activitate.inceput,
            activitate.nume,
        ),
    )
    selectate = []
    ultimul_sfarsit = None

    for activitate in ordonate:
        if ultimul_sfarsit is None or activitate.inceput >= ultimul_sfarsit:
            selectate.append(activitate)
            ultimul_sfarsit = activitate.sfarsit

    return selectate


def selectie_compatibila(activitati):
    ordonate = sorted(
        activitati,
        key=lambda activitate: (activitate.inceput, activitate.sfarsit),
    )
    return all(
        anterioara.sfarsit <= urmatoarea.inceput
        for anterioara, urmatoarea in zip(ordonate, ordonate[1:])
    )


# Problema rucsacului 0/1: Greedy nu garanteaza intotdeauna optimul
@dataclass(frozen=True)
class Obiect:
    nume: str
    greutate: int
    valoare: int


def greedy_dupa_raport(obiecte, capacitate):
    """Alege obiectele dupa raportul valoare/greutate.

    Euristica nu garanteaza optimul pentru problema rucsacului 0/1.
    """
    ordonate = sorted(
        obiecte,
        key=lambda obiect: (
            -obiect.valoare / obiect.greutate,
            obiect.greutate,
            obiect.nume,
        ),
    )
    alese = []
    greutate_folosita = 0

    for obiect in ordonate:
        if greutate_folosita + obiect.greutate <= capacitate:
            alese.append(obiect)
            greutate_folosita += obiect.greutate

    return alese


def solutie_optima_brutala(obiecte, capacitate):
    """Cauta solutia exacta prin enumerarea submultimilor (doar pentru exemple mici)."""
    cea_mai_buna = []
    valoare_maxima = 0
    greutate_minima = 0

    for dimensiune in range(len(obiecte) + 1):
        for submultime in combinations(obiecte, dimensiune):
            greutate = greutate_totala(submultime)
            valoare = valoare_totala(submultime)
            if greutate <= capacitate and (
                valoare > valoare_maxima
                or (valoare == valoare_maxima and greutate < greutate_minima)
            ):
                cea_mai_buna = list(submultime)
                valoare_maxima = valoare
                greutate_minima = greutate

    return cea_mai_buna


def greutate_totala(obiecte):
    return sum(obiect.greutate for obiect in obiecte)


def valoare_totala(obiecte):
    return sum(obiect.valoare for obiect in obiecte)
