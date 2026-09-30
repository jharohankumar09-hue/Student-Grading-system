
### `statement.md`

```markdown
# Problem Statement

## Student Grade Calculator

Create a Python program that accepts the marks/scores of five subjects from the user and calculates the student's average percentage.

Based on the calculated percentage, the program should assign a grade according to the following grading system:

- 90 to 100: Grade A
- 80 to below 90: Grade B
- 70 to below 80: Grade C
- 60 to below 70: Grade D
- 50 to below 60: Grade E
- Below 50: Grade F - Fail

The program should also determine and display the highest and lowest scores attained among the five subjects.

The highest and lowest scores must be calculated without using the built-in `min()` and `max()` functions. The program should use comparison statements such as `if` statements to determine these values.

In addition, the program should display a random motivational message, the current date, and a final thank-you message.

## Objectives

The objectives of this project are:

1. To take multiple numerical inputs from the user.
2. To calculate the average percentage of five scores.
3. To use conditional statements for grade calculation.
4. To find the highest score using comparison logic.
5. To find the lowest score using comparison logic.
6. To use the `random` module to display a motivational message.
7. To use the `datetime` module to display the current date.
8. To use the `time` module to add a short delay.
9. To practice basic Python programming concepts.

## Input

The program accepts five numerical values:

- First subject score
- Second subject score
- Third subject score
- Fourth subject score
- Fifth subject score

## Processing

The program calculates the percentage using:

```text
percentage = (num_1 + num_2 + num_3 + num_4 + num_5) / 5