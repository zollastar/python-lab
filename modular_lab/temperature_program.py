def convert_to_celsius(fahrenheit: float) -> float:
    """Return the number of Celsius degrees equivalent to fahrenheit
    degrees.

    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius: float) -> bool:
    """Return True if temperature celsius degrees is above freezing.
    above_freezing(5.2)
    True
    above_freezing(-2)
    False
    """
    return celsius > 0

if __name__ == '__main__':
    fahrenheit = float(input('Enter the temperature in degree Fahrenheit: '))
    celcius = convert_to_celsius(fahrenheit)
    if (above_freezing(celcius)):
        print('It is above freezing')
    else:
        print('It is below freezing')
