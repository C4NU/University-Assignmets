#GlowScript 2.9 VPython

from vpython import *

# Ground
ground = box(pos=vec(0,0,0), size=vec(100,0.10,70), color=color.green)

# Goal post
goal_post = box(pos=vec(15, 1.5, 0), size=vec(0.5, 3, 8), color=color.white)

# Initialize position & velocity of the ball
init_pos = vec(-30, 0.11, 0)
ball = sphere(pos=init_pos, radius=0.11, color=color.orange, make_trail=False)
ball.m = 0.45  # kg
ball.speed = 25  # m/s
ball.angle = radians(35)  # degrees
ball.v = ball.speed * vec(cos(ball.angle), sin(ball.angle), 0)
attach_arrow(ball, "v", shaftwidth=0.1, scale=0.3, color=color.yellow)

scene.range = 30
scene.camera.pos = vec(0, 50, -25)
scene.camera.axis = vec(0, -45, 45)
# Constants
g = -9.8  # m/s^2
rho = 1.204  # kg/m^3
Cd = 0.3
Cm = 1
w = 10 * 2 * pi

# UI
scene.append_to_caption(' \nInitial Values \n \n')

# Slider for velocity
velocitySlider = slider(min=0, max=45, value=25, bind=setVelocity)
scene.append_to_caption(' \nVelocity:', velocitySlider.min, 'to', velocitySlider.max, '\n \n')

def setVelocity():
    global ball
    ball.speed = velocitySlider.value
    ball.v = ball.speed * vec(cos(ball.angle), sin(ball.angle), 0)

# Slider for angle
angleSlider = slider(min=0, max=90, value=35, bind=setAngle)
scene.append_to_caption(' \nAngle:', angleSlider.min, 'to', angleSlider.max, ' \n \n')

def setAngle():
    global ball
    ball.angle = radians(angleSlider.value)
    ball.v = ball.speed * vec(cos(ball.angle), sin(ball.angle), 0)

# Slider for angular velocity
angularSlider = slider(min=-10, max=10, value=10, bind=setAngular)
scene.append_to_caption(' \nAngular velocity:', angularSlider.min, 'to', angularSlider.max, ' \n \n')

def setAngular():
    global w
    w = angularSlider.value * 2 * pi

# Button to shoot
btnStart = button(text='Shoot', bind=startbtn)

def startbtn(b):
    b.disabled = True
    return b.disabled

# Time settings
t = 0
dt = 0.01

while t < 20:
    rate(1/dt)

    if btnStart.disabled == True:
        ball.make_trail = True

        # Gravity Force
        grav = ball.m * vec(0, g, 0)

        # Drag Force
        drag = -0.5 * rho * Cd * (pi * ball.radius**2) * mag(ball.v)**2 * norm(ball.v)

        # Magnus Force
        magnus = 0.5 * rho * Cm * (pi * ball.radius**2) * ball.radius * w * mag(ball.v) * cross(vec(0, 1, 0), norm(ball.v))

        # Sum of Forces
        ball.f = grav + drag + magnus

        # Time stepping
        ball.v = ball.v + ball.f / ball.m * dt
        ball.pos = ball.pos + ball.v * dt

    # Collision with the goal post
    if goal_post.pos.x - goal_post.size.x / 2 < ball.pos.x < goal_post.pos.x + goal_post.size.x / 2 and \
       goal_post.pos.y - goal_post.size.y / 2 < ball.pos.y < goal_post.pos.y + goal_post.size.y / 2 and \
       goal_post.pos.z - goal_post.size.z / 2 < ball.pos.z < goal_post.pos.z + goal_post.size.z / 2:
        break

    # Collision with the ground
    if ball.pos.y - ball.radius < 0:
        scene.waitfor('click')

        # Reset
        btnStart.disabled = False
        ball.pos = init_pos
        ball.v = ball.speed * vec(cos(ball.angle), sin(ball.angle), 0)
        ball.make_trail = False
        t = 0

    t = t + dt

print("Goal!")
