from airreservation.fligth import Flight


from airreservation.helpers import card_printer
from airreservation.planes.airbusA319 import AirbusA319
from airreservation.planes.boeing777 import Boeing777


f = Flight("LH1344", Boeing777("NYC"))
print(f.get_aircraft_model())

f = Flight("BA758", AirbusA319("G-EUPP"))
print(f.get_aircraft_model())
print(f.get_airline())
print(f.get_number())
f.allocate_seats("12C", "Jan Nowak")
f.allocate_seats("1A", "Julian Nowak")
f.allocate_seats("15D", "Janek Nowak")
f.allocate_seats("8B", "Roman Dzieciol")
f.allocate_seats("3E", "Alex Kowlski")
f.allocate_seats("20F", "John Smith")
print(f._seating)
print(f.num_avilable_seats())
#print(f.relocate_passenger("12C", "18E"))
#f.make_boarding_cards(card_printer("Jan Nowak", "12C", "AF72", "Antonow"))
f.make_boarding_cards(card_printer)