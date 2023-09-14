#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    # dictionaries
    ths = {"MMM": 3000, "MM": 2000, "M": 1000}
    hnds = {"CM": 900, "DCCC": 800, "DCC": 700,
            "DC": 600, "D": 500, "CD": 400,
            "CCC": 300, "CC": 200, "C": 100}
    tns = {"XC": 90, "LXXX": 80, "LXX": 70,
           "LX": 60, "L": 50, "XL": 40,
           "XXX": 30, "XX": 20, "X": 10}
    ut = {"IX": 9, "VIII": 8, "VII": 7, "VI": 6,
          "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1}

    listOfRomans = [ut, tns, hnds, ths]
    sum = 0
    i = 0
    while i < len(roman_string):
        for dic in listOfRomans:
            for key, value in dic.items():
                if roman_string.startswith(key, i):
                    sum += value
                    i += len(key)
                    break
    return sum
