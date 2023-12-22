import math
import pandas as pd

tsv_path = 'data.tsv'
df = pd.read_csv(tsv_path, sep='\t', header=None)


def dataframe_to_dict(df):
    df.columns = df.iloc[0].str.strip()
    df = df.drop(0)
    data_dict = df.to_dict(orient='list')
    for key, values in data_dict.items():
        data_dict[key] = [convert_value(value) for value in values]
    return data_dict


def convert_value(value):
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return value


data_dict = dataframe_to_dict(df)


def probability_expected(data1: list, temp):
    prob = []
    exp = []
    for j, i in enumerate(data1):
        if i == '-':
            break
        value = (math.comb(len(data1) - data1.count('-'), j + 1) / math.comb(temp, j + 1))
        prob.append(value)
        exp.append(value * i - 1)
    return prob, exp


def variance(probabilities, prizes):
    var = []
    for i, j in zip(prizes, probabilities):
        if i == '-':
            break
        avg = i * j
        var.append((avg - i) ** 2 * j + avg ** 2 * (1-j))
    return var


temp = 9
for name in data_dict.keys():
    if 'Серія' not in name:
        continue
    elif 'Г' in name:
        temp = 16
    elif 'З' in name:
        temp = 25
    prob_exp = probability_expected(data_dict[name], temp)
    var = variance(prob_exp[0], data_dict[name])
