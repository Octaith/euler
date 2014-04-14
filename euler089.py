roman = (
    ('M',  1000),
    ('CM', 900),
    ('D',  500),
    ('CD', 400),
    ('C',  100),
    ('XC', 90),
    ('L',  50),
    ('XL', 40),
    ('X',  10),
    ('IX', 9),
    ('V',  5),
    ('IV', 4),
    ('I',  1)
)


def roman_to_dec(s):
    result = 0
    index = 0
    for numeral, integer in roman:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


def dec_to_roman(n):
    result = ""
    for numeral, integer in roman:
        while n >= integer:
            result += numeral
            n -= integer
    return result


with open('roman.txt') as f:
    data = f.read().split('\n')

saved = 0
for r in data:
    saved += len(r)
    saved -= len(dec_to_roman(roman_to_dec(r)))

print saved
