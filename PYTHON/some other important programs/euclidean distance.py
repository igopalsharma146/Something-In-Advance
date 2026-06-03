#euclidean distance
import math
def euclidean_distance(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensions")
    
    distance = 0
    for p1, p2 in zip(point1, point2):
        distance += (p1 - p2) ** 2
    
    return math.sqrt(distance)
# Example usage
pointA = [3, 4]
pointB = [7, 1]
print(euclidean_distance(pointA, pointB))