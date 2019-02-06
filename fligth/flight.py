class Flight:
    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        print(self._seating)

    def get_number(self):
        return self._number

    def get_airline(self):
        return self._number[:2]

    def get_aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):

        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format((row_text)))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seats(self, seat, passenger):
        # parse if the seat exists
        # in not empty
        # assign a passenger

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):

    # z miejsca na miejsce
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to allocate from {}".format((from_seat)))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[from_row][from_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_avilable_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        # card_printer
        for row, letter, passenger in sorted(self._passenger_seats(), key=lambda x: (x[0], x[1])):
            card_printer(passenger, "{}{}".format(row, letter), self.get_number(), self.get_aircraft_model())

    def _passenger_seats(self):
        # yield (passenger, "{}{}".format(row, letter)
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (row, letter, passenger)

