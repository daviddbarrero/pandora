from __future__ import print_function
import time
import pychromecast

# Your Chromecast device Friendly Name
device_friendly_name = "Andy"

chromecasts = pychromecast.get_chromecasts()

# select Chromecast device
cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_friendly_name)

# wait for the device
cast.wait()
print(cast.device)
print(cast.status)

# get media controller 
mc = cast.media_controller

mc = cast.media_controller

mc.block_until_active()
print(mc.status)

