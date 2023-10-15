from scipy import misc

def f1(x):
  return 4 * (x**3) - (10 * x) - 3

x = np.arange(-2.0, 2.0, 0.01)

y = f1(x)
plt.plot(x, y, 'y-')
plt.xlim(-7, 7)
plt.ylim(-11, 11)

learning_rate = 0.005
iterations = 100
start = 2.0 # start value
y0 = f1(start)
y1 = y0
plt.scatter(start, f1(start), color = 'r', marker = '^', s=150)

i = 200

while i > 0.0001 and iterations > 0:
    start = start - learning_rate * misc.derivative(f1, start)
    y0 = f1(start)
    iterations = iterations - 1
    i = abs(y1 - y0)
    y1 = y0
    plt.scatter(start, y0, marker="^", s=50)
print('A minimum point found as: ', start, y0)
plt.grid()
plt.show()