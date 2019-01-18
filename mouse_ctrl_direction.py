import pyautogui as pag,time

pag.FAILSAFE=True
sx,sy=pag.size()
pag.click(sx/2,sy/2)
xw=['left','' ,'right']
yw=['up','' ,'down']

while True:
    x,y=pag.position()
    if x==0 and y==0:
        break
    else:
        pass
    try:
        pag.press(xw[3*x//sx])
    except:
        pass
    try:
        pag.press(yw[3*y//sy])
    except:
        pass
    time.sleep(0.3)
