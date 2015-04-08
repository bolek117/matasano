# Description: Less number of points is better
__author__ = 'mwitas'
import string


def simple_score(data):
    result = 0
    for i in range(0, len(data)):
        if data[i] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 ':
            pass
        elif data[i] in string.printable:
            result += 1
        else:
            result += 2

    return result


def frequency_score(data):
    lookup = {'A': 0.6433070866141732,
              'B': 0.1015748031496063,
              'C': 0.21889763779527557,
              'D': 0.3346456692913386,
              'E': 1.0,
              'F': 0.17559055118110237,
              'G': 0.15905511811023623,
              'H': 0.4795275590551181,
              'I': 0.5488188976377952,
              'J': 0.011811023622047244,
              'K': 0.060629921259842526,
              'L': 0.31732283464566935,
              'M': 0.18976377952755907,
              'N': 0.531496062992126,
              'O': 0.5913385826771653,
              'P': 0.15196850393700786,
              'Q': 0.007874015748031498,
              'R': 0.47165354330708664,
              'S': 0.4984251968503937,
              'T': 0.7133858267716536,
              'U': 0.2173228346456693,
              'V': 0.07716535433070866,
              'W': 0.1858267716535433,
              'X': 0.011811023622047244,
              'Y': 0.1551181102362205,
              'Z': 0.005511811023622048
              }

    data = data.upper()

    frequencies = {}
    for i in string.ascii_uppercase:
        frequencies[i] = 0

    score = 0.0
    max_value = 1
    count = len(data)
    for i in xrange(0, len(data)):
        char = data[i]

        if char in string.ascii_uppercase:
            count += 1
            frequencies[char] += 1
            if frequencies[char] > max_value:
                max_value = frequencies[char]
        elif char in string.printable:
            score += 1
        else:
            score += 2

    # Normalize frequencies and generate scores
    for i in frequencies:
        frequencies[i] /= max_value
        score += abs(frequencies[i] - lookup[i])

    return score