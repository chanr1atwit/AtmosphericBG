LENGTH = 30
s = ShellLabStaticStrip(PORT, length=LENGTH)
s.reset()

COLORS = ['red','green','blue','yellow','cyan','purple','white']
#setShiftingSingleColor
s.reset()
while True:
    r = random.randint(0,7)*32
    g = random.randint(0,7)*32
    b = random.randint(0,7)*32
    s.color((r<<16)+(g<<8)+(b))
    time.sleep(1)
