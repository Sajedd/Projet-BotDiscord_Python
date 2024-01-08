from threading import Lock
from data_structures import LinkedList, HashTable

class CommandHistoryManager:
    def __init__(self):
        self.user_histories = HashTable()
        self.locks = HashTable() 
        self.current_positions = HashTable()

    def _get_lock(self, user_id):
        "Récupère ou crée un verrou pour un utilisateur donné."
        if not self.locks.get(user_id):
            self.locks.add(user_id, Lock())
        return self.locks.get(user_id)

    def add_command(self, user_id, command):
        "Ajoute une commande à l'historique d'un utilisateur."
        with self._get_lock(user_id):
            if not self.user_histories.get(user_id):
                self.user_histories.add(user_id, LinkedList())
            self.user_histories.get(user_id).append(command)
            self.current_positions.add(user_id, -1)

    def get_user_history(self, user_id):
        "Récupère l'historique des commandes d'un utilisateur."
        with self._get_lock(user_id):
            history = self.user_histories.get(user_id)
            return history.get_all_data() if history else []

    def get_last_command(self, user_id):
        if user_id in self.user_histories:
            history = self.user_histories.get(user_id)
            if not history or history.is_empty():
                return None
            return history.get_last()
        return None

    def clear_history(self, user_id):
        "Efface l'historique des commandes d'un utilisateur."
        with self._get_lock(user_id):
            self.user_histories.add(user_id, LinkedList())
            self.current_positions.add(user_id, -1)
            

    def navigate_history(self, user_id, direction):
        "Permet de naviguer dans l'historique des commandes."
        with self._get_lock(user_id):
            history = self.user_histories.get(user_id)
            if not history:
                return None

            position = self.current_positions.get(user_id)
            if direction == 'forward':
                position = min(position + 1, history.length() - 1)
            elif direction == 'backward':
                position = max(position - 1, -1)

            self.current_positions.add(user_id, position)
            if position == -1:
                return "Début de l'historique"
            return history.get_at(position)
