ls = Ws2812.LEDS(s, LENGTH )
# adjust the light power (brightness)
ON = 255 
RED, GREEN, BLUE = ON<<16, ON<<8, ON
rainbow = [ RED, GREEN, RED+GREEN, BLUE, BLUE+RED, BLUE+GREEN, RED+GREEN+BLUE ]

STEP = 30
r, g, b = 0, 0, 0
while True:
    for color in rainbow:
        for i in range(STEP):
            r = int(((color>>16) & 0xFF) * i / STEP)
            g = int(((color>>8) & 0xFF) * i / STEP)
            b = int(((color) & 0xFF) * i / STEP)
            c = (r<<16) + (g<<8) + b
            info( 'R:%d G:%d B:%d'% (r,g,b) )
            ls.pushf( [c] )
            time.sleep(0.1)

