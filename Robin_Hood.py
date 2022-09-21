puntos = [(4,5), (-0,2), (4,7), (1,-3), (3,-2), (4,5), (3,2), (5,7), (-5,7), (2,2), (-4,5), (0,-2), (-4,7), (-1,3), (-3,2), (-4,-5), (-3,2), 
          (5,7), (5,7), (2,2), (9, 9), (-8, -9)]

#1. Robin Hood is famous for hitting an arrow with another arrow. Has he got it?
points = [(4,5), (-0,2), (4,7), (1,-3), (3,-2), (4,5), (3,2), (5,7), (-5,7), (2,2), (-4,5), (0,-2), (-4,7), (-1,3), (-3,2), (-4,-5), (-3,2), (5,7), (5,7), (2,2), (9, 9), (-8, -9)]
result = set([point for point in points if points.count(point) > 1])
print("Robin Hood hitted this arrow with another arrow : " + str(result))
# 2. Calculate how many arrows have fallen in each quadrant.
q1 = []
q2 = []
q3 = []
q4 = []
center = 0
shot1, shot2 = zip(*points)
for point in range(len(shot1)):
    if (shot1[point] >= 0 and shot2[point] >= 0):
        q1.append(point)
    elif (shot1[point] < 0 and shot2[point] >= 0):
        q2.append(point)
    elif (shot1[point] < 0 and shot2[point] < 0):
        q3.append(point)
    elif (shot1[point] >= 0 and shot2[point] < 0):
        q4.append(point)
print('Shots in quadrant 1 = ', len(q1))
print('Shots in quadrant 2 = ', len(q2))
print('Shots in quadrant 3 = ', len(q3))
print('Shots in quadrant 4 = ', len(q4))
# 3. Find the closest point to the center. Calculate its distance from the center
# Defining a function that calculates the distance to the center can help.

#The Solution is Coming soon!!!!!!

# 4. If the target has a radius of 9, calculate the number of arrows to collect from the forest.
shots_failed = []

for point in points:
    if (abs(point[0]) >= 9 or abs(point[1]) >= 9):
        shots_failed.append(point)
        
print('The list of failed shots is: ', shots_failed)
print('The number of failed shots are: ', len(shots_failed))
