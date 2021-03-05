import pyautogui as pag

def check_win():
    try:
        x,y = pag.locateCenterOnScreen('next.png', grayscale=True, confidence=0.9)
        print('detected')
        return True
    except:
        print('no changes made')
    try:
        x,y = pag.locateCenterOnScreen('victorylogo.png', grayscale=True, confidence=0.9)
        print('detected')
        return True
    except:
        print('no changes made')

check_win()