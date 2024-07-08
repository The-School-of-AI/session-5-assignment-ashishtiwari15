import time
import re
import inspect
import math

def time_it(fn, *args, repetitions=1, **kwargs):
    """This is a generalized function to call any function user specified number of times and return the average time taken for calls"""
    if repetitions < 0:
        raise ValueError("repitions should be a positive number greater than 0")
    if repetitions == 0:
        return 0
    if fn is None:
        raise ValueError("Error:- required positional argument: 'fn' is None")
    if (fn not in dir() and not inspect.isfunction(fn) and not callable(fn)):
        raise NameError("Error:- required positional argument: 'fn' is not defined")
    if len(args) == 0:
        raise NameError("Empty arguments received")
    if len(kwargs.items()) == 0:
        raise NameError("Empty keyword arguments received")
    execution_times = []
    for _ in range(repetitions):
        start_time = time.perf_counter()
        response = fn(*args, **kwargs)
        end_time = time.perf_counter()
        execution_times.append(end_time-start_time)
    average_time = sum(execution_times)/len(execution_times)
    return average_time

def squared_power_list(number, *args, start=0, end=5, **kwargs):

    """Returns list by raising number to power from start to end -> number**start to number**end. Default start is 0 and end is 5"""
    if number is None:
        raise TypeError("Missing required positional argument: 'number'")
    if len(args) > 0:
        raise TypeError("squared_powered_list takes maximum 1 positional arguments")
    if len(kwargs.items()) > 0:
        raise TypeError("squared_powered_list takes maximum 2 keyword/named arguments")
    if not isinstance(number, int):
        raise TypeError(" Only integer type arguments are allowed ")
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")
    if start > end:
        raise ValueError("Value of start should be less than end")
    if number > 10:
        raise ValueError("Value of number should be less than 10")
    # Logic
    squaring_function = lambda x, y: x**y
    response = [squaring_function(number, a) for a in range(start, end)]
    print("Here =>", response)
    return response

def polygon_area(length, *args, sides=3, **kwargs):
    """Returns area of a regular polygon with number of sides between 3 to 6 both inclusive"""
    if length is None:
        raise TypeError("required positional argument: 'length'")
    if not isinstance(length, int):
        raise TypeError("Only integer type arguments are allowed")
    if sides is None:
        raise TypeError("required positional argument: 'length'")
    if not isinstance(sides, int):
        raise TypeError("error: Only integer type arguments are allowed")
    if length <= 0:
        raise ValueError("Length of side of the Polygon should be more than 0")
    if sides < 3:
        raise ValueError("A polygon must have atleast 3 sides")
    if len(args) > 0:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    # Logic
    apothem = length / (2 * math.tan(math.pi / sides))
    area = 0.5 * sides * length * apothem
    return area

def temp_converter(temp, *args, temp_given_in='f', **kwargs):
    """Converts temperature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius"""
    if temp is None:
        raise TypeError("required positional argument: 'temp'")
    if temp_given_in is None:
        raise TypeError("required positional argument: 'temp_given_in'")
    if not isinstance(temp, int):
        raise TypeError("Only integer type arguments are allowed")
    if not isinstance(temp_given_in, str):
        raise TypeError("Charcater string expected")

    # Converting temp_given_in to lower case
    temp_given_in = temp_given_in.lower()

    if temp_given_in not in ['f', 'c']:
        raise ValueError("Only f or c is allowed")
    if temp_given_in in ['c'] and temp < -273.15:
        raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
    if temp_given_in in ['f'] and temp < -459.67:
        raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    if len(args) > 0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")
    # Logic
    if temp_given_in == 'c':
        response = (temp * 9/5) + 32
    elif temp_given_in == 'f':
        response = (temp - 32) * 5/9
    else:
        response = 0
    return response

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 299792.458:
        raise ValueError("Speed can't be greater than speed of light")

    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")

    # Converting dist to lower case
    dist = dist.lower()

    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowe")

    if not isinstance(time, str):
        raise TypeError("Charcater string expected")

    # Converting time to lower case
    time = time.lower()

    if time not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    if len(args) > 0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs.items()) > 0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    # Logic
    if dist == 'km':
        if time == 'ms':
            converted_speed = speed // 3600000
        elif time == 's':
            converted_speed = speed // 3600
        elif time == 'min':
            converted_speed = speed // 60
        elif time == 'hr':
            converted_speed = speed
        elif time == 'day':
            converted_speed = speed * 24

    elif dist == 'm':
        if time == 'ms':
            converted_speed = speed // 3600
        elif time == 's':
            converted_speed = speed / 3.6
        elif time == 'min':
            converted_speed = int(speed * 16.667)
        elif time == 'hr':
            converted_speed = speed * 1000
        elif time == 'day':
            converted_speed = speed * 24000

    elif dist == 'ft':
        if time == 'ms':
            converted_speed = round(speed/1097)
        elif time == 's':
            converted_speed = round(speed * 0.911344)
        elif time == 'min':
            converted_speed = round(speed * 54.6806649169)
        elif time == 'hr':
            converted_speed = round(speed * 3280.8398950131)
        elif time == 'day':
            converted_speed = round(speed * 78740.10)

    elif dist == 'yrd':
        if time == 'ms':
            converted_speed = round(speed / 3292)
        elif time == 's':
            converted_speed = round(speed / 3.292)
        elif time == 'min':
            converted_speed = round(speed * 18.2268883056)
        elif time == 'hr':
            converted_speed = round(speed * 1093.6132983377)
        elif time == 'day':
            converted_speed = round(speed * 26246.61916)

    return converted_speed