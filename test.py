import unittest
from model import Model
from agenci import Grass
from agenci import Prey


class TestModel(unittest.TestCase):

    def test_grass(self):
        grass = Grass((0, 0), 'model')
        self.assertIsInstance(grass, Prey)

    def test_number_of_agents(self):
        model = Model(20, 10, 5, 0.2, 0.1)
        model.collect_data()
        prey_n=[i['preys'] for i in model.data]
        predator_n=[i['predators'] for i in model.data]
        self.assertEqual(15, int(predator_n[0])+int(prey_n[0]))

    def test_get_neightbourhood(self):
        pass

    def test_move_agent(self):
        pass

    def test_remove_from_grid(self):
        pass
    def test_prey_energy(self):
        prey = Prey((2,2), 'model')
        prey.energy=10
        for i in range(4):
            prey.energy -=2
        self.assertEqual(prey.energy, 2)

    def test_remove_agent(self): #nie wiem jak tego uzywac :<<

        #model = Model(20, 1, 1, 0.2, 0.1)
        #model.collect_data()
        #print(model.data)
        #preys = [i['preys'] for i in model.data]
        #model.remove_agent(preys)
        #modezl.collect_data()
        #print(model.data)

        pass

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
