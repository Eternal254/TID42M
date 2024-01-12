import pyautogui, time

time.sleep(3)
a=0

while a < 1000:
    pyautogui.typewrite('.')
    pyautogui.press('enter')
    a = a+1