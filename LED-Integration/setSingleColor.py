LENGTH = 30
s = ShellLabStaticStrip(PORT, length=LENGTH)
s.reset()

COLORS = ['blue'] #available colors 'red','green','blue','yellow','cyan','purple','white'

# show classic color
while True:
    for c in COLORS:
        s.setColor(c, brightness=1.0)
        info('%s (100%%)'% c)
        time.sleep(1)
