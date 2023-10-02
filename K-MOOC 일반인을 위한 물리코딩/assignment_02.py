from vpython import *

# 화면 설정
scene = canvas(width=800, height=800, background=color.black)

# 지구와 태양 생성
earth = sphere(pos=vector(0, 1.5e11, 0), radius=6.4e9, texture=textures.earth, make_trail=True, retain=365)
sun = sphere(pos=vector(0, 0, 0), radius=3.5e10, color=color.yellow)

# 초기속도 설정
earth.velocity = vector(-29783, 0, 0)
sun.velocity = vector(0, 0, 0)

# 물체의 질량 설정
earth.mass = 5.97e24
sun.mass = 1.99e30

# 중력 상수 설정
G = 6.67e-11

# 시뮬레이션 설정
dt = 24 * 3600  # 24시간 간격
t = 0

while t < 365 * 24 * 3600:  # 1년 동안 시뮬레이션
    rate(1000)  # 화면 업데이트 속도 제한

    # 중력 상호 작용 계산
    r = earth.pos - sun.pos
    if mag(r) != 0:  # 거리가 0이 아닌 경우에만 계산
        F = (-G * earth.mass * sun.mass / mag(r) ** 3) * r
        earth.velocity += F / earth.mass * dt
        sun.velocity += -F / sun.mass * dt

        # 새 위치 계산
        earth.pos += earth.velocity * dt
        sun.pos += sun.velocity * dt

    t += dt
