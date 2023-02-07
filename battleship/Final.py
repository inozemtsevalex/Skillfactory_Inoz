
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

#    def __repr__(self):
 #       return f"({self.x}, {self.y})"

class Ship:
    def __init__(self, start, length, orient):
        self.start = start
        self.length = length
        self.orient = orient
    def coord(self):
        ship_coord = []
        for i in range(self.length):
            coord_x = self.start.x
            coord_y = self.start.y

            if self.orient == 'v':
                coord_x += i

            elif self.orient == 'h':
                coord_y += i

            ship_coord.append(Dot(coord_x, coord_y))

        return ship_coord

class Board:
    def __init__(self, size=6):
        self.size = size
        self.field = [["o"] * self.size for i in range(0, self.size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        game_field = "  |"
        for i in range(self.size):
            game_field += f" {i + 1} |"
        for i, value in enumerate(self.field):
            game_field += f"\n{i + 1} | " + " | ".join(value) + " |"
        return game_field