class Solution:
    def romanToInt(self, s: str) -> int:
        #create dictionary to store the character values
        roman_values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num=0
        last="I"

        for numeral in s[::-1]:
            if roman_values[numeral]< roman_values[last]:
                num -=roman_values[numeral]
            else:
                num += roman_values[numeral]
            last= numeral
        return num
