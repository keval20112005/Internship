import temp_converter as tc

def menu():
    print("----- Temperature Unit Converter -----")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    return choice

def main():
    while True:
        choice = menu()

        if choice == '1':
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", tc.celsius_to_fahrenheit(c))

        elif choice == '2':
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", tc.fahrenheit_to_celsius(f))

        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print("Kelvin:", tc.celsius_to_kelvin(c))

        elif choice == '4':
            k = float(input("Enter Kelvin: "))
            print("Celsius:", tc.kelvin_to_celsius(k))

        elif choice == '5':
            print("Exiting the converter.")
            break

        else:
            print("Invalid choice. Try again.\n")

main()
