def main():
    depths = readFile()

    print(f"Part One : {part_one(depths)}")    
    print(f"Part Two : {part_two(depths, 3)}")


def part_one(depths):
    prev_depth = depths[0]
    count_inc = 0

    for depth in depths[1:]:
        if depth > prev_depth:
            count_inc += 1

        prev_depth = depth
    
    return count_inc
    

def part_two(depths, window_size):
    prev_depth_sum = sum(depths[0 : window_size])
    count_inc = 0

    for depth in range(1, len(depths) - (window_size - 1)):
        _depths_sum = sum(depths[depth : depth + window_size])

        if _depths_sum > prev_depth_sum:
            count_inc += 1
        
        prev_depth_sum = _depths_sum


    return count_inc


def readFile():
    f = open('c:/Users/arkto/Documents/UNOB/3SEMESTR/aoc/input.txt' , "r")
    data = f.read().splitlines()
    data = [ int(x) for x in data ]
    return data 
    

if __name__ == "__main__":
    main()