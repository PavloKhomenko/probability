import math


def probability():
    probabilities = []
    for i in range(0, 7):
        probabilities.append(math.comb(6, i) * math.comb(46, 6 - i) / math.comb(52, 6))
    return probabilities


def expected_value(probabilities):
    value = 0
    for i, j in enumerate(prizes):
        value += probabilities[i] * (prizes[i] - 30)
    return value


def variance(probabilities, avg):
    var = 0
    for i, j in zip(prizes, probabilities):
        var += (avg - i) ** 2 * j
    return var


prizes = [0, 0, 38, 72, 1831, 39692, 20595669]
probabilities = probability()
mean = expected_value(probabilities)
var = variance(probabilities, mean)
result = f'Var {var},\nStdev {var ** 0.5}\nExpected value: {mean}\n'
print(result)