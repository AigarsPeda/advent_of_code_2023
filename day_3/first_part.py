from typing import List, IO

file = open("day_3/data.txt", "r")

def create_data(file: IO[str]) -> List[str]:
  data = []
  for line in file:
    # remove new line character
    line = line.replace("\n", "")
    data.append(line)
  return data

data = create_data(file)



# ['467..114..']
# ['...*......']
# ['..35..633.']
# ['......#...']
# ['617*......']
# ['.....+.58.']
# ['..592.....']
# ['......755.']
# ['...$.*....']
# ['.664.598..']





def find_all_symbols_except_dot_and_numbers(data: List[str]) -> List[str]:
  symbols = []
  for line in data:
    for char in line:
      if char not in symbols and char != "." and not char.isdigit():
        symbols.append(char)
  return symbols

symbols = find_all_symbols_except_dot_and_numbers(data)
print(symbols)




def find_full_numbers_around_symbols(grid, symbols):
    # Function to check if a character is a number
    def is_number(char):
        return char.isdigit()

    # Function to get full number starting from a specific position
    def get_full_number(grid, i, j):
        number = ""
        # Check left
        left = j - 1
        while left >= 0 and is_number(grid[i][left]):
            number = grid[i][left] + number
            left -= 1

        # Add the current number
        number += grid[i][j]

        # Check right
        right = j + 1
        while right < len(grid[i]) and is_number(grid[i][right]):
            number += grid[i][right]
            right += 1

        return number

    # Results list
    results = []
    res_numbers_around: List[int] = []

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current_char = grid[i][j]

            # Check if the current character is one of the symbols
            if current_char in symbols:
                # Set to store full numbers found around the symbol
                numbers_around = set()

                # Check all eight directions around the symbol
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        # Skip the center position where the symbol is
                        if di == 0 and dj == 0:
                            continue

                        # Calculate new position
                        ni, nj = i + di, j + dj

                        # Check if the new position is within the bounds of the grid
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                            # Check if the character at the new position is a number
                            if is_number(grid[ni][nj]):
                                full_number = get_full_number(grid, ni, nj)
                                numbers_around.add(full_number)

                # Add the symbol position and the numbers found around it to the results
                results.append(((i, j), numbers_around))
                
                # loop through numbers_around
                for number in numbers_around:
                  # add number to res_numbers_around
                  res_numbers_around.append(number)

              
                


    return {"results": results, "numbers_around": res_numbers_around}



res = find_full_numbers_around_symbols(data, symbols)



def find_sum(array: List[str]):
  num_sum = 0
  for i in range(len(array)):
    string = array[i]
    
    # combine all string in array to one string
    string = "".join(string)
    num = int(string)
    num_sum += num
    
  return num_sum 
    
part_one =  find_sum(res["numbers_around"])
print("part_one", part_one)


file.close()