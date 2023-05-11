from ahk import AHK
ahk = AHK()
import keyboard

while True:
    if keyboard.is_pressed('1'):
        while True:
            print('Process')
            ahk.click()
            if keyboard.is_pressed('2'):
                print('STOP')
                break