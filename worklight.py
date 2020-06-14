import time
import magichue
import sys

light_ip="192.168.1.64"

light = magichue.Light(light_ip) 
colors = {
    "red": (255,0,0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (255, 0, 255),
    "yellow": (255, 255, 0), 
    "cyan": (0,255,255),
    "pink": (255,0,255)
}


if len(sys.argv) <= 2:
    if sys.argv[1] == "on":
        light.is_white = True
        light.brightness = 255

    elif sys.argv[1] == "off":
        light.on=False

else:
    if sys.argv[2].isdigit():
        if sys.argv[1] == "on":
            light.is_white = True
            light.brightness = int(round(((float(sys.argv[2])/100)*255),0))

        elif sys.argv[1] == "off":
            light.on=False
    else:
        if sys.argv[1] == "on":
            light.is_white = False
            light.rgb = (colors[sys.argv[2]])
            light.brightness = 255

        elif sys.argv[1] == "off":
            light.on = False 
    


