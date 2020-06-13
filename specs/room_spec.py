import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from room import *
from song import *
from guest import *

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Girlfri", "NSYNC")
        self.song2 = Song("Power of Love", "Huey Lewis and the News")
        self.song3 = Song("Pretty Rave Girl", "Daddy DJ")
        self.song4 = Song("You shook me all night long", "AC/DC")
        self.song5 = Song("Barbie Girl", "Aqua")
        self.song6 = Song("Ode to Joy", "Beethoven")

        self.songs1 = [self.song1, self.song2, self.song3, self.song4]
        self.songs2 = [self.song5, self.song6]

        self.room = Room("CodeClan Room", 3, self. songs1, 5)

        self.guest1 = Guest("Alice", 15.0, self. song2)
        self.guest2 = Guest("Bob", 500.0, self. song1)
        self.guest3 = Guest("Charlie", 1.0, self. song3)
        self.guest4 = Guest("Dave", 20.0, self. song4)

        self.guests = [self.guest1, self.guest2, self.guest4]

    def test_room_has_name(self):
        self.assertEqual(self.room.name, "CodeClan Room")

    def test_room_has_songs(self):
        self.assertEqual(self.room.number_of_songs(), 4)

    def test_can_check_in_guests(self):
        self.room.check_in_guests(self.guests)
        self.assertEqual(3, len(self.room.guests))
        
    def test_can_check_in_guests__room_already_has_guests(self):
        group1 = [self.guest1, self.guest2]
        group2 = [self.guest4]
        self.room.check_in_guests(group1)
        self.room.check_in_guests(group2)
        self.assertEqual(3, self.room.number_of_guests())
        
    def test_can_check_in_guests__one_guest_cannot_afford(self):
        guests = [self.guest1, self.guest2, self.guest3]

        self.room.check_in_guests(guests)
        self.assertEqual(2, self.room.number_of_guests())
        
    def test_cannot_be_overbooked(self):
        self.room.check_in_guests(self.guests)

        self.room.check_in_guests([ self.guest4])
        self.assertEqual(3, self.room.number_of_guests())
        

    def test_guests_can_check_out(self):
        self.room.check_in_guests(self.guests)
        self.room.check_out_guests()
        self.assertEqual(0, len(self.room.guests))
        

    def test_can_cheer(self):
        self.room.check_in_guests(self.guests)
        songs = self.room.songs

        self.assertEqual("Whooo!", self.guests[0].cheer(songs))
        

    def test_fee_was_paid_at_check_in(self):
        self.room.check_in_guests(self.guests)
        self.assertEqual(15, self.room.till)
        self.assertEqual(10.0, self.guests[0].get_funds())
        self.assertEqual(495.0, self.guests[1].get_funds())
        self.assertEqual(15.0, self.guests[2].get_funds())

    def test_can_add_one_song(self):
        self.room.add_song(self.song5)
        self.assertEqual(5, self.room.number_of_songs())
        

    def test_can_add_multiple_songs(self):
        self.room.add_multiple_songs(self.songs2)
        self.assertEqual(6, self.room.number_of_songs())

        