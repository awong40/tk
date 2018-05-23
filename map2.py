# find center of map

from csv import DictReader
import requests
import math
import Tkinter
import webbrowser
import urllib
import PIL
from PIL import Image,ImageTk
from io import BytesIO
import base64

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
str_coor = "%.7f,%.7f" % (v,u)
preq= requests.PreparedRequest()
preq.prepare_url(GPS_url, {'center':str_coor, 'size':'800x500', 'zoom':zoom})
print(preq.url)

master = Tkinter.Tk()
master.title("etherwhere")
#master.minsize(width, height)
urlreader = urllib.urlopen(preq.url)
imgdata = urlreader.read()
urlreader.close()
base64data = base64.encodestring(imgdata)
image = Tkinter.PhotoImage(data=base64data)
w = Tkinter.Canvas(master, width =width, height= height)
w.create_image(0,0, image=image, anchor=Tkinter.NW)
w.pack()
master.mainloop()


