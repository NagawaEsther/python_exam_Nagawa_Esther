            #ai)
def calculate_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score >= 50 and score <= 59:
        return "E"
    else:
        return "Fail"

score = float(input("Enter student's score (0-100): "))
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    grade = calculate_grade(score)
    print(f"The student's grade is: {grade}")


            #ii)
def celsius_to_fahrenheit(celsius):
    "Convert temperature from Celsius to Fahrenheit."
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    "Convert temperature from Fahrenheit to Celsius."
    return (fahrenheit - 32) * (5/9)

try:
    choice = input("Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius: ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")


                    #bi)
def calculate_triangle_area(base, height):
    "Calculate the area of a triangle."
    return 0.5 * base * height

try:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area}")
except ValueError:
    print("Invalid input. Please enter numeric values for base and height.")

                # bii)
def sum_list(numbers):
    "Calculate the sum of all numbers in a list."
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [9, 2, 3, 5, 8]
result = sum_list(sample_list)
print("The sum of all numbers in the list is:", result)
