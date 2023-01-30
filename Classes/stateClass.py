""" defining a class for all nodes """
""" contains heuristics and family """

class StateNode(): 
    def __init__(self, heuristic, name):
        self.name = name
        self.heuristic = heuristic
        self.family = {}
    
    def get_name(self):
        return(self.name)
        
    def get_heuristic(self):
        return(self.heuristic)

    def get_family(self):
        return(self.family)

    def add_member(self, member, cost):
        self.family[member.get_name()] = [member,cost]    
