from collections import defaultdict

file = open("day_2/data.txt", "r")




def create_data (file):
  data = []
  for line in file:
    # remove new line character
    line = line.replace("\n", "")
    data.append(line)
  return data

data = create_data(file)



# D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
#only 12 red cubes, 13 green cubes, and 14 blue cubes?
for line in data:
  ok = True
  id_, line = line.split(':')
  V = defaultdict(int)
  for event in line.split(';'):
    for balls in event.split(','):
      n,color = balls.split()
      n = int(n)
      V[color] = max(V[color], n)
      if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
        ok = False
  score = 1
  for v in V.values():
    score *= v
  p2 += score
  if ok:
    p1 += int(id_.split()[-1])
print(p1)
print(p2)

# # witch games are possible with the given cubes?

# def format_giver (given: str):
#   # {'red': 12, 'green': 13, 'blue': 14}
#   res = {}
#   format = given.split(", ")
#   for color in format:
#     color = color.split(" ")
#     res[color[1]] = int(color[0])
    
#   return res

# formatted_given = format_giver(given)
# print(formatted_given)

# def format_games (games: list[str]):
#   # res = []
#   games_with_colors = {}
#   for game in games:
#     # use regex is string find Game and get the number after it
#     game_name = re.findall(r"Game (\d+)", game)

#     game_name = "".join(game_name)
#     # # use regex to find all colors and numbers before
#     game = re.findall(r"(\d+) (\w+)", game)
    
    
#     # [('3', 'blue'), ('4', 'red'), ('1', 'red'), ('2', 'green'), ('6', 'blue'), ('2', 'green')]
#     # count all ble blue: 9, red: 5, green: 4
#     count_colors = {}
#     for color in colors:
#       count_colors[color] = 0
#     for color in game:
#       count_colors[color[1]] += int(color[0])
    
#     games_with_colors[game_name] = count_colors

#   return games_with_colors

# formatted_games = format_games(data)
# print(formatted_games)


# # get games that are possible with the given cubes where the number each color is equal or lower than the given cubes
# def get_possible_games (formatted_games: dict, formatted_given: dict):
#   res = []
#   for game in formatted_games:
#     is_possible = True
#     for color in formatted_games[game]:
#       if formatted_games[game][color] > formatted_given[color]:
#         is_possible = False
#     if is_possible:
#       res.append(game)
#   return res

# possible_games = get_possible_games(formatted_games, formatted_given)
# print(possible_games)

# # count the sum of all possible games
# def count_sum_of_ids (possible_games: list[str]):
#   res = 0
#   for game in possible_games:
#     res += int(game)
#   return res

# sum_of_ids = count_sum_of_ids(possible_games)
# print(sum_of_ids)

# def format_giver(given: str):
#     # Format the given string into a dictionary
#     res = {}
#     format = given.split(", ")
#     for color in format:
#         color = color.split(" ")
#         res[color[1]] = int(color[0])
#     return res

# formatted_given = format_giver(given)

# def format_games(games):
#     # Format the games into a dictionary
#     games_with_colors = {}
#     colors = ['red', 'green', 'blue']
#     for game in games:
#         # Extract game name and game details
#         game_name = re.findall(r"Game (\d+)", game)[0]
#         game_details = re.findall(r"(\d+) (\w+)", game)
        
#         # Count colors in each game
#         count_colors = {color: 0 for color in colors}
#         for amount, color in game_details:
#             count_colors[color] += int(amount)
        
#         games_with_colors[game_name] = count_colors

#     return games_with_colors

# formatted_games = format_games(games)

# def get_possible_games(formatted_games, formatted_given):
#     # Determine which games are possible with the given cubes
#     res = []
#     for game in formatted_games:
#         is_possible = True
#         for color in formatted_games[game]:
#             if formatted_games[game][color] > formatted_given[color]:
#                 is_possible = False
#         if is_possible:
#             res.append(game)
#     return res

# possible_games = get_possible_games(formatted_games, formatted_given)

# def count_sum_of_ids(possible_games):
#     # Sum the IDs of all possible games
#     return sum([int(game) for game in possible_games])

# sum_of_ids = count_sum_of_ids(possible_games)

# print(sum_of_ids)


file.close()