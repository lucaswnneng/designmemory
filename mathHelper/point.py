class Point:
    def __init__(
        self,
        p: tuple[int, int] | tuple[float, float],
    ):
        self.x = p[0]
        self.y = p[1]

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))