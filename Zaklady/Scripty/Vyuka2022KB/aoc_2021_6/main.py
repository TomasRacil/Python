from os.path import realpath, dirname, join
from collections import deque

# def play(fish:list[int], turn_count:int)->int:
#     for t in range(turn_count):
#         for i,f in enumerate(fish):
#             fish[i]-=1
#             if fish[i]<0:
#                 fish[i]=6
#                 fish.append(9)
#         print(fish)
#     return len(fish)

def play(fish:list[int], turn_count:int)->int:
    # fish = deque(fish)
    for t in range(turn_count):
        # fish.rotate(-1)
        fish = fish[1:]+[fish[0]]
        fish[6]+=fish[-1]
        # print(fish)
    return sum(fish)

with open(join(dirname(realpath(__file__)),"input.txt"),
          "r", encoding="utf_8") as file:
    data=[0]*9
    for fish in file.read().split(','):
        data[int(fish)]+=1

print(play(data, 256))
# print(play(data, 16))






