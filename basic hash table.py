class HashTable:

    def __init__(self):
        self.collection={}

    def hash(self, string: str):
        return sum(ord(char) for char in string) #Returns the sum of the unicode values of each character in the string

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key] #this checks for a key, if it collides, and looks for the speific one you are looking to delete, so it doesn't wipe out keys with the same hash value.

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None