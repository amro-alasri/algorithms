class RandomizedSet(object):

    def __init__(self):
        self.elementToIndex = {}
        self.elements = []
    def insert(self, val):
        if val in self.elementToIndex:
            return False  # Element already exists, insertion failed

        self.elements.append(val)
        self.elementToIndex[val] = len(self.elements) - 1
        return True  # Insertion successful

    def remove(self, val):
        if val not in self.elementToIndex:
            return False  # Element doesn't exist, removal failed

        last_element = self.elements[-1]
        index_to_remove = self.elementToIndex[val]

        # Swap the element to be removed with the last element
        self.elements[index_to_remove] = last_element
        self.elementToIndex[last_element] = index_to_remove

        # Remove the last element
        self.elements.pop()
        del self.elementToIndex[val]

        return True  # Removal successful

    def getRandom(self):
        # Generate a random index within the size of the array
        random_index = random.randint(0, len(self.elements) - 1)
        return self.elements[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()