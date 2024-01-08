Projet Bot Discord B2
Description
Ce projet consiste à développer un bot Discord avec diverses fonctionnalités, en utilisant des structures de données telles que les listes chaînées, les files, les arbres binaires, et les hashtables. Le bot est conçu pour maintenir un historique des commandes, gérer des dialogues interactifs, et stocker des données liées à l'utilisateur.

Fichiers et Leur Fonctionnalités
bot_main.py
Ce fichier est le point d'entrée principal du bot Discord. Il initialise le bot et gère les interactions de base avec l'utilisateur Discord.

command_history_manager.py
Gère l'historique des commandes du bot. Implémente des fonctionnalités pour voir la dernière commande, voir toutes les commandes d'un utilisateur, naviguer dans l'historique, et vider l'historique.

config.py
Contient la configuration du bot, y compris les tokens, les identifiants, et autres paramètres nécessaires au fonctionnement du bot.

data_persistence.py
Ce fichier gère la persistance des données. Il s'occupe de sauvegarder et de charger l'état du bot (y compris l'historique des commandes et l'état des dialogues) pour assurer la continuité en cas de redémarrage du bot.

data_structures.py
Définit les structures de données personnalisées utilisées dans le projet, comme les listes chaînées, les files, et les arbres binaires. Ces structures sont essentielles pour la gestion de l'historique des commandes et des dialogues interactifs.

football_motocross_quiz.py
Implémente un système de quiz interactif en utilisant un arbre de décision. Permet au bot de poser une série de questions à l'utilisateur et de répondre en fonction des réponses de l'utilisateur.

utilities.py
Fournit des fonctions utilitaires qui aident dans divers aspects du bot, comme la manipulation de chaînes de caractères, le traitement des entrées utilisateur, etc.

Fonctionnalités Clés
Gestion de l'Historique des Commandes : Utilise une liste chaînée, une pile, ou une file pour maintenir un historique des commandes.
Intégrité de l'Historique : Utilise une file pour limiter l'accès à l'historique à une seule personne à la fois.
Système de Dialogue Interactif : Utilise un arbre binaire pour créer un dialogue interactif avec l'utilisateur, permettant de poser des questions et de répondre aux besoins de l'utilisateur.
Stockage des Données par Utilisateur : Utilise une hashtable pour lier les données (historique des commandes, état des dialogues) à chaque utilisateur Discord.
Persistance des Données : Assure que les données ne sont pas perdues lorsque le bot s'arrête.
Extensibilité : Le système est conçu pour permettre l'ajout facile de nouvelles fonctionnalités au bot.
