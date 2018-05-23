# find center of map

from csv import DictReader
import requests
import math
import Tkinter
import webbrowser

sqrt = math.sqrt
atan2 = math.atan2
sin = math.sin
cos = math.cos
pi = math.pi
data_url = '/home/ubuntu/Desktop/tk/coordinaptes.pos'
GPS_url = 'https://maps.googleapis.com/maps/api/staticmap?'
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
coordinates = [v,u]
width = 640
height = 480
zoom = 13
window = Tk()
window.title("etherwhere")
window.minsize(width, height)
preq = requests.PreparedRequest()
preq.prepare_url(GPS_url, {'center':'coordinates', 'size':'800x500'})
mapimage = webbrowser.open(preq.url)
canvas.create_image(0,0,image=mapimage,anchor=Tkinter.NW)
canvas.pack()
window.mainloop()

canvas.pack()
window.mainloop()

print(u)
print(v)
