from agenci import Grass, Predator, Prey


class Model:
    def __init__(self, size, predator_n, prey_n):
        # przydala by sie lista wszytskich agentow ale tez plansza gdzie sie znajduja zeby potem latwiej robic step
        # ale tez jeszcze niewiem jak to powinno dzialac moze wgl inaczej a nie tak xd
        self.grid = [] # SIZExSIZE
        self.agents = []
        # tworzymy ich na podstawie odpowiednio liczby predatorow i preyow
        for i in range(predator_n):
            self.agents.append(Predator)
        for i in range(prey_n):
            self.agents.append(Prey)

    def step(self):
        for agent in self.agents:
            agent.step()
