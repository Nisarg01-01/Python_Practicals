class Point(object):
     pass
class Rectangle(object):
     pass
rectangle = Rectangle()
bottom_left = Point() 
bottom_left.x = 8.0 
bottom_left.y = 3.0
top_right = Point() 
top_right.x = 9.0 
top_right.y = 6.0
rectangle.corner1 = bottom_left 
rectangle.corner2 = top_right
dx = 15.0 
dy = 16.0

def move_rectangle(rectangle, dx, dy):
    print ("The rectangle started with bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and top right corner at (%g,%g)."
           % (rectangle.corner2.x, rectangle.corner2.y)),
    print ("dx is %g and dy is %g" % (dx, dy))
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print ("It ended with a bottom left corner at (%g,%g)"
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and a top right corner at (%g,%g)"
           % (rectangle.corner2.x, rectangle.corner2.y))

move_rectangle(rectangle, dx, dy)
