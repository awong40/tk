/* calculations for azimuth and elevation */
/* inputs include satellite x,y,z and receiver l,l,h */

import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import izip
xyzURL = '/home/ubuntu/Desktop/tk/sp3data'
llhURL = '/home/ubuntu/Desktop/tk/rtk_ew_data/llh_data/py'

a = 6378137
b = 6356752.3142
f = (a - b)/a
e_sq = f * (2-f)

k = 0
n = 0 

with open(xyzURL, "rt") as g:
  for line in g:
    n = n +1
    b = line.split()
    l = [float(dd) for dd in b]
    x = l[0]
    y = l[1]
    z = l[2]
   
with open(llhURL, "rt") as j:
  data = j.read()
  q = data.split()
  w = [float(blah) for blah in q]
  lat = w[0]
  long = w[1]
  h = w[2]

print(x,y,z)
print(lat,long,h)

def llh2ecef:
  e = 0.08181979099211
  P = a^2/sqrt( (r_e*cos(long))^2 + (b*sin(long))^2 )
  lat0 = (P+h)*cos(long)*cos(lat)
  long0 = (P+h)*cos(long)*sin(lat)
  h0 = (P*(b/a)^2 + h)*sin(long)
  return lat0,long0,h0
  
def ecef2enu(x,y,z,lat0,long0,h0):
  lamb = math.radians(lat0)
  phi = math.radians(long0)
  s = math.sin(lamb)
  N= a/math.sqrt(1-e_sq*s*s)
  
  sin_lambda = math.sin(lamb)
  cos_lambda = math.cos(lamb)
  sin_phi = math.sin(phi)
  cos_phi = math.cos(phi)
  
  x0 = (h0+N)*cos_lambda*cos_phi
  y0 = (h0+N)*cos_lambda*sin_phi
  z0 = (h0+(1-e_sq)*N)*sin_lambda
  
  xd = x - x0
  yd = y-y0
  zd = z-z0
  
  xEast = -sin_phi*xd + cos_phi*yd
  yNorth = -cos_phi*sin_lambda*xd 
  zUp = cos_lambda*cos_phi*xd + cos_lambda*sin_phi*yd + sin_lambda*zd
  
  horiz = math.sqrt(yNorth**2+xEast**2)
  zenith = math.atan2(horiz*xEast*yNorth,zUp)
  azimuth = math.atan2(xEast,yNorth)
  return zenith, azimuth

blah = ecef2enu(x,y,z,lat0,long0,h0)
print(blah)
