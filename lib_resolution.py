"""Description.
Fonctionnalités pour la résolution du problème d'ordonnancement.
"""

from typing import Union
from rich.table import Table
from typing import List, Dict, Tuple

def _cherche_sans_prerequis(cahier_des_charges: Dict[str, List[str]]) -> List[str]:
    """Cherche les tâches qui n'ont pas de prérequis nécessaire. 
    Renvoie la liste des tâches correspondantes.
    """
    return [tache for tache, prerequiss in cahier_des_charges.items() if prerequiss == []]

def _elague_cdc(cahier_des_charges: Dict[str, List[str]], a_effectuer: str) -> Dict[str, List[str]]:
    """Renvoie la liste des tâches qui ne sont pas à effectuer.
    """
    return {
        tache: [prerequis for prerequis in prerequiss if prerequis != a_effectuer]
        for tache, prerequiss in cahier_des_charges.items()
        if tache != a_effectuer
    }

def ordonnance(cahier_des_charges: Dict[str, List[str]]) -> List[str]:
    """Renvoie l'ordre optimal des tâches.
    """
    a_choisir = _cherche_sans_prerequis(cahier_des_charges)
    if a_choisir == []:
        if cahier_des_charges == {}:
            return []
        else:
            raise ValueError("Il n'y a pas d'ordonnancement possible")
    a_effectuer, *_ = a_choisir
    nouveau = _elague_cdc(cahier_des_charges=cahier_des_charges, a_effectuer=a_effectuer)
    resultat = [a_effectuer]
    resultat.extend(ordonnance(nouveau))
    return resultat

def edt_parallele(
    cdc: Dict[str, Tuple[List[str], Union[float, int],Union[float, int]]]) -> Dict[str, Tuple[List[str],Union[float, int], Union[float, int]]]:
    """Permet d'effectuer des tâches simultanément. 
    Renvoie l'ordre des tâches et la durée totale à chaque étape.
    """
    ordre = ordonnance(
        {
            tache: prerequis
            for tache, (prerequis,duree, attente) in cdc.items()
        }
    )
    resultat = dict()
    for tache in ordre:
        prerequis, duree, attente = cdc[tache]
        if prerequis == []:
            debut = 0
        else:
            debut = max(resultat[precedent][1] for precedent in prerequis) 
        resultat[tache] = (debut+attente, debut+attente+duree)
    return resultat

def edt_to_table(cdc: Dict[str, Tuple[Union[float, int],Union[float, int]]]) -> Table:
    """Renvoie la solution du problème dans un tableau récapitulatif.
    """
    resultat = Table("Tâche", "Debut", "Fin")
    for (tache, (debut, fin)) in cdc.items():
        resultat.add_row(
            str(tache),
            str(debut),
            str(fin)
                )
    return resultat