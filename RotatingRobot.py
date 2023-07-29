import turtle

def rotate_robot(degrees):
    robot.right(degrees)

# Set up the turtle
robot = turtle.Turtle()
robot.shape("turtle")

# Rotate the robot in different degrees
rotation_angles = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]

for angle in rotation_angles:
    rotate_robot(angle)
    turtle.done() # Uncomment this line if you want to see each rotation before continuing to the next.

turtle.done()