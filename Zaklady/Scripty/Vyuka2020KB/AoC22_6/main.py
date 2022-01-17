from os import path


def lanternFishRepr(fishes):
    fishes2 = fishes[1:]
    fishes2.append(fishes[0])
    fishes2[6] += fishes[0]
    return fishes2


with open(
    path.join(path.dirname(path.realpath(__file__)),
              "input.txt"), "r") as f:
    fishes = [0 for _ in range(9)]
    for fish in f.readline().split(","):
        fishes[int(fish)] += 1
days = 0
input(fishes)
while(days < 256):
    fishes = lanternFishRepr(fishes)
    input(fishes)
    days += 1
print(fishes)
print(sum(fishes))
