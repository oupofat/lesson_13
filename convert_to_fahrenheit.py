def convert_to_fahrenheit(c):
    fahrenheit = c * 9/5 + 32
    print(fahrenheit,"is", c,)
c = float(input("How hot is it in °C? "))
convert_to_fahrenheit(c)