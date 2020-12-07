def solve2(data):
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            if (data[i]+data[j] == 2020):
                print("Solve for 2 entries:")
                print("Entry1 = ", data[i])
                print("Entry2 = ", data[j])
                print("Product = ", data[i]*data[j])
                return

def solve3(data):
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

with open('1_input.txt', 'r') as txtfile:
    numbers_list = txtfile.readlines()
    data = [int(num) for curr_line in numbers_list for num in curr_line.split()]
 
solve2(data)
solve3(data)