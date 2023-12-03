def check_for_adjacent_symbols(row: str, part_start: int, part_end: int) -> bool:
    # Ensure first or last row are handled correctly
    if row == "":
        return False

    start_index = part_start
    if part_start != 0:
        start_index -= 1
    
    end_index = part_end
    if part_end != len(row) - 1:
        end_index += 1

    for char in row[start_index:end_index+1]:
        if not char.isdigit() and not char == '.':
            return True
        
    return False


def get_part_numbers(top_row: str, current_row: str, under_row: str) -> int:
    total_count_in_row = 0

    part_start = -1
    part_end = -1 

    for i, char in enumerate(current_row):
        if char.isdigit() and part_start == -1:
            part_start = i
        elif (not char.isdigit() or i == len(current_row) -1) and part_start != -1:
            # Does it end on the right side wall?
            if i == len(current_row)-1 and char != '.':
                part_end = i
            else:
                part_end = i - 1

            if check_for_adjacent_symbols(top_row, part_start, part_end) or \
                    check_for_adjacent_symbols(current_row, part_start, part_end) or \
                    check_for_adjacent_symbols(under_row, part_start, part_end):
                
                total_count_in_row += int(current_row[part_start: part_end + 1])
            
            part_start = -1
            part_end = -1

    return total_count_in_row

with open("./input.txt", "r") as file:
    count = 0

    top_row = ""
    current_row = file.readline().strip()
    under_row = file.readline().strip()

    while True:
        if current_row == "":
            break

        count += get_part_numbers(top_row, current_row, under_row)

        next_line = file.readline()
        if not next_line:
            next_line = ""

        top_row = current_row
        current_row = under_row
        under_row = next_line.strip()

    print(f"The sum of part numbers is {count}")
