class Board:
    def __init__(self, size):
        self.size = size
        self.field = [["o"] * self.size for i in range(0, self.size)]
        self.busy = []


    def __str__(self):
        game_field = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, value in enumerate(self.field):
            game_field += f"\n{i + 1} | " + " | ".join(value) + " |"
        return game_field

b = Board(6)
print(b)
