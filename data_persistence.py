import json
import os
from threading import Timer

class DataPersistence:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def save_data(self):
        """ Sauvegarde les données dans un fichier JSON. """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Erreur lors de l'enregistrement des données : {e}")

    def load_data(self):
        """ Charge les données depuis un fichier JSON. """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except IOError as e:
                print(f"Erreur lors du chargement des données : {e}")
        return {}

    def update_data(self, key, value):
        """ Met à jour une valeur spécifique dans les données. """
        self.data[key] = value
        self.save_data()

    def get_data(self, key):
        """ Récupère une valeur spécifique depuis les données. """
        return self.data.get(key)
