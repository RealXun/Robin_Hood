points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

seen = []
dupes = []
for point in points:
    if point not in seen:
        seen.append(point)
    else:
        dupes.append(point)

if (len(dupes) == 0):
    print('No one can do it other than Mr Robin Hood')
else:
    print('Yes of course. Duplicated shots: ', dupes)
# 1
bullseye = []
for i in range(len(points)):
    if points[i] in points[i+1:]:
        bullseye.append(points[i])
print(bullseye)

# 2
q1 = []
q2 = []
q3 = []
q4 = []
count = 0
while count < len(points):
    for Point0,Point1 in points[count:count+1]:
        if Point0 > 0 and Point1 > 0:
            q1.append(points[count])
        elif Point0 > 0 and Point1 < 0:
            q4.append(points[count])
        elif Point0 < 0 and Point1 > 0:
            q2.append(points[count])
        elif Point0 < 0 and Point1 < 0:
            q3.append(points[count])
    count += 1
solution = "There is a total of " + str(len(q1)) + " arrows in quadrant 1, " + str(len(q2)) + " arrows in quadrant 2, " + str(len(q3)) + " arrows in quadrant 3 and " + str(len(q4)) + " arrows in quadrant 4."
print(solution)
print(points[7:].index((5,7)))


# 3
##defining distance from center

import math
def from_center(shot):
    Point0 = shot[0]
    Point1 = shot[1]
    distance = math.sqrt(Point0**2 + Point1**2)
    return distance

##creating list of distances

distances = []
for i in points:
    distances.append(round(from_center(i), 2))
print(distances)
##creating list of closest points

counter = 0
marksman = []
for i in distances:
    if i == min(distances):
         marksman.append(points[counter])
    counter += 1    

##printing solution

print("The closest point(s) to the center is(are):", marksman)
print("The distance of the closest point to the center is:", min(distances))
import numpy
dist = numpy.linalg.norm(points,)
print(dist)


# 4

radius = 9
print(sum(1 for i in distances if i > radius), "arrows didn't meet the target. Robin shoots in misterious ways.")
