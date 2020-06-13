import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from song import *

class SongTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Livin La Vida Loca", "Ricky Martin")

    def test_has_name(self):
        self.assertEqual(self.song1.name, "Livin La Vida Loca")
        
    def test_has_author(self):
        self.assertEqual(self.song1.author, "Ricky Martin")



if __name__ == "__main__":
    unittest.main()