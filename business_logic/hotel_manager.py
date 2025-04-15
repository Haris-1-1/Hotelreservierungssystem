from data_access.hotel_dal import HotelDAL
from model.hotel import Hotel

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = []  # Liste von Zimmern, z. B. Room-Objekte
      
    def set_name(self, name: str) -> None:
        self.__name = name

    def set_stars(self, stars: int) -> None:
        self.__stars = stars

    def delete(self) -> None:
        del self
  
    def get_hotel_id(self) -> int:
        return self.__hotel_id

    def get_name(self) -> str:
        return self.__name
      
    def get_stars(self) -> int:
        return self.__stars
      
    def get_rooms(self) -> list:
        return self.__rooms

    def get_available_rooms(self, start: str, end: str) -> list:
        # Beispielhafte Logik: nur freie Zimmer zurückgeben
        return [room for room in self.__rooms if room.is_available(start, end)]

    def add_room(self, room):
        self.__rooms.append(room) # APpend um neue Zimmer zu speichern ohne die alten zu löschen
