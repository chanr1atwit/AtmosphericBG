COLORS = ['red']

while True:
    for c in COLORS:
        s.setColor(c, brightness=1.0)
        info('%s (100%%)'% c)
        time.sleep(1)