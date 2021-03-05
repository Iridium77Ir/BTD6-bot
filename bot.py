from pynput.mouse import Button, Controller
import pyautogui as pag
import pandas as pd
import csv
import time
from os import path
import copy

mouse = Controller()

folder = 'cubismEasy/'

roundBTD = 0
prev_round = -1
faster = False

pag.FAILSAFE = False

def go_to_game():
    filename = 'start.txt'

    df = pd.read_csv(folder + filename, names=['x', 'y', 'time', 'state'])
    starttime = float(df['time'][0])
    
    file = open(folder + filename, "r")
    reader = csv.reader(file, delimiter=',')

    for column in reader:
        print(column)
        sleeptime = abs(starttime - float(column[2]))
        starttime = float(column[2])
        print(sleeptime)
        time.sleep(sleeptime)
        mouse.position = (int(column[0]), int(column[1]))
        print('moved')
        if column[3] == 'dn':
            mouse.press(Button.left)
            print('down')
        elif column[3] == 'up':
            mouse.release(Button.left)
            print('up')
        elif column[3] == 'su':
            mouse.scroll(0, 1)
            print('sup')
        elif column[3] == 'sd':
            mouse.scroll(0, -1)
            print('sdown')

def change_settings():
    mouse.position = (1600,41)
    mouse.press(Button.left)
    mouse.release(Button.left)
    print("open settings")
    time.sleep(1)
    try:
        x,y = pag.locateCenterOnScreen('drop.png', grayscale=True, confidence=0.9)
        pag.click(x, y)
        print('detected')
    except:
        print('no changes made')
    try:
        x,y = pag.locateCenterOnScreen('auto.png', grayscale=True, confidence=0.9)
        pag.click(x, y)
        print('detected')
    except:
        print('no changes made')

    mouse.position = (1319,859)
    mouse.press(Button.left)
    mouse.release(Button.left)

def check_win():
    try:
        x,y = pag.locateCenterOnScreen('next.png', grayscale=True, confidence=0.9)
        pag.click(x, y)
        print('detected')
        return True
    except:
        print('no changes made')
    try:
        x,y = pag.locateCenterOnScreen('victorylogo.png', grayscale=True, confidence=0.9)
        pag.click(813,833)
        print('detected')
        return True
    except:
        print('no changes made')

def check_loss():
    try:
        x,y = pag.locateCenterOnScreen('defeatlogo.png', grayscale=True, confidence=0.9)
        pag.click(700,805)
        print('detected')
        return True
    except:
        print('no changes made')

def check_round():
    global roundBTD, prev_round, faster
    try:
        x,y = pag.locateCenterOnScreen('start.png', grayscale=True, confidence=0.9)
        
        if prev_round != roundBTD:
            do_action()
        prev_round = copy.copy(roundBTD)
        time.sleep(1)

        pag.click(1814,1016)
        print('start round')
        roundBTD += 1
    except:
        print('round started')
    """ try:
        x,y = pag.locateCenterOnScreen('slow.png', grayscale=True, confidence=0.999)
        pag.click(1814,1016)
        print('faster')
    except:
        print('is faster') """
    if roundBTD == 1 and prev_round == 0 and faster == False:
        faster = True
        pag.click(1814,1016)

def placing(filename):
    df = pd.read_csv(folder + filename, names=['x', 'y', 'time', 'state'])
    starttime = float(df['time'][0])
    
    file = open(folder + filename, "r")
    reader = csv.reader(file, delimiter=',')

    for column in reader:
        sleeptime = abs(starttime - float(column[2]))
        starttime = float(column[2])
        print(sleeptime)
        time.sleep(sleeptime)
        mouse.position = (int(column[0]), int(column[1]))
        print('moved')
        if column[3] == 'dn':
            mouse.press(Button.left)
            print('down')
        elif column[3] == 'up':
            mouse.release(Button.left)
            print('up')
        elif column[3] == 'su':
            mouse.scroll(0, 1)
            print('sup')
        elif column[3] == 'sd':
            mouse.scroll(0, -1)
            print('sdown')

