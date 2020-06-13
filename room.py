class Room:

    def __init__(self, name, max_capacity, songs, entry_fee):
        self.name = name
        self.max_capacity = max_capacity
        self.songs = songs
        self.guests = []
        self.entry_fee = entry_fee
        self.till = 0

    def number_of_songs(self):
        return len(self.songs)

    def number_of_guests(self):
        return len(self.guests)

    def add_song(self, song):
        self.songs.append(song)

    def add_multiple_songs(self, new_songs):
        for song in new_songs:
            self.songs.append(song)

    def add_fee_to_till(self):
        self.till += self.entry_fee

    def available_spaces(self):
        return self.max_capacity - len(self.guests)

    def free_space(self, guests):
        return len(guests) <= self.available_spaces()

    def check_out_guests(self):
        self.guests.clear()

    def check_in_guests(self, guests):
        if not self.free_space(guests):
            return

        for guest in guests:
            if guest.can_afford_entry(self.entry_fee):
                self.check_in_guest(guest)

    def check_in_guest(self, guest):
        guest.deduct_funds(self.entry_fee)
        self.add_fee_to_till()
        self.guests.append(guest)






