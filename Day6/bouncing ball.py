import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
GRAVITY = 9.8  # m/s^2
INITIAL_HEIGHT = 10  # meters
ELASTICITY = 0.8  # Coefficient of restitution

# Function to update the position of the ball
def update(frame):
    # Update velocity based on gravity
    ball.velocity -= GRAVITY * frame_interval
    # Update position
    ball.position += ball.velocity * frame_interval
    # Check for collision with ground
    if ball.position <= 0:
        ball.velocity *= -ELASTICITY  # Reverse direction with some energy loss
        ball.position = 0

    # Update ball position
    ball_line.set_ydata(ball.position)
    return ball_line,

# Class to represent the ball
class Ball:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

# Parameters for animation
num_frames = 300
frame_interval = 0.05  # seconds

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, INITIAL_HEIGHT + 1)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create the ball object
ball = Ball(INITIAL_HEIGHT, 0)

# Create a line to represent the ball
ball_line, = ax.plot([0.5], [ball.position], 'o', color='b')

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=frame_interval * 1000, blit=True)

plt.show()
