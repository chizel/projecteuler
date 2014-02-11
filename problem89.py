#! /usr/bin/env python
# -*- coding: utf-8 -*-

class RomanNumbers():
    def __init__(self, roman):
        self.set_roman(roman)

    def set_roman(self, roman):
        self.roman = roman

    def set_arabic(self, arabic):
        self.arabic = arabic

    def convert_roman_to_arabic(self):
        self.arabic = []

        for number in self.roman:
            result = number
            self.arabic.append(result)

    def convert_arabic_to_roman(self):
        self.roman_numbers = []

        for number in self.arabic:
            result = number
            self.roman_numbers.append(result)

    roman_to_arabic = {
            'I':1, 'V':5, 'X':10, 'L':50,
            'C':100, 'D':500, 'M':1000
            }
 
    roman_to_arabic_once = {
            'IV':4, 'IX':9, 'XL':40,
            'XC':90, 'CD':400, 'CM':900
            }

    def arabic_to_roman(self, number):
        if number >= 4000:#what bound????
            return

        if number > == 1000:
            for i in range(0, number/3):
                result += 'M'
            number %= 1000

        if number >= 900:
            result += 'CM'
            number %= 100

        if number >= 500:
            result += 'D'
            number %= 100
        elif number >= 400:
            result += 'CD'
            number %= 100

        if number >= 'XC':
            result += 'XC'
            number %= 10

            'I':1, 'V':5, 'X':10, 'L':50,
            'IV':4, 'IX':9, 'XL':40,


        while number:
            tmp = number % 10
            number %= 10

    #def roman_to_arabic(roman):
        #res = []

        #for number in roman:
      #      pass
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

