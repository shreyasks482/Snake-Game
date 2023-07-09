from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_segment(pos)

    def add_segment(self, pos):
        pet = Turtle("square")
        pet.color("white")
        pet.shapesize(stretch_len=.75, stretch_wid=.75)
        pet.penup()
        pet.goto(pos)
        self.segments.append(pet)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[segnum - 1].xcor()
            ny = self.segments[segnum - 1].ycor()
            # self.head=self.segments[0]
            self.segments[segnum].goto(nx, ny)
        # self.segments[0].forward(MOVE)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
