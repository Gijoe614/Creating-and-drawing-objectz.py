from swampy.World import World

world = World()

class Point(object):
    """Represents a point in 2-D space."""
blank = Point()

blank.x = 3.0
blank.y = 4.0

class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """
bbox = Rectangle()


def draw_rectangle(canvas,rectangle):
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(rectangle.bbox, fill=rectangle.color)

def draw_point(canvas, point):
    bbox =[[point.x, point.y], [point.x, point.y,]]
    drawn_canvas = world.ca(canvas.width, canvas.height)
    drawn_canvas.rectangle(bbox, width=2, fill="black")


canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')

canvas2 = canvas
canvas2.circle([-25,0], 70, outline=None, fill='red')

canvas3 = canvas
canvas3.circle([-45,0], 50, outline='black', fill='skyblue')

canvas4 = canvas
canvas4.circle([-55,0], 42, outline='orange', fill='black')

canvas5 = canvas
canvas5.circle([-85,0], 30, outline='pink', fill='white')


world.mainloop()
