# We are going to be looking at approximations of Pi
# as well as looking at the math module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfsides = math.sin(math.radians(halfAngleA))
    sides = oneHalfsides * 2
    polygpmCircumfernce = numSides * sides
    pi = polygpmCircumfernce / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it to make the two close.


# Accumulators

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)
