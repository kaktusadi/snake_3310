from turtle import Turtle

 #const var
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
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
        """creating a new "Turtle_segment x3 as whole snake"""
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, i_position):
        """the part of method above: snake creation"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(i_position)
        self.segments.append(new_segment)

    def extend(self):
        """add a new segment to the snake
        position() of class Turtle
        hold the right position of the last segment
        add a segment to the position of the last
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """moving snake forward continuously"""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y) #last segment goes to the defined position
        self.segments[0].forward(MOVE_DISTANCE) #wazne to poza petla bo psuje animacje
        # for seg in segments:
        #     seg.forward(20)

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


