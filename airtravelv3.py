#!/usr/bin/python3
"""
from airtravel import *
f=Flight("AB2345",Aircraft("G-EUPT","Airbus A319",num_rows=12,num_seats_per_row=6))

from airtravel import console_card_printer, make_flight
f=make_flights()

f.make_boarding_cards(console_card_printer)

a=AirbusA319i("AA123")

a.num_seats()

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


#Base Class
class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

# Derived Classes
class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1,56),"ABCDEFGHJK"

def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A","Scoffers van Partner")
    f.allocate_seat("15F","John Spedan Lewis")
    f.allocate_seat("15E","Willian A Rose")
    f.allocate_seat("1C","Leonard Graces Phillips")
    f.allocate_seat("1D","Barney Rubble esq")
    

    g = Flight("AF123", Boeing777("F-FIPS"))
    g.allocate_seat("55K","Rene van der Kerkoff")
    g.allocate_seat("55J","Willie van der Kerkoff")
    g.allocate_seat("33C","Yorkie Pudding Lewis")
    g.allocate_seat("5E","Orinoco Badger")
    
    return f,g


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
