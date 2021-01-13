import unittest
from model import Model
from agenci import Grass


class TestModel(unittest.TestCase):

    def test_grass(self):
        pass

    def test_number_of_agents(self):
        pass

    def test_get_neightbourhood(self):
        pass

    def test_move_agent(self):
        pass

    def test_remove_from_grid(self):
        pass

    def test_remove_agent(self):
        pass

    def test_collect_data(self):
        pass

    def test_grass_step(self):
        print('Running test_grass_step ...')
        grass = Grass((0, 0), 'model')
        grass.grown = False
        for i in range(14):
            grass.step()
        self.assertFalse(grass.grown)
        grass.step()
        self.assertTrue(grass.grown)
        self.assertEqual(grass.count, 15)


if __name__ == '__main__':
    unittest.main()
