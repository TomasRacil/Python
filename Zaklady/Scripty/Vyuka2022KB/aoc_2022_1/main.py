from os.path import realpath, dirname, join

with open(join(dirname(realpath(__file__)),"input.txt"),
          "r", encoding="utf_8") as file:
    data=sorted([sum([int(cal) for cal in elf.split('\n')]) 
         for elf in file.read().split('\n\n')])
        
    
print(data[-1])
print(sum(data[-3:]))
    # maximal, curent=0,0
    # for radek in file.read().split('\n'):
    #     if radek =='':
    #         if curent>maximal: 
    #             maximal = curent
    #         curent = 0
    #     else:
    #         curent+=int(radek)
    # print(maximal)
    
    
    
    
    

