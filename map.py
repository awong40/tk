import Tkinter
import urllib
import urllib.request
import base64
def getaddress(location, width, height, zoom):

    locationnospaces = urllib.quote_plus(location)

    address = "http://maps.googleapis.com/maps/api/staticmap?\

center={0}&zoom={1}&size={2}x{3}&format=gif&sensor=false"\

.format(locationnospaces, zoom, width, height)

    return address

def getmap(location, width, height, zoom):

    address = getaddress(location, width, height, zoom)

    urlreader = urllib.urlopen(address)

    data = urlreader.read()

    urlreader.close()

    base64data = base64.encodestring(data)

    image = Tkinter.PhotoImage(data=base64data)

    return image
