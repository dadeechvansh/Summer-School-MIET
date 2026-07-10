import temperature
# or
import temperature as tmp

# help(temperature)

x=tmp.celsius_to_fahrenheit(100)
print(x)
 
y=tmp.fahrenheit_to_celsius(50)
print(y) 

print(tmp.FREEZING_POINT_CELSIUS)
print(tmp.FREEZING_POINT_FAHRENHEIT)
print(tmp.BOILZING_POINT_CELSIUS)
print(tmp.BOILING_POINT_FAHRENHEIT)
