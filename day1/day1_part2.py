import re
import os

count = 0

def normalize_digit(digit: str) -> str:
    match digit:
        case "one": 
            return "1"
        case "two": 
            return "2"
        case "three": 
            return "3"
        case "four": 
            return "4"
        case "five": 
            return "5"
        case "six": 
            return "6"
        case "seven":
            return "7"
        case "eight": 
            return "8"
        case "nine":
            return "9"
        case _:
            return digit

with open("./input.txt", "r") as file:
    while True:
        line = file.readline()
        
        # If there are no more lines, stop
        if not line:
            break

        first_digit = re.search(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line).group(0)
        # .* is greedy, abuse that :)
        last_digit = re.search(r".*(\d|one|two|three|four|five|six|seven|eight|nine)", line).group(1)

        count += int(normalize_digit(first_digit) + normalize_digit(last_digit))

    print(f"The calibration number was: {count}")
