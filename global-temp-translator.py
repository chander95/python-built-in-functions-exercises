#Use f-strings for output and apply this to a practical scenario of temp conversion
#(0°C × 9/5) + 32

initial_temp = input("Please enter a temperature in Celsius: ")
initial_temp = int(initial_temp)

def c_to_f():
    new_temp = initial_temp * (9/5) + 32
    print(f"The temperature in Farenheit is {new_temp} degrees.")

c_to_f()