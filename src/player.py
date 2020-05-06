# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
    

    def __str__(self):
        return f" My name is '\033[0;31m{self.name}\033[0m'\nI am currently located {self.location}"
    
    def pickup_item(self, item):
        self.items.append(item)
        print(f"you picked up \033[1;33m{item.name}\033[0m")
    
    def drop_item(self, item):
        self.items.remove(item)
        print(f"you dropped \033[1;33m{item.name}\033[0m")
