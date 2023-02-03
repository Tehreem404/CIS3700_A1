>CIS-3700 AI Assignment 1 -- Author: Tehreem Nazar 1108993

# Part 1: Searching
`part1.py` will complete:
* Depth-first search
* Breadth-first search
* Uniform-cost search
* Greedy best-first search
* A* search

# How to Run Part 1
`python3 part1.py`
* if there are any errors running it could be the version I am running version 3.11.0


# Part 2: SuperQueens
`part2.py` will complete:
* nxn SuperQueens
* solution is derived using genetic algorithm with mutations
* 20000 parents are generated (on default) and generations are reproduced until the optimal solution is found

# How to Run Part 2
`python3 part2.py [-n N] [-p POPULATION_SIZE] [-c CONFLICT_THRESHOLD] [-l LIMIT]`
* where `[N]` represents the number of queens and the nxn board size (if left empty default will be 10)
* where `[POPULATION_SIZE]` represents an (optional) configuration for how big the user wants the population (if left empty, default will be 10000) 
* where `[CONFLICT_THRESHOLD]` represents minimum number of conflicts to look for (if left empty, default will be 0)
* where `[LIMIT]` represents the number of iterations (generations) that are produced (if left empty, default is 100)
* if there are any errors running it could be the version I am running version 3.11.0
    
>NOTES: 
* run `python3 part2.py -h` to see all usages 
* the only flags that really need to be used are: `[-n N]`, and `[-c CONFLICT_THRESHOLD]`
>>* Example: `python3 part2.py -n 6 -c 1` (lowest number of conflicts in 6x6 is 1)
* IT WILL USUALLY TAKE AROUND 50 ITERATIONS TO FIND 0 COLLISIONS 10X10 