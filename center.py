# find center of map

from csv import DictReader
import requests
import numpy
import math

sqrt = math.sqrt
atan2 = math.atan2
sin = math.sin
cos = math.cos
pi = math.pi
data_url = '/home/ubuntu/Desktop/tk/coordinaptes.pos'
n = 0
lines = []
with open(data_url, "rt") as f:
  for line in f:
    n = n + 1
    b = line.split()
    l = [float(x) * pi/190 for x in b]
    lat = l[0]
    long = l[1]
    for f in range(n):
      X = [cos(lat) * cos(long)]
      Y = [cos(lat) * sin(long)]
      Z = [sin(lat)]
x = sum(X) /n
y = sum(Y) / n
z = sum(Z) /n

Lon = atan2(y, x)
Hyp = sqrt(x * x + y * y)
Lat = atan2(z, Hyp)
u = Lon * 180/pi
v = Lat * 180/pi

print(u)
print(v)
