class Guest:
    def __init__(self, name, funds, fav_song):
        self.__name__ = name
        self.__funds__ = funds
        self.__fav_song__ = fav_song

    def get_name(self):
        return self.__name__

    def set_name(self, name):
        self.__name__ = name

    def get_funds(self):
        return self.__funds__

    def set_funds(self, funds):
        self.__funds__ = funds

    def get_fav_song(self):
        return self.__fav_song__

    def set_fav_song(self, song):
        self.__fav_song__ = song

    def deduct_funds(self, cost):
        self.set_funds(self.get_funds() - cost)

    def can_afford_entry(self, price):
        return self.get_funds() >= price

    def cheer(self, songs):
        for song in songs:
            if song.name == self.__fav_song__.name:
                return "Whooo!"
