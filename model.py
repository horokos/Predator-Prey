from agenci import Grass, Predator, Prey
from random import randrange, shuffle


class Model:
    def __init__(self, size, prey_n, predator_n, prey_bread_rate, predator_bread_rate):
        self.grid = [[[] for i in range(size)] for j in range(size)]
        self.agents = []
        self.data = []
        self.size = size
        self.prey_bread_rate = prey_bread_rate
        self.predator_bread_rate = predator_bread_rate
        for i in range(predator_n):
            x = randrange(size)
            y = randrange(size)
            p = Predator((x, y), self)
            self.agents.append(p)
            self.grid[y][x].append(p)
        for i in range(prey_n):
            x = randrange(size)
            y = randrange(size)
            p = Prey((x, y), self)
            self.agents.append(p)
            self.grid[y][x].append(p)
        for y in range(size):
            for x in range(size):
                g = Grass((x, y), self)
                self.agents.append(g)
                self.grid[y][x].append(g)

    def step(self):
        shuffle(self.agents)
        for agent in self.agents:
            agent.step()
        self.collect_data()

    def get_field(self, x, y):
        return self.grid[y][x]

    def get_neighbourhood(self, pos):
        neightbourhood = []
        if pos[0] > 0:
            neightbourhood.append((pos[0]-1, pos[1]))
            if pos[1] > 0:
                neightbourhood.append((pos[0] - 1, pos[1] - 1))
            if pos[1] < self.size-1:
                neightbourhood.append((pos[0] - 1, pos[1] + 1))
        if pos[1] > 0:
            neightbourhood.append((pos[0], pos[1] - 1))
        if pos[1] < self.size - 1:
            neightbourhood.append((pos[0], pos[1] + 1))
        if pos[0] < self.size - 1:
            neightbourhood.append((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                neightbourhood.append((pos[0] + 1, pos[1] - 1))
            if pos[1] < self.size-1:
                neightbourhood.append((pos[0] + 1, pos[1] + 1))
        return neightbourhood

    def move_agent(self, agent, new_pos):
        i = self.grid[agent.pos[1]][agent.pos[0]].index(agent)
        a = self.grid[agent.pos[1]][agent.pos[0]].pop(i)
        self.grid[new_pos[1]][new_pos[0]].append(a)

    def collect_data(self):
        preys = 0
        predators = 0
        for obj in self.agents:
            if type(obj) is Prey:
                preys += 1
            if type(obj) is Predator:
                predators += 1
        self.data.append({'preys': preys, 'predators': predators})

    def remove_from_grid(self, obj, pos):
        self.grid[pos[1]][pos[0]].remove(obj)

    def remove_agent(self, obj):
        self.agents.remove(obj)
