import unittest
from model import Model
from agenci import Grass
from agenci import Prey


class TestModel(unittest.TestCase):

    def setUp(self):
        self.n = 20
        self.preys_n = 13
        self.predators_n = 36
        self.model = Model(self.n, self.preys_n, self.predators_n, 0.2, 0.1)

    def test_false(self):
        grass = Grass((0, 0), 'model')
        self.assertIsInstance(grass, Prey)

    def test_grass(self):
        n = 0
        for col in self.model.grid:
            for field in col:
                n_f = 0
                for obj in field:
                    if type(obj) is Grass:
                        n += 1
                        n_f += 1
                self.assertEqual(n_f, 1)
        self.assertEqual(n, self.n*self.n)

    def test_number_of_agents(self):
        self.model.collect_data()
        prey_n = [i['preys'] for i in self.model.data]
        predator_n = [i['predators'] for i in self.model.data]
        self.assertEqual(self.preys_n + self.predators_n, int(predator_n[0])+int(prey_n[0]))

    def test_get_neightbourhood(self):
        cases = [[(0, 0), (0, 1), (1, 0), (1, 1)],
                 [(19, 0), (18, 0), (18, 1), (19, 1)],
                 [(0, 19), (0, 18), (1, 19), (1, 18)],
                 [(19, 19), (18, 19), (18, 18), (19, 18)]]
        for case in cases:
            nbh = self.model.get_neighbourhood(case[0])
            self.assertEqual(case[1::], nbh)

    def test_move_agent(self):
        prey = Prey((6, 13), self.model)
        self.model.grid[prey.pos[1]][prey.pos[0]].append(prey)
        self.assertTrue(prey in self.model.grid[prey.pos[1]][prey.pos[0]])
        new = (7, 12)
        self.model.move_agent(prey, new)
        self.assertFalse(prey in self.model.grid[prey.pos[1]][prey.pos[0]])
        self.assertTrue(prey in self.model.grid[new[1]][new[0]])

    def test_remove_from_grid(self):
        model = Model(20, 0, 0, 0.2, 0.1)
        prey = Prey((3, 16), model)
        model.grid[prey.pos[1]][prey.pos[0]].append(prey)
        self.assertTrue(prey in model.grid[prey.pos[1]][prey.pos[0]])
        model.remove_from_grid(prey, prey.pos)
        self.assertFalse(prey in model.grid[prey.pos[1]][prey.pos[0]])

    def test_prey_energy(self):
        prey = Prey((2, 2), 'model')
        prey.energy = 10
        for i in range(4):
            prey.energy -= 2
        self.assertEqual(prey.energy, 2)

    def test_remove_agent(self):
        prey = Prey((0, 0), self.model)
        self.model.agents.append(prey)
        self.assertTrue(prey in self.model.agents)
        self.model.remove_agent(prey)
        self.assertFalse(prey in self.model.agents)

    def test_grass_step(self):
        grass = Grass((0, 0), 'model')
        grass.grown = False
        for i in range(14):
            grass.step()
        self.assertFalse(grass.grown)
        grass.step()
        self.assertTrue(grass.grown)
        self.assertEqual(grass.count, 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)
