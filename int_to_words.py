WORDS = { 1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         15: "fifteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         80: "eighty"}

ORDER = [[0, ''],
         [3, 'thousand'],
         [6, 'million'],
         [9, 'billion'],
         [12, 'trillion'],
         [15, 'quadrillion'],
         [18, 'quintillion'],
         [21, 'sextillion'],
         [24, 'septillion'],
         [27, 'octillion'],
         [30, 'nonillion'],
         [33, 'decillion'],
         [36, 'undecillion'],
         [39, 'duodecillion'],
         [42, 'tredecillion'],
         [45, 'quattuordecillion'],
         [48, 'quindecillion'],
         [51, 'sexdecillion'],
         [54, 'septendecillion'],
         [57, 'octodecillion'],
         [60, 'novemdecillion'],
         [63, 'vigintillion']]
ORDER.reverse()

def _tens_to_words(n):
    result = ""
    try:
        result = WORDS[n]
    except KeyError:
        ones = n % 10
        if n // 10 == 1:
            result = WORDS[ones] + "teen"
        else:
            try:
                result = WORDS[n // 10 * 10]
            except KeyError:
                result = WORDS[n // 10]
                result += "ty"
            if ones > 0:
              result += "-" + WORDS[ones]
    
    return result

def int_to_words(n):
    if n >= 10 ** 66:
        raise ValueError("number too high to be expressed by words")
    if n == 0:
        return "zero"
    result = ""
    for o in ORDER:
        hundreds = n // 10 ** o[0]
        if hundreds > 0:
            if hundreds >= 100:
                result += WORDS[hundreds // 100] + " hundred "
            if hundreds % 100 > 0:
                result += _tens_to_words(hundreds % 100)
            result += " " + o[1] + " "
            n %= 10 ** o[0]

    return result.strip()

number = int(input('number: '))
#for number in range(999999999999999999999999999999999999999999999999999999999999999999):
    print(str(number) + ': ' + int_to_words(number))
