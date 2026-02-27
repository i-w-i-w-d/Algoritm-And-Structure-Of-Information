class ChainingHashTable:
    def __init__(self, capacity=10007):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity = self.capacity * 2 + 1
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        if self.size >= self.capacity * 1.5:
            self._resize()

        idx = self._hash(key)
        bucket = self.table[idx]

        for i, kv in enumerate(bucket):
            if kv[0] == key:
                bucket[i][1] = value
                return

        bucket.append([key, value])
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for k, v in bucket:
            if k == key:
                return v
        return None

catalog = None

def init():
    """Викликається 1 раз на початку виконання програми."""
    global catalog
    catalog = ChainingHashTable()


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