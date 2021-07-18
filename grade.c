#include <cs50.h>
#include <stdio.h>

char calculate(int grades[], int n);

int main(void)
{
    // Get number of subjects
    int n = get_int("Number of subjects: ");

    // Declare grades array for n subjects
    int grades[n];

    // Get each number grade from user
    for (int i = 0; i < n; i++)
    {
        grades[i] = get_int("Subject %i Grade: ", i + 1);
    }

    // Print out letter average
    printf("Your letter average is: %c\n", calculate(grades, n));
}

char calculate(int grades[], int n)
{
    // Get numeric average
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += grades[i];
    }
    float avg = (float) sum / n;

    // Determine letter grade
    if (avg >= 90)
    {
        return 'A';
    }
    if (avg >= 80)
    {
        return 'B';
    }
    if (avg >= 70)
    {
        return 'C';
    }
    if (avg >= 65)
    {
        return 'D';
    }
    return 'F';
}
