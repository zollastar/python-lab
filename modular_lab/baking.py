import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """Return instructions for preheating the oven  in fahrenheit degrees and
    Celcius degrees.
    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'    
    """
    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return f'Preheat oven to {fahr} degrees F ({cels} degrees C).'

fahr = float(input('Enter the baking temperature in degree Fahrenheit: '))
print(get_preheating_instructions(fahr))
print('It is below freezing')