def do_action():
    if roundBTD == 0 and path.exists(folder + "1.txt"):
        placing('1.txt')
    elif roundBTD == 1 and path.exists(folder + "2.txt"):
        placing('2.txt')
    elif roundBTD == 2 and path.exists(folder + "3.txt"):
        placing('3.txt')
    elif roundBTD == 3 and path.exists(folder + "4.txt"):
        placing('4.txt')
    elif roundBTD == 4 and path.exists(folder + "5.txt"):
        placing('5.txt')
    elif roundBTD == 5 and path.exists(folder + "6.txt"):
        placing('6.txt')
    elif roundBTD == 6 and path.exists(folder + "7.txt"):
        placing('7.txt')
    elif roundBTD == 7 and path.exists(folder + "8.txt"):
        placing('8.txt')
    elif roundBTD == 8 and path.exists(folder + "9.txt"):
        placing('9.txt')

    elif roundBTD == 9 and path.exists(folder + "10.txt"):
        placing('10.txt')
    elif roundBTD == 10 and path.exists(folder + "11.txt"):
        placing('11.txt')
    elif roundBTD == 11 and path.exists(folder + "12.txt"):
        placing('12.txt')
    elif roundBTD == 12 and path.exists(folder + "13.txt"):
        placing('13.txt')
    elif roundBTD == 13 and path.exists(folder + "14.txt"):
        placing('14.txt')
    elif roundBTD == 14 and path.exists(folder + "15.txt"):
        placing('15.txt')
    elif roundBTD == 15 and path.exists(folder + "16.txt"):
        placing('16.txt')
    elif roundBTD == 16 and path.exists(folder + "17.txt"):
        placing('17.txt')
    elif roundBTD == 17 and path.exists(folder + "18.txt"):
        placing('18.txt')
    elif roundBTD == 18 and path.exists(folder + "19.txt"):
        placing('19.txt')

    elif roundBTD == 19 and path.exists(folder + "20.txt"):
        placing('20.txt')
    elif roundBTD == 20 and path.exists(folder + "21.txt"):
        placing('21.txt')
    elif roundBTD == 21 and path.exists(folder + "22.txt"):
        placing('22.txt')
    elif roundBTD == 22 and path.exists(folder + "23.txt"):
        placing('23.txt')
    elif roundBTD == 23 and path.exists(folder + "24.txt"):
        placing('24.txt')
    elif roundBTD == 24 and path.exists(folder + "25.txt"):
        placing('25.txt')
    elif roundBTD == 25 and path.exists(folder + "26.txt"):
        placing('26.txt')
    elif roundBTD == 26 and path.exists(folder + "27.txt"):
        placing('27.txt')
    elif roundBTD == 27 and path.exists(folder + "28.txt"):
        placing('28.txt')
    elif roundBTD == 28 and path.exists(folder + "29.txt"):
        placing('29.txt')

    elif roundBTD == 29 and path.exists(folder + "30.txt"):
        placing('30.txt')
    elif roundBTD == 30 and path.exists(folder + "31.txt"):
        placing('31.txt')
    elif roundBTD == 31 and path.exists(folder + "32.txt"):
        placing('32.txt')
    elif roundBTD == 32 and path.exists(folder + "33.txt"):
        placing('33.txt')
    elif roundBTD == 33 and path.exists(folder + "34.txt"):
        placing('34.txt')
    elif roundBTD == 34 and path.exists(folder + "35.txt"):
        placing('35.txt')
    elif roundBTD == 35 and path.exists(folder + "36.txt"):
        placing('36.txt')
    elif roundBTD == 36 and path.exists(folder + "37.txt"):
        placing('37.txt')
    elif roundBTD == 37 and path.exists(folder + "38.txt"):
        placing('38.txt')
    elif roundBTD == 38 and path.exists(folder + "39.txt"):
        placing('39.txt')


while True:
    roundBTD = 0
    prev_round = -1
    faster = False
    go_to_game()
    time.sleep(5)
    change_settings()
    while True:
        print(roundBTD, ',', prev_round)
        pag.click(0,0)
        time.sleep(0.5)
        pag.click(0,0)

        time.sleep(2)
        if check_win() == True:
            time.sleep(5)
            break
        if check_loss() == True:
            time.sleep(5)
            break
        
        check_round()
        