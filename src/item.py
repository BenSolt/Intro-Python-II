
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    #this what i want??
        # self.inspect = []
       
        
    def __str__(self):
        return f"\033[1;33m{self.name}\033[0m, \033[1;32m{self.description}\n\033[0mtype \033[0;34mpickup\033[0m to pickup items\n"


