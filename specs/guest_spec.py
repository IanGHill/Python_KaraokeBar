import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from guest import *
from song import *

class GuestTest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Makin Your Mind Up", "Bucks Fizz")
        self.song2 = Song("Take On Me", "A-ha")
        self.guest1 = Guest("Jimmy", 50, self.song1)

    def test_can_get_name(self):
        self.assertEqual(self.guest1.get_name(), "Jimmy")

    def test_can_set_name(self):
        self.guest1.set_name("Jo")
        self.assertEqual(self.guest1.get_name(), "Jo")

    def test_can_get_funds(self):
        self.assertEqual(self.guest1.get_funds(), 50)

    def test_can_set_funds(self):
        self.guest1.set_funds(30)
        self.assertEqual(self.guest1.get_funds(), 30)

    def test_can_get_fav_song(self):
        self.assertEqual(self.guest1.get_fav_song(), self.song1)

    def test_can_Set_fav_song(self):
        self.guest1.set_fav_song(self.song2)
        self.assertEqual(self.guest1.get_fav_song(), self.song2)

    def test_can_deduct_funds(self):
        self.guest1.deduct_funds(20)
        self.assertEqual(self.guest1.get_funds(), 30)

    def test_can_afford_entry(self):
        self.assertEqual(self.guest1.can_afford_entry(10), True)

    def test_cant_afford_entry(self):
        self.assertFalse(self.guest1.can_afford_entry(60))


if __name__ == "__main__":
    unittest.main()