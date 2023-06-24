import turtle

def draw_fractal_tree(branch_length, angle, scale_factor, num_branches, depth):
    if depth == 0:  # Base case: stop recursion when depth reaches zero
        return
    else:
        turtle.forward(branch_length)  # Draw the trunk

        for _ in range(num_branches):
            turtle.left(angle)  # Turn left to draw the left subtree
            draw_fractal_tree(branch_length * scale_factor, angle, scale_factor, num_branches, depth - 1)

        turtle.right(angle * num_branches * 2)  # Turn right to draw the right subtree
        draw_fractal_tree(branch_length * scale_factor, angle, scale_factor, num_branches, depth - 1)

        turtle.left(angle * num_branches)  # Turn back to the original direction
        turtle.backward(branch_length)  # Go back to the trunk's starting point

# Setup turtle
turtle.setup(width=800, height=600)
turtle.speed(0)  # Set the turtle's speed (0 is the fastest)
turtle.bgcolor("black")  # Set the background color
turtle.pencolor("white")  # Set the pen color

# Position turtle at the bottom of the screen
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Start drawing the fractal tree
draw_fractal_tree(100, 30, 0.5, 3, 6)  # Adjust the parameters to create different types of fractals

# Hide turtle
turtle.hideturtle()

# Keep the window open until it's manually closed
turtle.done()
