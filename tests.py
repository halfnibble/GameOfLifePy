import unittest
from world import World
from cell import Cell


class TestWorldMethods(unittest.TestCase):

    def test_world_has_map(self):
        world = World()

        self.assertIsInstance(world.map, list)

    def test_world_map_create_nodes(self):
        world = World()
        cell = Cell(1, 5)
        world.addCell(cell)
        self.assertEqual(len(world.map), 1)
        newCell = Cell(1, 5)
        world.addCell(newCell)
        self.assertEqual(len(world.map), 1)

    def test_number_of_neighbors(self):
        """
        Setup
        - - -
        - 1 -
        - 2 -
        - 3 -
        - - -
        """
        world = World()
        cell1 = Cell(1, 1)
        cell2 = Cell(2, 1)
        cell3 = Cell(3, 1)
        world.addCell(cell1)
        world.addCell(cell2)
        world.addCell(cell3)

        self.assertEqual(world.numberOfNeighbors(cell2), 2)
        self.assertEqual(world.numberOfNeighbors(cell3), 1)


if __name__ == '__main__':
    unittest.main()
