#! /usr/bin/env python
# -*- coding: utf-8 -*-

class RomanNumbers():
    roman_to_arabic = {
            'I':1, 'IV':4, 'V':5,
            'IX':9, 'X':10, 'XL':40,
            'L':50, 'XC':90, 'C':100,
            'CD':400, 'D':500, 'CM':900,
            'M':1000}

    def __init__(self, roman):
        self.set_roman(roman)

    def set_roman(self, roman):
        self.roman = roman

    def set_arabic(self, arabic):
        self.arabic = arabic

    def convert_roman_to_arabic(self):
        self.arabic = []

        for number in self.roman:
            #result = number
            self.arabic.append(result)

    def convert_arabic_to_roman(self):
        self.roman_numbers = []

        for number in self.arabic:
            #result = number
            self.roman_numbers.append(result)

    def arabic_to_roman(self, number):
        if number > 4000:#what bound????
            return

        #while number:
            #tmp = number % 10
            #number %= 10

    def roman_to_arabic(roman):
        res = []

        for number in roman:
            pass
def main():
#    romain_numbers = []

    #with open('roman.txt', 'r') as f:
        #for line in f:
            #romain_numbers.append(line[:-1])

    p = RomanNumbers([])
    arabic = [1,2,3,4,9,10,40,40, 90, 88]
    p.set_arabic(arabic)
    p.convert_arabic_to_roman()
    

    return

if __name__ == "__main__":
    main()

