from Classes.frontier import *
from Classes.stateClass import *
import pprint

def print_(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)

""" Parsing nodeInfo.txt to store information """
def parse_graph_nodes(filename):
    nodes = {}
    familyDict = {}
    file = open(filename, 'r')
    for line in file:
        name, h, family = line.split()
        familyDict[name] = family
        node = StateNode(h, name)
        nodes[name] = node
    create_graph(nodes, familyDict)
    return(nodes)

""" Creating the graph for all nodes"""
def create_graph(nodes, familyDict):
    for name, node in nodes.items():
        family = familyDict.get(name)
        members = family.split(",")
        for member in members:
            vertice, cost = member.split(":")
            if vertice == "None":
                continue
            node.add_member(nodes.get(vertice), cost)

""" implements bfs, dfs, ucs, gbfs, and a* """
def general_search(start, goal, frontier):
    explored = []
    frontier.add(start)
    parent = {start: None}
    while not frontier.is_empty():
        current = frontier.pop()
        explored.append(current)
        if current == goal:
            path = []
            while current != None:
                path.append(current)
                current = parent.get(current)
            path.reverse()
            return(path)
        family = current.get_family()
        for key in family:
            member = family[key][0]
            if member not in explored and not frontier.contains(member):
                frontier.add(member)
                parent[member] = current
    return(explored)

""" Depth-first search """
def depth_first_search(explored, graph, node, goal):
    if node == goal:
        explored.append(node)
    if node not in explored:
        explored.append(node)
        family = node.get_family()
        for key in family:
            member = family[key][0]
            if member not in explored:
                return depth_first_search(explored, graph, member, goal)
    return(explored)

""" Breadth-first search """
def breadth_first_search(start, goal):
    frontier = QueueFrontier()
    return(general_search(start, goal, frontier))

""" Uniform-cost search """
def uniform_cost_search(start, goal):
    frontier = [start]
    explored = []
    while frontier:
        node = frontier.pop(0)
        explored.append(node)
        if node == goal:
            return(explored)
        family = sort_family(node.get_family())
        for key in family:
            member = family[key][0] 
            if member not in explored and member not in frontier:
                frontier.append(member)
    return(explored)

""" Greedy Best-first search """
def greedy_best_first_search(start, goal):
    explored = []
    current = start
    while True:
        explored.append(current)
        if current == goal:
            return explored
        current = min([member[0] for member in current.get_family().values()], key=lambda node:node.get_heuristic())
    
""" A* search """
def a_star_search(start, goal):
    explored = []
    current = start
    while True:
        explored.append(current)
        if current == goal:
            return explored
        current = min([member[0] for member in current.get_family().values()], key=lambda node:node.get_heuristic())

""" function to print the search result lists """
def print_search(search):
    for i in range(len(search)):
        if i != len(search) -1:
            print(search[i].get_name(), end="-")
        else:
            print(search[i].get_name(), end="\n\n")

""" funciton to sort the family by cost """
def sort_family(family):
    sorted_family = {}
    cost_list = []
    for key in family:
        cost_list.append(int(family[key][1]))
    cost_list.sort()
    for cost in cost_list:
        for key in family:
            if int(family[key][1]) == cost:
                sorted_family[key] = family[key]
    return(sorted_family)

def main():
    graph = parse_graph_nodes('Data/nodeInfo.txt')

    print("Depth-first search:")
    explored = []
    dfs = depth_first_search(explored, graph, graph['S'], graph['F'])
    print_search(dfs)

    print("Breadth-first search:")
    bfs = breadth_first_search(graph['S'], graph['F'])
    print_search(bfs)

    print("Uniform-cost search:")
    ucs = uniform_cost_search(graph['S'], graph['F'])
    print_search(ucs)
    
    print("Greedy best-first search:")
    gbfs = greedy_best_first_search(graph['S'], graph['F'])
    print_search(gbfs)
    
    print("A* Search:")
    ass = a_star_search(graph['S'], graph['F'])
    print_search(ass)

if __name__ == '__main__':
    main()