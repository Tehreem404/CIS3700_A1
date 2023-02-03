from Classes.board import *
import pprint
import random
import argparse


def print_(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)

def optimal_board(n, population_size, conf_threshold, limit):
    population = [Board(n) for _ in range(population_size)]
    iter = 0
    set_probability(population)
    #print params
    print(f"Parameters: n={n}, population_size={population_size}, conflict_threshold={conf_threshold}, limit={limit}")
    print("-"*50)
    threshold = 1/(conf_threshold+1)
    while iter < limit:
        if (possible_optimal := sort_population(population)[0]).get_fitness() >= threshold:
            return possible_optimal
        print(f"\nIter:{iter}/{limit} Most optimal board:")
        print(possible_optimal)     
        iter += 1
        population = breed_population(population)
        set_probability(population)

    sorted_pop = sort_population(population)
    print_(sorted_pop[:10])

    return (sorted_pop[0])

def breed_population(population: list[Board]):
    gene_sample = []
    #for creating n samples
    population_size = len(population)
    for _ in range(population_size):
        #for checking n intervals
        r = random.random()
        lb = 0
        for i in range(population_size):
            board = population[i]
            ub = lb + population[i].probability
            # lb, ub = sum([member.probability for member in population[:i]]), sum([member.probability for member in population[:i+1]])
            if lb < r < ub:
                gene_sample.append(board)
                break
            lb = ub
    new_population = []
    for i in range(0, population_size, 2):
        x, y = gene_sample[i], gene_sample[i+1]
        new_population += x.breed(y), y.breed(x)

    return(new_population)

def set_probability(population):
    total_fitness = 0
    for x in population:
        total_fitness += x.get_fitness()
    #-6, -4 : sum -> -10 
    #-6/-10 = 0.6, -4/-10 = 0.4
    for x in population:
        x.set_probability((x.get_fitness()/total_fitness))

def sort_population(population):
    return(sorted(population, key=lambda x: x.get_fitness(), reverse=True))

def main(n, population_size, conflict_threshold, limit):
    op_board = optimal_board(n, population_size, conflict_threshold, limit)
    
    output_board = [["." for _ in range(n)] for _ in range(n)]
    
    print("-"*50)
    print("Final board Information:")
    print(op_board)
    board = op_board.get_board() 
    for y in range(n):
        output_board[y][board[y]] = "Q"
    
    print("\n")
    print(f"Board with {conflict_threshold} conflict threshold found (Or Limit {limit} reached):")
    for i in range(n):
        for j in range(n):
            print(output_board[i][j], end=" ")
        print()
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #all args are keyword args, with meta variable name
    parser.add_argument("-n", type=int, help="size of board", default=10)
    parser.add_argument("-p", "--population_size", type=int, help="size of population", default=10000)
    parser.add_argument("-c", "--conflict_threshold", type=int, help="conflict threshold", default=0)
    parser.add_argument("-l", "--limit", type=int, help="limit of iterations", default=50)

    args = parser.parse_args()
    main(args.n, args.population_size, args.conflict_threshold, args.limit)