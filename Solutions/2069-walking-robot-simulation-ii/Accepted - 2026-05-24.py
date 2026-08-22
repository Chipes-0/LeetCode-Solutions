class Robot:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos_x = 0
        self.pos_y = 0
        self.dirs = ["East", "Nort", "West", "South"]
        self.mov = [1, 1, -1, -1]
        self.index = 0
        self.corners = [(0, 0), (width - 1, 0), (width - 1, height - 1), (0, height - 1)]
        
    def step(self, num: int) -> None:
        while num:
            if self.index & 1:
                self.pos_y += self.mov[self.index]
            else:
                self.pos_x += self.mov[self.index]
            if (self.pos_x, self.pos_y) in self.corners:
                self.index = (self.index + 1) % 4
            num -= 1

    def getPos(self) -> List[int]:
        return [self.pos_x, self.pos_y]

    def getDir(self) -> str:
        return self.dirs[self.index]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()