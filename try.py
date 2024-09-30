import babypy as easy

def main_menu():
    easy.say("Welcome to the PyEasy Conversion and Calculation App!")
    options = [
        "Temperature Conversion",
        "Length Conversion",
        "Basic Calculator",
        "List Operations",
        "String Operations",
        "Exit"
    ]
    
    while True:
        choice = display_menu("Main Menu", options)
        if choice == 1:
            temperature_conversion()
        elif choice == 2:
            length_conversion()
        elif choice == 3:
            basic_calculator()
        elif choice == 4:
            list_operations()
        elif choice == 5:
            string_operations()
        elif choice == 6:
            easy.say("Thank you for using PyEasy Conversion and Calculation App. Goodbye!")
            break
        
        if choice != 6:
            easy.ask("\nPress Enter to continue...")

def display_menu(title, options):
    while True:
        easy.say(f"\n{title}:")
        for i, option in enumerate(options, 1):
            easy.say(f"{i}. {option}")
        try:
            choice = easy.make_number(easy.ask(f"Enter your choice (1-{len(options)})"))
            if easy.is_inside(choice, easy.count_from_to(1, len(options))):
                return choice
            else:
                easy.say("Invalid choice. Please try again.")
        except:
            easy.say("Invalid input. Please enter a number.")

def get_number(prompt):
    while True:
        try:
            return easy.make_number(easy.ask(prompt))
        except:
            easy.say("Invalid input. Please enter a number.")

def temperature_conversion():
    easy.say("\nTemperature Conversion")
    temp = get_number("Enter the temperature")
    unit = easy.say_loudly(easy.ask("Enter the unit (C for Celsius, F for Fahrenheit)"))
    
    if unit == "C":
        result = (temp * 9/5) + 32
        easy.say(f"{temp}°C is equal to {easy.make_rounder(result, 2)}°F")
    elif unit == "F":
        result = (temp - 32) * 5/9
        easy.say(f"{temp}°F is equal to {easy.make_rounder(result, 2)}°C")
    else:
        easy.say("Invalid unit. Please use C or F.")

def length_conversion():
    easy.say("\nLength Conversion")
    length = get_number("Enter the length")
    unit = easy.say_loudly(easy.ask("Enter the unit (M for meters, FT for feet)"))
    
    if unit == "M":
        result = length * 3.28084
        easy.say(f"{length} meters is equal to {easy.make_rounder(result, 2)} feet")
    elif unit == "FT":
        result = length / 3.28084
        easy.say(f"{length} feet is equal to {easy.make_rounder(result, 2)} meters")
    else:
        easy.say("Invalid unit. Please use M or FT.")

def basic_calculator():
    easy.say("\nBasic Calculator")
    num1 = get_number("Enter the first number")
    num2 = get_number("Enter the second number")
    op = easy.ask("Enter the operation (+, -, *, /)")
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            easy.say("Error: Division by zero!")
            return
    else:
        easy.say("Invalid operation.")
        return
    
    easy.say(f"Result: {num1} {op} {num2} = {easy.make_rounder(result, 2)}")

def list_operations():
    easy.say("\nList Operations")
    numbers = []
    for i in easy.count_from_to(1, 10):
        num = get_number(f"Enter number {i} (or 0 to finish)")
        if num == 0:
            break
        numbers.append(num)
    
    if not numbers:
        easy.say("No numbers entered.")
        return
    
    easy.say(f"Original list: {numbers}")
    easy.say(f"Sorted list: {easy.sort_stuff(numbers)}")
    easy.say(f"Reversed list: {easy.flip_order(numbers)}")
    easy.say(f"Sum of numbers: {easy.add_up(numbers)}")
    easy.say(f"Average of numbers: {easy.make_rounder(easy.find_middle(numbers), 2)}")
    easy.say(f"Minimum number: {easy.get_min(numbers)}")
    easy.say(f"Maximum number: {easy.get_max(numbers)}")

def string_operations():
    easy.say("\nString Operations")
    text = easy.ask("Enter a string")
    
    easy.say(f"Original string: {text}")
    easy.say(f"Uppercase: {easy.say_loudly(text)}")
    easy.say(f"Lowercase: {easy.say_quietly(text)}")
    easy.say(f"Pretty version: {easy.make_pretty(text)}")
    easy.say(f"Reversed: {''.join(easy.flip_order(text))}")
    easy.say(f"Length: {easy.count_letters(text)}")
    easy.say(f"Is it all numbers? {easy.all_yes([char.isdigit() for char in text])}")
    easy.say(f"Does it have any letters? {easy.any_yes([char.isalpha() for char in text])}")

if __name__ == "__main__":
    main_menu()