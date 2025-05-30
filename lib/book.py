#!/usr/bin/env python3

class Book:
   class Book:
    def __init__(self, title="", page_count=0, genre=""):
        self.title = title
        self.page_count = page_count
        self.genre = genre

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # Validation using property for page_count
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be a positive integer.")

    page_count = property(get_page_count, set_page_count)

    
        