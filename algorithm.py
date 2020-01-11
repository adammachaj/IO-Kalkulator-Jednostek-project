import prefix

def returnResult(inputValue, inputPrefix, outputPrefix):
    x = prefix.prefixes[inputPrefix] / prefix.prefixes[outputPrefix]
    wynik = x * inputValue

    return wynik
