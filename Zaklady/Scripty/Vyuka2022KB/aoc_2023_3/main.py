from os.path import realpath, dirname, join
from re import finditer

def main():
    with open(join(dirname(realpath(__file__)),"test.txt"),
            "r", encoding="utf_8") as file:
        input = file.read().split('\n')
        numbers = [(y,it.start(),it.end(),int(it.group())) for y,line in enumerate(input) for it in finditer(r"\d+",line)]
        parts = [(y,it.start(),it.end(),it.group()) for y,line in enumerate(input) for it in finditer(r"[^\.\d]+",line)]
    # print(numbers)
    adj = []
    # for y_1,xs_1,xe_1,number in numbers:
    #     for y_2,xs_2,_,_ in parts:
    #         if abs(y_1-y_2)<=1 and (xs_2>=xs_1-1 and xs_2<=xe_1):adj.append(number)
    print(sum([number for y_1,xs_1,xe_1,number in numbers for y_2,xs_2,xe_2,part in parts if abs(y_1-y_2)<=1 and (xs_2>=xs_1-1 and xs_2<=xe_1)])) 
    
    # data = [(y,it.start(),it.end(),it.group()) for y,line in enumerate(input)  for it in finditer(r"[^\.]+",line)]
    # print(data)
    
    print(1 if False else 2)
    
    
if __name__=="__main__":
    main()

    
# data = [(y,it.start(),it.end(),it.group()) for y,line in enumerate(input) for it in finditer(r"[^\.]+",line)]
