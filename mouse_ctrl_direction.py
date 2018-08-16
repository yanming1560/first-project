import pyautogui as pag,time

pag.FAILSAFE=True
sx,sy=pag.size()
pag.click(sx/2,sy/2)

while True:
    x,y=pag.position()
    if sx/3<x<sx*2/3 and 0<=y<sy/3:
        pag.press('up')
    elif sx/3<x<sx*2/3 and sy*2/3<y<=sy:
        pag.press('down')
    elif 0<=x<sx/3 and sy/3<y<sy*2/3:
        pag.press('left')
    elif sx*2/3<x<=sx and sy/3<y<sy*2/3:
        pag.press('right')
    time.sleep(0.3)