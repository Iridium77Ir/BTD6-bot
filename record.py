from pynput import mouse
import time

with open("click.txt", "w") as myfile:
            myfile.write('')

def on_scroll(x, y, dx, dy):
    if dy >= 0:
        content = str(x) + ',' + str(y) + ',' + str(time.time()) + ',su\n'
    else:
        content = str(x) + ',' + str(y) + ',' + str(time.time()) + ',sd\n'
    with open("click.txt", "a") as myfile:
        myfile.write(content)

def on_click(x, y, button, pressed):
    if str(button) == 'Button.right':
        return False
    if pressed:
        content = str(x) + ',' + str(y) + ',' + str(time.time()) + ',dn\n'
        with open("click.txt", "a") as myfile:
            myfile.write(content)
    else:
        content = str(x) + ',' + str(y) + ',' + str(time.time()) + ',up\n'
        with open("click.txt", "a") as myfile:
            myfile.write(content)

# Collect events until released
with mouse.Listener(on_scroll=on_scroll,
        on_click=on_click) as listener: 
    listener.join() 