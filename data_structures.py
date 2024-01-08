class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        "Ajoute un nouvel élément à la fin de la liste."
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def get_all_data(self):
        "Récupère tous les éléments de la liste."
        data = []
        current = self.head
        while current:
            data.append(current.data)
            current = current.next
        return data

    def length(self):
        "Retourne la longueur de la liste."
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get_at(self, index):
        "Récupère un élément à un index spécifique."
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None  # Si l'index est hors de portée
    
    def get_last(self):
        "Retourne le dernier élément de la liste."
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.data

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        " Fonction de hachage pour convertir une clé en un index de tableau."
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = LinkedList()
        else:
            current = self.table[index].head
            while current:
                if current.data[0] == key:
                    current.data = (key, value)
                    return
                current = current.next
        self.table[index].append((key, value))

    def get(self, key):
        "Récupère une valeur à partir d'une clé."
        index = self._hash(key)
        if self.table[index]:
            current = self.table[index].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
        return None
