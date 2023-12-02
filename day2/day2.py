import re

def game_line_value(line: str, max_red: int, max_green: int, max_blue: int) -> int: 
    line = line.strip().split(":")

    id = int(line[0].replace("Game ", ""))

    subsets = line[1].strip().split(";")
    
    for subset in subsets:
        cube_colors = subset.split(",")
        for cube_color in cube_colors:
            if "red" in cube_color:
                if int(cube_color.replace("red", "")) > max_red:
                    return 0
            if "blue" in cube_color:
                if int(cube_color.replace("blue", "")) > max_blue:
                    return 0
            if "green" in cube_color:
                if int(cube_color.replace("green", "")) > max_green:
                    return 0
    return id

with open("./input.txt", "r") as file:
    count = 0

    while True:
        line = file.readline()
        
        # If there are no more lines, stop
        if not line:
            break

        count += game_line_value(line, 12, 13, 14)

    print(f"The sum of ids is {count}")
