import math

points = [(3,4), (6,8), (5,12), (8,10), (-5, 10)]

distances = []
# To find the distances by using the formula
def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar."""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Looping through the points and getting all combinations of the distances
for i in range(len(points) -1):
    for j in range(i+1,len(points)):
        distance = round(euclideanDistance(points[i], points[j]),2)
        distances.append(distance)

# printing the minimum distance
min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)

