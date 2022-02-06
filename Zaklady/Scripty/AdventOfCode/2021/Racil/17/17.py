"""
Solution to 17. day of advent of code 2021
https://adventofcode.com/2021/day/17
"""

from os.path import realpath, dirname, join


class Probe:
    """
    Represents probe.

    Args:
        x_speed (int): initial speed of the probe in x direction
        y_speed (int): initial speed of the probe in y direction

    Atributes:
        x_coord (int): coordinate x of the probe
        y_coord (int): coordinate y of the probe
        x_speed (int): speed of the probe in x direction
        y_speed (int): speed of the probe in y direction

    """

    x_coord = 0
    y_coord = 0

    def __init__(self, x_speed: int, y_speed: int):
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        """
        Simulate movement of the probe in one step.
        """
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed
        if self.x_speed > 0:
            self.x_speed -= 1
        elif self.x_speed == 0:
            self.x_speed = 0
        else:
            self.x_speed += 1
        self.y_speed -= 1

    def info(self) -> tuple[int, int]:
        """
        Information about probe.

        Returns:
            tuple[int,int]: position of the probe x and y coordinates
        """
        return (self.x_coord, self.y_coord)

    def highest_poin(self)->int:
        """
        Find the highest point the probe would reach.

        Returns:
            int: highest point
        """
        while self.y_speed >= 0:
            self.move()
        print(self.info()[1])


def main():
    """
    main
    """
    with open(
        join(dirname(realpath(__file__)), "input.txt"), "r", encoding="utf_8"
    ) as file:
        area = [[int(item) for item in line.split(",")] for line in file]
    fib, fib1 = 1, 1
    while fib < area[0][0]:
        fib, fib1 = fib + fib1 + 1, fib1 + 1

    target_x = list(range(area[0][0], area[0][1] + 1))
    target_y = list(range(area[1][0], area[1][1] + 1))
    posible_vectors = [
        (x, y)
        for x in range(fib1, area[0][1] + 1)
        for y in range(area[1][0], abs(area[1][0]))
    ]

    y_max = 0
    vectors = []
    for x_dir, y_dir in posible_vectors:
        my_probe = Probe(x_dir, y_dir)

        while True:
            my_probe.move()
            if my_probe.info()[0] in target_x and my_probe.info()[1] in target_y:
                vectors.append((x_dir, y_dir))
                if y_max < y_dir:
                    y_max = y_dir
                break
            if my_probe.info()[0] > area[0][1] or my_probe.info()[1] < area[1][0]:
                break

    print(f"highest point reached: {my_probe.highest_poin()}")
    print(f"number of distinct velocity: {len(vectors)}")


if __name__ == "__main__":
    main()
