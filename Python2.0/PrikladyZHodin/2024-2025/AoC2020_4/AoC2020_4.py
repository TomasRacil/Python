from os import path
from re import split, match

def test_hgt(hgt:str)->bool:
    m = match('^(\d{2,3})(cm|in)$', hgt)
    if not m:
        return False
    if m[2] == 'cm':
        return 150<= int(m[1])<=193
    else:
        return 59<= int(m[1])<=76



potrebne_pole = ('byr','iyr','eyr','hgt','hcl','ecl','pid') #,'cid')

with open(path.join(path.dirname(path.realpath(__file__)), "vstup.txt")) as soubor:
    pasy = [
        {pole.split(":")[0]: pole.split(":")[1] for pole in split("\s", pas)}
        for pas in soubor.read().split("\n\n")
    ]
    platne_pasy = [pas for pas in pasy if all(pole in pas for pole in potrebne_pole)]
    # print(platne_pasy)
    print(len(platne_pasy))
    
    # platne_pasy_2 = [pas for pas in pasy if 
    #                  1920<=int(pas.get('byr','0'))<=2002 and
    #                  2010<=int(pas.get('iyr','0'))<=2020 and
    #                  2020<=int(pas.get('eyr','0'))<=2030 and
    #                  test_hgt(pas.get('hgt','')) and
    #                 match('^#[0-9a-f]{6}$',pas.get('hcl','')) and
    #                 pas.get('ecl','') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
    #                 match('^\d{9}$', pas.get('pid', ''))
    #                  ]
    
    platne_pasy_2 = [pas for pas in platne_pasy if 
                     1920<=int(pas['byr'])<=2002 and 
                     2010<=int(pas['iyr'])<=2020 and 
                     2020<=int(pas['eyr'])<=2030 and 
                     (
                        (59 <= int(m.group(1)) <= 76 if m.group(2) == "in" else 150 <= int(m.group(1)) <= 193) if 
                        (m := match(r"^(\d{2,3})(cm|in)$", pas['hgt'])) 
                        else False
                      ) and
                     match("^#[0-9a-f]{6}$",pas['hcl']) and
                     pas['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
                     match("^\d{9}$",pas['pid'])]

    print(len(platne_pasy_2))   


