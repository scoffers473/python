#!/usr/bin/python3
"""
from airtravel import *
f=Flight("AB2345",Aircraft("G-EUPT","Airbus A319",num_rows=12,num_seats_per_row=6))

from airtravel import console_card_printer, make_flight
f=make_flight()

f.make_boarding_cards(console_card_printer)


""" 

class Flight():
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No Airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid Airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None]  +[{letter: None for letter in seats} for _ in rows]




    def number(self):
        return self._number



    def airline(self):
        return (self._number[:2])



    def aircraft_model(self):
        return self._aircraft.model()



    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text) 
        except ValueError:
           raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".fornat(row))
        
        return row, letter



    def allocate_seat(self, seat, passenger):

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already allocated".format(seat))
        self._seating[row][letter] = passenger



    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger os in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft():
    def __init__(self,registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model=model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return self._registration


    def model(self):
        return self._model


    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A","Scoffers van Partner")
    f.allocate_seat("15F","John Spedan Lewis")
    f.allocate_seat("15E","Willian A Rose")
    f.allocate_seat("1C","Leonard Graces Phillips")
    f.allocate_seat("1D","Barney Rubble esq")
    
    return f


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"        \
             "  Flight: {1}"      \
             "  Seat: {2}"        \
             "  Aircraft: {3}"    \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) -2) + '+'
    border = '|' + '-' * (len(output) -2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
