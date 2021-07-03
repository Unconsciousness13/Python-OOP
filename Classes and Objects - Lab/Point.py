class Point:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_x(self,new_x: int):
        self.x = new_x
        return new_x

    def set_y(self,new_y: int):
        self.y = new_y
        return new_y

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"
    
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
