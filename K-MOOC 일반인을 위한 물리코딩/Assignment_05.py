Web VPython 3.2

ground = box(size=vec(40, 40, 1), color=color.green)
ball = sphere(pos=vec(-18, 0, 0), radius=0.5)
ground.pos.z = ground.pos.z - ground.width / 2 - ball.radius
hole = cylinder(pos=vec(15, 0, ground.pos.z + ground.width / 2), axis=vec(0, 0, 1), radius=3 * ball.radius,
                color=vec(0.8, 0.8, 0.8))
hole.pos.z = hole.pos.z - mag(hole.axis) * 0.9

# Properties
ball.m = 0.045
g = 9.8
mu = 0.5

initialspeed = 18

scale = initialspeed
ball.v = initialspeed * vec(1, 0, 0)

# Time
t = 0
dt = 0.01

while t < 100:
    rate(100)

    # 마찰력 계산
    friction_force = -mu * ball.m * g * norm(ball.v)
    
    # 마찰력을 이용한 가속도 계산
    friction_acceleration = friction_force / ball.m
    
    # 현재 속도에 마찰력 가속도를 적용
    ball.v += friction_acceleration * dt

    # 운동방정식을 사용하여 위치 업데이트
    ball.pos += ball.v * dt

    # 시간 업데이트
    t += dt

