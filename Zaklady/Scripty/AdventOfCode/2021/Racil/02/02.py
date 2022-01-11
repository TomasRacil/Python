from os import path


class Submarine:
    z = 0
    x = 0
    aim = 0

    def move1(self, value, command):
        """
        change position of object
        param: value
        param: command
        """
        if command == "forward":
            self.x += value
        elif command == "up":
            self.z += value
        else:
            self.z -= value

    def move2(self, value):
        """
        change position of object (depends on aim)
        param: value
        """
        self.x += value
        self.z += value*self.aim

    def changeAim(self, value, direction):
        """
        change aim of object
        param: value
        param: direction
        """
        if direction == "down":
            self.aim += value
        else:
            self.aim -= value

    def navigate1(self, navigation):
        """
        based on navigation data call move method object parameters
        (without aim)
        param: list of [value(int),order(str)]
        """
        for order in navigation:
            self.move1(order[1], order[0])

    def navigate2(self, navigation):
        """
        based on navigation data change object parameters (with aim)
        param: list of [value(int),order(str)]
        """
        for order in navigation:
            if order[0] == "forward":
                self.move2(order[1])
            else:
                self.changeAim(order[1], order[0])

    def reset(self):
        """
        reset object parameters
        """
        self.x, self.y, self.z = 0, 0, 0

    def info(self):
        '''
        print info about object
        '''
        print(
            f"x: {self.x}\nz: {self.z}\naim: {self.aim}\nx*z={abs(self.x*self.z)}"
            )


with open(path.join(path.dirname(path.realpath(__file__)),
                    "input.txt"), "r") as f:
    commands = [[line.strip().split()[0], int(line.strip().split()[1])]
                for line in f]

sub = Submarine()
sub.navigate1(commands)
sub.info()
sub.reset()
sub.navigate2(commands)
sub.info()
