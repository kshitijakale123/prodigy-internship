def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Welcome to the Temperature Conversion Program")
    print("Enter the temperature value and the original unit of measurement:")
    value = float(input("Temperature value: "))
    unit = input("Original unit of measurement (Celsius, Fahrenheit, Kelvin): ").lower()

    if unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    elif unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
    elif unit == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")
    else:
        print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")

if __name__ == "__main__":
    main()
