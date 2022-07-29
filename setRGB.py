#setRGBColor for LED strip
LENGTH = 30 #setLength
s = ShellLabStrip(PORT, length=0) 
ls = Ws2812.LEDS(s, LENGTH ) #connectLED strips
# adjust the light power (brightness)
ON = 255
RED, GREEN, BLUE = ON<<16, ON<<8, ON
all_red = [RED] * LENGTH
all_green = [GREEN] * LENGTH
all_blue = [BLUE] * LENGTH
rainbow = [ RED, GREEN, RED+GREEN, BLUE, BLUE+RED, BLUE+GREEN, RED+GREEN+BLUE ]
rainbow = rainbow * (int(LENGTH/len(rainbow))+1)  # duplicate to be large enough

# test three basic colors
ls.write(all_red)
time.sleep(1)
ls.write(all_green)
time.sleep(1)
ls.write(all_blue)
time.sleep(1)

# RGB Colors Movement
while True:
    ls.write(rainbow[:LENGTH])
    #rainbow.append(rainbow.pop(0))  # left
    rainbow.insert(0,rainbow.pop())  # right
    time.sleep(0.1)

