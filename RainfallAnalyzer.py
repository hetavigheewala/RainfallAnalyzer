

def main():
    # Loop until valid input for number of weeks (1-4) is provided
    while True:
        try:
            num_weeks = int(input("Enter the number of weeks (1-4): "))
            if 1 <= num_weeks <= 4:
                break  # Exit loop if input is valid
            else:
                print("Please enter a valid number of weeks between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number of weeks.")

    total_rainfall = 0

    # Loop through each week based on the number of weeks provided
    for week in range(1, num_weeks + 1):
        # Ask for the rainfall in centimeters for the current week
        rainfall = float(input(f"Enter the rainfall in centimeters for week {week}: "))
        total_rainfall += rainfall  # Add current week's rainfall to the total
        
        # Print a message if the rainfall is more than 3 centimeters
        if rainfall > 3:
            print(f"Rainfall in week {week} was more than 3 centimeters.")

    # Display the total rainfall for the specified number of weeks
    print(f"Total rainfall for {num_weeks} weeks: {total_rainfall} centimeters")

if __name__ == "__main__":
    main()
