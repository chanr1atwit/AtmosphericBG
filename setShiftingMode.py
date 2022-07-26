COLORS = ['red','green','blue','yellow','cyan','purple','white']

s.reset(freq=10)
for i in range(10):
    s.color('red')
    time.sleep(0.5)
    s.color('blue')
    time.sleep(0.5)

s.reset()
while True:
    r = random.randint(0,7)*32
    g = random.randint(0,7)*32
    b = random.randint(0,7)*32
    s.color((r<<16)+(g<<8)+(b))
    time.sleep(1)
