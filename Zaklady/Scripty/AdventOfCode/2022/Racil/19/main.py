"""
Solution to 18. day of advent of code 2022
https://adventofcode.com/2022/day/18
"""

from os.path import realpath, dirname, join
from re import findall

class Blueprint:
    def __init__(self,data: str) -> None:
        part_1, part_2 = tuple(data.split(':'))
        self.id:int = int(part_1.split()[1])
        self.ore_robot_cost: dict = self.parse_robot_cost(part_2.split('.')[0])
        self.clay_robot_cost: dict = self.parse_robot_cost(part_2.split('.')[1])
        self.obsidian_robot_cost:dict  = self.parse_robot_cost(part_2.split('.')[2])
        self.geode_robot_cost:dict = self.parse_robot_cost(part_2.split('.')[3])
    
    def __repr__(self) -> str:
        output = f"""ID: {self.id}
            Each ore robot costs {self.ore_robot_cost['ore']} ore and {self.ore_robot_cost['clay']} clay and {self.ore_robot_cost['obsidian']} obsidian
            Each clay robot costs {self.clay_robot_cost['ore']} ore and {self.clay_robot_cost['clay']} clay and {self.clay_robot_cost['obsidian']} obsidian
            Each obsidian robot costs {self.obsidian_robot_cost['ore']} ore and {self.obsidian_robot_cost['clay']} clay and {self.obsidian_robot_cost['obsidian']} obsidian
            Each geode robot costs {self.geode_robot_cost['ore']} ore and {self.geode_robot_cost['clay']} clay and {self.geode_robot_cost['obsidian']} obsidian
        """
        return output
        
    def parse_robot_cost(self, line:str):
        ore:list = findall(r'(\d+)\sore', line)
        clay:list = findall(r'(\d+)\sclay', line)
        obsidian:list = findall(r'(\d+)\sobsidian', line)
        output: dict = {'ore':0 if ore==[] else ore.pop(),
                  'clay': 0 if ore==[] else clay.pop(),
                  'obsidian': 0 if obsidian==[] else obsidian.pop()}
        return output

class Scenario:
    def __init__(self, blueprint) -> None:
        self.blueprint:Blueprint = blueprint
        self.ore:int = 0
        self.ore_robots:int = 1
        self.clay: int = 0
        self.clay_robots: int = 0
        self.obsidian: int = 0
        self.obsidian_robots:int = 0
        self.geodes:int = 0
        self.geode_robots:int = 0
    
    def __repr__(self) -> int:
        return self.blueprint.id*self.geodes

def main(version: str):
    """_summary_

    Args:
        version (str): _description_
    """
    with open(
        join(dirname(realpath(__file__)), version + ".txt"), "r", encoding="utf_8"
    ) as file:
        blueprints = [Blueprint(blueprint) for blueprint in file.read().split('\n')]
    for blueprint in blueprints:
        print(blueprint)
    
    

if __name__ == "__main__":
    main("test")
