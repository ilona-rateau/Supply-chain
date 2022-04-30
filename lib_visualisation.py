"""Description.
Fonctionnalités pour la visualisation du problème.
"""

from lib_resolution import _cherche_sans_prerequis, _elague_cdc,edt_parallele, ordonnance
from typing import Generator, Union
from rich.table import Table
import networkx as nx
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt


def genere_ordres(cahier_des_charges: Dict[str, List[str]]) -> Generator[List[str], None, None]:
    """Renvoie toutes les possibilités d'ordonnancement.
    """
    a_choisir = _cherche_sans_prerequis(cahier_des_charges)
    if a_choisir == []:
        if cahier_des_charges == {}:
            yield []
        else:
            raise ValueError("Il n'y a pas d'ordonnancement possible")
    for a_effectuer in a_choisir:
        nouveau = _elague_cdc(cahier_des_charges=cahier_des_charges, a_effectuer=a_effectuer)
        
        for ordre_suite in genere_ordres(nouveau):
            resultat = [a_effectuer]
            resultat.extend(ordre_suite)
            yield resultat

def cdc_to_table(cdc: Dict[str, Tuple[List[str],Union[float, int],Union[float, int]]]) -> Table:
    """Transforme le cahier des charges en tableau récapitulatif.
    """
    resultat = Table("Tâche","Prérequis", "Durée", "Attente")
    for (tache, (prerequis, duree, attente)) in cdc.items():
        resultat.add_row(
            str(tache),  
            " ".join([str(precedent) for precedent in prerequis]), 
            str(duree),
            str(attente)
        )
    return resultat

def genere_graphe(cdc: Dict[str, List[str]])->nx.DiGraph:
    """Crée le graphe associé au problème."""
    G = nx.DiGraph() #creation d'un graphe orienté 
    for k,v in cdc.items():
        G.add_node(k) #ajout des sommets
        for i in v:
            G.add_edge(i, k) #ajout des arretes
    nx.draw(G,edge_color='salmon',node_color='orchid', with_labels=True)
    plt.show
    plt.savefig("graph.png") #pour enregistrer dans un fichier format png
