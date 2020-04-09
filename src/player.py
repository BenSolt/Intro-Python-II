# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
    

    def __str__(self):
        return f"My name is '{self.name}', I am currently located {self.location}"
    
    def pickup_item(self, item):
        self.items.append(item)
        print(self.location.item)
    
    def drop_item(self,item):
        self.items.remove(item)
