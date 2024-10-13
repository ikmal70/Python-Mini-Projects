def calculate_bmi(weight, height):
    # Calculate BMI using the formula
    bmi = weight / (height ** 2)
    
    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

def main():
    print(":: WELCOME TO BMI CALCULATOR APP ::\n")
    user_weight = float(input("|> Enter your weight (kg): "))
    user_height = float(input("|> Enter your height (m): "))
    calculate_bmi(user_weight, user_height)

if __name__ == "__main__":
    main()