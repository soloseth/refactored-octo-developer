import csv

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

# Generate temperature conversion data using a for loop
celsius_values = list(range(-200, 200 + 1, 1))
fahrenheit_values = [celsius_to_fahrenheit(c) for c in celsius_values]

#function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit2):
    return (fahrenheit2 - 32) * 5 / 9

fahrenheit2_values = list(range(-200, 200 + 1, 1))
celsius2_values = [fahrenheit_to_celsius(f) for f in fahrenheit2_values]



# Store data in different structures
temp_list_tuples = [(c, f) for c, f in zip(celsius_values, fahrenheit_values)] #structure of tuple, parameters for list_of_tuples creation
temp_tuple = (celsius_values, fahrenheit_values)
temp_dict1 = {c: f for c, f in zip(celsius_values, fahrenheit_values)}
temp_dict2 = {f: c for f, c in zip(fahrenheit2_values, celsius2_values)}
temp_list_tuples2 = [(c, f) for c, f in zip(celsius2_values, fahrenheit2_values)]

# Display stored data
print("\nTemperature data from list of tuples:")
for c, f in temp_list_tuples:
    print(f"{c}°C -> {f}°F")

print("\nTemperature data from dictionary:")
for c, f in temp_dict1.items():
    print(f"{c}°C -> {f}°F")

# Add new temperature (300°C) to data structures
new_celsius = 300                                    # Created new temp. value
new_fahrenheit = celsius_to_fahrenheit(new_celsius)  #Converted to fahrenheit

temp_list_tuples.append((new_celsius, new_fahrenheit))
temp_dict1[new_celsius] = new_fahrenheit

while True:
    print("""
    TEMPERATURE DATA HUB
    Please select an operation:
    1. Convert Temperature
    2. Sort Temperature Data
    3. Export Temperature Data
    4. Close Program
    """)

    choice = input("Choice: ")
    if choice == "1":
        print("""
Please choose:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
        """)
        conversion = input("Choice: ")

        if conversion == "1":
            # User input to retrieve Fahrenheit value
            user_celsius = int(input("\nEnter a Celsius value to retrieve Fahrenheit: "))

            # Retrieve from dictionary
            if user_celsius in temp_dict1:
                print(
                    f"From dictionary: {user_celsius}°C -> {temp_dict1[user_celsius]}°F")  # output is value of key(user_celsius) in dictionary
            else:
                print("Value not found in dictionary.")

            # Retrieve from list of tuples
            found = False
            for c, f in temp_list_tuples:
                if c == user_celsius:
                    print(f"From list of tuples: {user_celsius}°C -> {f}°F")
                    found = True
                    break
            if not found:
                print("Value not found in list of tuples.")


        elif conversion == "2":
            # User input to retrieve Fahrenheit value
            user_fahrenheit = int(input("\nEnter a Fahrenheit value to retrieve Celsius: "))

            # Retrieve from dictionary
            if user_fahrenheit in temp_dict2:
                print(
                    f"From dictionary: {user_fahrenheit}°F -> {temp_dict2[user_fahrenheit]}°C ")
            else:
                print("Value not found in dictionary.")

            # Retrieve from list of tuples
            found = False
            for c, f in temp_list_tuples2:
                if f == user_fahrenheit:
                    print(f"From list of tuples: {user_fahrenheit}°F -> {c}°C")
                    found = True
                    break
            if not found:
                print("Value not found in list of tuples.")


        else:
            print("Invalid conversion choice")

    elif choice == "2":
        # Sorting options
        sort_option = input("\nSort data by Celsius or Fahrenheit? (C/F): ").strip().upper()
        sort_order = input("Sort in ascending or descending order? (A/D): ").strip().upper()

        if sort_option == "C":
            temp_list_tuples.sort(key=lambda x: x[0], reverse=(sort_order == "D"))
        elif sort_option == "F":
            temp_list_tuples.sort(key=lambda x: x[1], reverse=(sort_order == "D"))

        # Display sorted data
        print("\nSorted Temperature Data:")
        for c, f in temp_list_tuples:
            print(f"{c}°C -> {f}°F")

    elif choice == "3":
        # Export to CSV
        export_choice = input("\nWould you like to export the data to CSV? (Y/N): ").strip().upper()
        if export_choice == "Y":
            filename = "temperature_data.csv"
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Celsius", "Fahrenheit"])
                writer.writerows(temp_list_tuples)
            print(f"Data successfully exported to {filename}.")

    elif choice == "4":
        break

    else:
        print("invalid choice")