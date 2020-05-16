import math

def distance(x1, y1, x2, y2):
    dx = math.fabs(x2 - x1)
    dy = math.fabs(y2 - y1)
    return math.sqrt(math.pow(dx, 2.5) + math.pow(dy, 2.5))
    # return math.sqrt(dx * dx + dy * dy)

d = distance(5, 0, 0, 12)


