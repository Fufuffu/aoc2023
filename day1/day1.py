import re
import os

count = 0

with open("./input.txt", "r") as file:
    while True:
        line = file.readline()
        
        # If there are no more lines, stop
        if not line:
            break

        first_digit = re.search(r"\d", line).group()
        last_digit = re.search(r"\d", line[::-1]).group()

        count += int(first_digit + last_digit)

    print(f"The calibration number was: {count}")
