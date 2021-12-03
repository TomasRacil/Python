from os import path

absolute_path = path.dirname(path.abspath(__file__))

def solve1(data):
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if (data[i]+data[j] == 2020):
                print("Solve for 2 entries:")
                print("Entry1 = ", data[i])
                print("Entry2 = ", data[j])
                print("Product = ", data[i]*data[j])
                return

def solve2(data):
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            for k in range(0, len(data)):
                if (data[i]+data[j]+data[k] == 2020):
                    print("\nSolve for 3 entries:")
                    print("Entry1 = ", data[i])
                    print("Entry2 = ", data[j])
                    print("Entry3 = ", data[k])
                    print("Product = ", data[i]*data[j]*data[k])
                    return

with open(absolute_path + "/1_input.txt", 'r') as txtfile:
    numbers_list = txtfile.readlines()
    data = [int(num) for curr_line in numbers_list for num in curr_line.split()]
 
solve1(data)
solve2(data)