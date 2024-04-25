import math

distances = []
points = [(3,4), (6,8), (5,12), (8,10), (-5, 10)]

# To find the distances by using the formula
def euclideanDistance(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Looping through the points and getting all combinations of the distances
for a in range(len(points) -1):
    for b in range(a+1,len(points)):
        distance = round(euclideanDistance(points[a], points[b]),2)
        distances.append(distance)

# printing the minimum distance
print(min(distances))

