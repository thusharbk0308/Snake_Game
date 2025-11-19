from turtle import Turtle,Screen

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:

    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head=self.all_segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segment.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segment[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.all_segment) - 1, 0, -1):
            new_x = self.all_segment[seg_num - 1].xcor()
            new_y = self.all_segment[seg_num - 1].ycor()
            self.all_segment[seg_num].goto(new_x, new_y)
        self.all_segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def reset(self):
        for seg in self.all_segment:
            seg.goto(1000,1000)
        self.all_segment.clear()
        self.create_snake()
        self.head=self.all_segment[0]