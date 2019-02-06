from airreservation.aircraft import Aircraft

class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A-319"

    def seating_plan(self):
        return range(1,24), "ABCDEF"