# To jest taki zarys mniej wiecej jak to powinno wygladac
# Genrelanie nie ma powiedziane jak to musi wygladac bo mozna do tego dodawac ile sie chce parametrow
# Np jakis bread_rate czyli jakie sa szanse na rozmnozenie
# Move moze byc poprostu wybieramy jedna z pozycji obok czyli jedna z 8 wokol losowo
from random import choice, random


class Agent:
    def __init__(self, pos, model):
        self.pos = pos
        self.energy = 20
        self.model = model

    def move(self):
        moves = self.model.get_neighbourhood(self.pos)
        next_move = choice(moves)
        self.model.move_agent(self, next_move)
        self.pos = next_move


class Predator(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)

    def step(self):
        self.energy -= 2
        if self.energy < 1:
            self.model.remove_from_grid(self, self.pos)
            self.model.remove_agent(self)
        else:
            self.move()
            if self.energy < 11:
                field = self.model.get_field(self.pos[0], self.pos[1])
                preys = [obj for obj in field if isinstance(obj, Prey)]
                if len(preys) > 0:
                    prey = choice(preys)
                    self.model.remove_from_grid(prey, self.pos)
                    self.model.remove_agent(prey)
                    self.energy += 10
            if random() < self.model.predator_bread_rate and self.energy > 7:
                predator = Predator(self.pos, self.model)
                self.model.grid[self.pos[1]][self.pos[0]].append(predator)
                self.model.agents.append(predator)
                self.energy //= 2


class Prey(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)

    def step(self):
        self.energy -= 2
        if self.energy < 1:
            self.model.remove_from_grid(self, self.pos)
            self.model.remove_agent(self)
        else:
            self.move()
            if self.energy < 11:
                field = self.model.get_field(self.pos[0], self.pos[1])
                grass = [obj for obj in field if isinstance(obj, Grass)][0]
                if grass.grown:
                    self.energy += 10
                    grass.grown = False
            if random() < self.model.prey_bread_rate and self.energy > 7:
                prey = Prey(self.pos, self.model)
                self.model.grid[self.pos[1]][self.pos[0]].append(prey)
                self.model.agents.append(prey)
                self.energy //= 2


class Grass:
    def __init__(self, pos, model):
        self.model = model
        self.pos = pos
        self.grown = True
        self.count = 15

    def step(self):
        if not self.grown:
            self.count -= 1
            if self.count == 0:
                self.grown = True
                self.count = 15
