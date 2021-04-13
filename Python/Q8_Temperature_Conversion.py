def cel_to_fah(celsius):
    c = celsius
    f = c * (9 / 5) + 32
    print("The converted temperature is ",f,"°F")

def fah_to_cel(fahrenheit):
    f = fahrenheit
    c = (f - 32) * (5 / 9)
    print("The converted temperature is ",c,"°C")

def main():
    print("What temperature are you converting to?")
    userInput = input("Enter 'celsius' or 'fahrenheit': ")

    if userInput == 'celsius':
        temp = int(input("Please enter the temperature: "))
        fah_to_cel(temp)
    elif userInput == 'fahrenheit':
        temp = int(input("Please enter the temperature: "))
        cel_to_fah(temp)

main()