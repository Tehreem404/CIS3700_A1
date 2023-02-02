from Classes.board import *
import random
import pprint
import sys

def print_(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)

def optimal_board(n, population_size):
    limit = 100
    gen = 0
    while gen < limit:
        gen += 1
        #generate population
        population = generate_population(n, population_size)    
        #find 2 fittest
        #crossbreed

def generate_population(n, population_size):
    return [Board(n) for _ in range(population_size)]

def main(n, population_size):
    ob = optimal_board(n, population_size)
    print(ob)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except:
        n = 10

    try:
        population_size = int(sys.argv[2])
    except:
        population_size = 20
    main(n, population_size)