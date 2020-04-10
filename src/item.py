
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"\033[1;33m{self.name}\033[0m, \033[1;32m{self.description}\033[0m"


class ItemNot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"\033[1;33m{self.name}\033[0m, \033[1;32m{self.description}\033[0m"