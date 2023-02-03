""" a class for all nxn boards """
""" will generate/determine its own fitness, mutation etc. """

import random

class Board:
    #a board object for each nxn queen solution
    def __init__(self, n):
        self.n = n
        self.conflicts = 0
        self.board = self.generate_board(n)
        self.fitness = self.determine_fitness()
        self.mutation_rate = 0.05
        self.probability = 0
    
    def get_fitness(self):
        return self.fitness
    
    def set_probability(self, probability):
        self.probability = probability

    def get_probability(self):
        return self.probability
    
    def get_board(self):
        return self.board
    
    def generate_board(self, n):
        #create a random board
        board = [i for i in range(n)]
        random.shuffle(board)
        return board
    
    def determine_fitness(self):
        #determine fitness of the board
        conflicts = 0
        for i in range(self.n):
            #check for diagonal conflicts
            conflicts += self.conflict(i)
        self.conflicts = conflicts
        
        return 1/(conflicts+1)
    
    def conflict(self, i):
        #starting from 12, clockwise
        queen_deltas = [(1,-1),(1,1)]
        knight_deltas = [(1,-2),(2,-1),(2,1),(1,2)]

        conflicts = 0
        for dx, dy in queen_deltas:
            scalar = 0
            while True:
                scalar += 1
                x, y = i + scalar*dx, self.board[i] + scalar*dy
                #if x or y out of bound, break
                if x >= self.n or x < 0 or y >= self.n or y < 0:
                    break
                #else check for queen in new x,y, add to conflict if true
                if self.board[x] == y:
                    conflicts += 1

        for dx, dy in knight_deltas:
            x, y = i + dx, self.board[i] + dy
            #if x or y out of bound, break
            if x >= self.n or x < 0 or y >= self.n or y < 0:
                break
            #else check for queen in new x,y, add to conflict if true
            if self.board[x] == y:
                conflicts += 1

        return conflicts

    def set_board(self, board):
        self.board = board

    def breed(self, other):
        #breed a board with another board
        child = Board(self.n)
        other_board = other.get_board()
        child.set_board(self.board[:self.n//2] + other_board[self.n//2:])
        child.mutate()
        child.fix_board()
        self.fitness = self.determine_fitness()
        return child

    def fix_board(self):
        #fixes the board for horizontal conflicts
        non_existent = []
        for i in range(self.n):
            if i not in self.board:
                non_existent.append(i)
        for i in range(self.n):
            if self.board.count(self.board[i]) > 1:
                self.board[i] = non_existent.pop()
    
    def mutate(self):
        #mutate a board
        for i in range(self.n):
            if random.random() < self.mutation_rate:
                self.board[i] = random.randint(0, self.n-1)
    
    def __repr__(self):
        return f"Board({self.board}, fitness={self.fitness}, conflicts={self.conflicts}, probability={self.probability})"