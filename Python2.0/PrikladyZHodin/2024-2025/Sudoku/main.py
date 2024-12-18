from os.path import join, dirname, realpath


class Sudoku:
    def __init__(self, sudoku):
        radky = sudoku.split("\n")
        self.name = radky[0]
        self.sudoku = [[int(cislo) for cislo in radek] for radek in radky[1:]]

    def __str__(self):
        repr = f"{self.name}:"
        repr += "\n"
        repr += "\n".join(
            [
                " ".join(
                    [
                        str(cislo) if cislo != 0 else " "
                        for idx, cislo in enumerate(radek)
                    ]
                )
                for radek in self.sudoku
            ]
        )
        repr += "\n"
        return repr

    def find_usolved_positions(self):
        unsolved_positions = []
        for y in range(9):
            for x in range(9):
                if self.sudoku[y][x] == 0:
                    unsolved_positions.append((y, x))
        return unsolved_positions

    def find_posible_numbers(self, x, y):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            if self.sudoku[x][i] in numbers:
                numbers.remove(self.sudoku[x][i])
            if self.sudoku[i][y] in numbers:
                numbers.remove(self.sudoku[i][y])
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if self.sudoku[i][j] in numbers:
                    numbers.remove(self.sudoku[i][j])
        return numbers

    def solve(self):
        unsolved_positions = self.find_usolved_positions()

        if len(unsolved_positions) == 0:
            return True
        posible_solutions = sorted(
            [
                (position, self.find_posible_numbers(position[0], position[1]))
                for position in unsolved_positions
            ],
            key=lambda x: len(x[1]),
        )
        if len(posible_solutions[0][1]) == 0:
            return False
        for number in posible_solutions[0][1]:
            self.sudoku[posible_solutions[0][0][0]][posible_solutions[0][0][1]] = number
            if self.solve():
                return True
            else:
                self.sudoku[posible_solutions[0][0][0]][posible_solutions[0][0][1]] = 0
        return False


if __name__ == "__main__":
    with open(join(dirname(realpath(__file__)), "sudoku.txt")) as soubor:
        sudoku = [
            Sudoku(sudoku.strip())
            for sudoku in soubor.read().split("Grid ")
            if sudoku.strip() != ""
        ]
        for s in sudoku[:2]:
            print(s)
            s.solve()
            print(s)
