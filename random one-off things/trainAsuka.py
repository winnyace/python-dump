# # I made this to get some points on a Discord bot.

import pyautogui
import time

time.sleep(5)
while True:
    for i in range(20):
        print(i)
        pyautogui.write('train')
        pyautogui.press('enter')
        time.sleep(1.5)
    time.sleep(10)
