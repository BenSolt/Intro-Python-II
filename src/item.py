
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        # on_take
        # on_drop
        # on_look
    

    def __str__(self):
        return f"You have picked up '{self.name}', It is {self.description}"
