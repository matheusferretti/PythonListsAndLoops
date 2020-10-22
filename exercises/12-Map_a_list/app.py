Celsius_values = [-2,34,56,-10]



def fahrenheit_values(value):
# the magic go here:
    fahrenheit = (value * 9/5) + 32
    return fahrenheit
result = map(fahrenheit_values, Celsius_values)
result = list(result)
print(result)
