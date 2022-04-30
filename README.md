# Supply-chain

## Problème d'ordonnancement

Le problème du montage d'un film s'apparente à un problème d'ordonnancement que nous tenterons de généraliser en premier temps.

Le problème est le suivant : nous souhaitons trouver l'ordre optimal dans lequel effectuer des activités (appelées *__tâches__*). Cependant, ces activités nécessitent des *__prérequis__* c'est-à-dire que pour effectuer une activité, il est nécessaire d'en avoir effectuer une (ou plusieurs) autre(s) au préalable. Enfin, chaque activité nécessite une certaine *__durée__* (en nombre de jours) pour être effectuée mais également un temps *__d'attente__* entre la fin d'un prérequis et le début de cette tâche. Ces durées doivent être minimisées de sorte à ce que les activités soient réalisées le plus tôt possible.

Ce problème peut être modélisé via un graphe avec chaque sommet représentant une tâche (assimilée à sa durée correspondante) et chaque arrête représentant un prérequis.

## Dossier

Le dossier est composé :
- d'une librairie visualisation (qui modèlise le problème)
- d'une librairie résolution (qui résout le problème)
- des tests des librairies
- d'un fichier toml pour la gestion des dépendances
- d'une interface en ligne de commande
- d'un fichier README de présentation
- d'une image png qui visualise le graphe associé au problème
