from mrg_core import util
from mrg_core.util import astro
from mrg_core.util.astro import julian_day
import datetime

blah = julian_day(datetime.datetime(2000, 1, 1, 12, 0, 0))
print(blah)
