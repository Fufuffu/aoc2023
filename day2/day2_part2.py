def game_line_value(line: str) -> int: 
    line = line.strip().split(":")

    subsets = line[1].strip().split(";")
    
    current_max = {"red": -9999, "blue": -9999, "green": -9999}

    for subset in subsets:
        cube_colors = subset.split(",")
        for cube_color in cube_colors:
            if "red" in cube_color:
                num_cubes = int(cube_color.replace("red", ""))
                if num_cubes > current_max["red"]:
                    current_max["red"] = num_cubes
            if "blue" in cube_color:
                num_cubes = int(cube_color.replace("blue", ""))
                if num_cubes > current_max["blue"]:
                    current_max["blue"] = num_cubes
            if "green" in cube_color:
                num_cubes = int(cube_color.replace("green", ""))
                if num_cubes > current_max["green"]:
                    current_max["green"] = num_cubes
    return current_max["red"] * current_max["blue"] * current_max["green"]

with open("./input.txt", "r") as file:
    count = 0
    while True:
        line = file.readline()
        
        # If there are no more lines, stop
        if not line:
            break

        count += game_line_value(line)

    print(f"The sum of powers is {count}")
