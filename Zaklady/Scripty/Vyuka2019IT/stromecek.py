def print_tree_1(height: int):
    for number in range(height):
        # temp=''
        # for _ in range(number+1):
        #     temp+='*'
        # print(temp)
        print('*'*(number+1))
        
def print_tree_2(height: int):
    for number in range(height):
        print(' '*(height-number-1)+'*'*(number*2+1))

def print_tree_3(height: int, stump_radius:int = 1, stump_length: int = 2):
    print_tree_2(height)
    for number in range(stump_length):
        print(' '* (height-stump_radius-1) + '#'*(stump_radius*2+1))
 
print_tree_3(5)