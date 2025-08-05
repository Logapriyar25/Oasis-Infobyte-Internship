# bmi_calculator.py

def calculate_bmi(weight, height):
    """Calculate BMI and return both BMI value and category."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

def main():
    print("=== BMI CALCULATOR ===")
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height_cm = float(input("Enter your height in meters: "))
            height = height_cm / 100 
            if weight <= 0 or height <= 0:
                print("⚠️ Weight and height must be positive numbers.\n")
                continue
            bmi, category = calculate_bmi(weight, height)
            print(f"\nYour BMI is: {bmi}")
            print(f"Category: {category}\n")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values only.\n")

        choice = input("Do you want to calculate again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using the BMI Calculator. Stay healthy! 💪")
            break

if __name__ == "__main__":
    main()
