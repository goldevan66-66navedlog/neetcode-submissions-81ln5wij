class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        distances = set()
        for x,y in self.points.keys():
            if(x == point[0] and y != point[1]):
                distances.add(abs(y-point[1]))
            if(y == point[1] and x != point[0]):
                distances.add(abs(x-point[0]))
        
        squares = 0
        for d in distances:
            squares += self.points[tuple([point[0]+d,point[1]])]* self.points[tuple([point[0],point[1]+d])] * self.points[tuple([point[0]+d,point[1]+d])]
            squares += self.points[tuple([point[0]+d,point[1]])]* self.points[tuple([point[0],point[1]-d])] * self.points[tuple([point[0]+d,point[1]-d])]
            squares += self.points[tuple([point[0]-d,point[1]])]* self.points[tuple([point[0],point[1]+d])] * self.points[tuple([point[0]-d,point[1]+d])]
            squares += self.points[tuple([point[0]-d,point[1]])]* self.points[tuple([point[0],point[1]-d])] * self.points[tuple([point[0]-d,point[1]-d])]
        return squares

        
        
