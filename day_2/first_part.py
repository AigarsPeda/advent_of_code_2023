from collections import defaultdict
from typing import List, IO

file = open("day_2/data.txt", "r")




def create_data(file: IO[str]) -> List[str]:
  data = []
  for line in file:
    # remove new line character
    line = line.replace("\n", "")
    data.append(line)
  return data

data = create_data(file)

def possible_game_id_sum (data: List[str]):
  p1 = 0
  p2 = 0
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
  return { p1,  p2}
# 2685 83707
print(possible_game_id_sum(data))


file.close()