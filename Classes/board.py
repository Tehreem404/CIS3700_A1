import random

class Board:
    #a board object for each nxn queen solution
    def __init__(self, n):
        self.n = n
        self.board = self.generate_board(n)
        self.fitness = self.determine_fitness()
        self.mutation_rate = 0.1
        self.mutation_amount = 0.1
    
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

        return -conflicts
    
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

    def mutate(self):
        #mutate a board
        for i in range(self.n):
            if random.randint(0, self.n - 1) < self.mutation_rate:
                self.board[i] = (self.board[i] + random.randint(-self.mutation_amount, self.mutation_amount)) % self.n
        self.fitness = self.get_fitness()
    
    def __repr__(self):
        return f"Board({self.board}, fitness={self.fitness})"