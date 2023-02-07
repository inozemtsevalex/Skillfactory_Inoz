class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
       return f"({self.x}, {self.y})"

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

            if self.orient == 'h':
                coord_x += i

            elif self.orient == 'v':
                coord_y += i

            ship_coord.append(Dot(coord_x, coord_y))

        return ship_coord

ship = Ship(Dot(2,2), 2, 'h')
coordship =[]
coordship = ship.coord()
print(coordship)
