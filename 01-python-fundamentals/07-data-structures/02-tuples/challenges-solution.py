import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":
    p1 = (3, 4)
    p2 = (0, 0)
    print(f"Distance between {p1} and {p2} is: {calculate_distance(p1, p2)}")
