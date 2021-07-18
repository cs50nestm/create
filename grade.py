from cs50 import get_int
import time


def main():

    # Instructions for user
    print("\nCONVERT YOUR NUMBER GRADES TO A LETTER AVERAGE!\n")

    # Check for valid input
    while True:
        n = get_int("Number of Grades: ")
        if 0 < n < 10:
            break
        print("Please enter number between 1 and 9.")

    # Create grades list and add numeric grades
    grades = []
    for i in range(n):
        grades.append(get_int(f"Number Grade {i + 1}: "))

    # A fun device to humanize computer
    print("\nCalculating...\n")
    time.sleep(1)

    # Call to letter function and assign return value
    letter_average = letter(grades)

    # Final output is letter grade
    print("Letter Grade:", letter_average)


# Calculate letter grade
def letter(grades):

    # Initialize sum to zero
    sum = 0

    # Iterate through grades list and add each to sum
    for grade in grades:
        sum += grade

    # Computer average numeric grade
    average = sum / len(grades)

    # Assign appropriate letter grade, depending on average
    if average >= 90:
        letter_avg = 'A'
    elif average >= 80:
        letter_avg = 'B'
    elif average >= 70:
        letter_avg = 'C'
    elif average >= 65:
        letter_avg = 'D'
    else:
        letter_avg = 'F'

    # Return the letter grade
    return letter_avg


main()


