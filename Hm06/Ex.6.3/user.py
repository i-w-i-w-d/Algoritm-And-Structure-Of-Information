class OpenAddressingHashTable:
    def __init__(self, capacity=10007):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.DELETED = object()

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_keys = self.keys
        old_values = self.values
        self.capacity = self.capacity * 2 + 1
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        for k, v in zip(old_keys, old_values):
            if k is not None and k is not self.DELETED:
                self.put(k, v)

    def put(self, key, value):
        if self.size >= self.capacity * 0.7:
            self._resize()

        idx = self._hash(key)
        first_deleted = -1

        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            if self.keys[idx] is self.DELETED and first_deleted == -1:
                first_deleted = idx
            idx = (idx + 1) % self.capacity

        if first_deleted != -1:
            idx = first_deleted

        self.keys[idx] = key
        self.values[idx] = value
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
        return None

catalog = None

def init():
    """Викликається 1 раз на початку виконання програми."""
    global catalog
    catalog = OpenAddressingHashTable()

def addBook(author, title):
    """Додає книгу до бібліотеки."""
    global catalog
    books = catalog.get(author)
    if books is None:
        books = set()
        catalog.put(author, books)
    books.add(title)

def find(author, title):
    """Перевіряє чи міститься задана книга у бібліотеці."""
    global catalog
    books = catalog.get(author)
    if books is not None:
        return title in books
    return False

def delete(author, title):
    """Видаляє книгу з бібліотеки."""
    global catalog
    books = catalog.get(author)
    if books is not None:
        if title in books:
            books.remove(title)

def findByAuthor(author):
    """Повертає список книг заданого автора у алфавітному порядку."""
    global catalog
    books = catalog.get(author)
    if books is not None and len(books) > 0:
        return sorted(list(books))
    return []