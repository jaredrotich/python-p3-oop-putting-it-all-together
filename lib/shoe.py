#!/usr/bin/env python3

class Shoe:
   class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        self.size = size
        self.condition = ""

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    # Validation using property for size
    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._size = value
        else:
            print("size must be a positive number.")

    size = property(get_size, set_size)
