import pyautogui

pyautogui.PAUSE= 1

pyautogui.FAILSAFE= True

print(pyautogui.size())

pyautogui.moveTo(200,100,2)

pyautogui.moveRel(70,10,2)

print(pyautogui.position())

#pyautogui.click(30, 35, button="right")

pyautogui.mouseDown()
pyautogui.moveTo(500, 500, 3)
pyautogui.mouseUp()

pyautogui.doubleClick()
pyautogui.middleClick()

pyautogui.dragTo()
pyautogui.dragRel()

pyautogui.scroll(50)

pyautogui.typewrite("Hello word!!!")

pyautogui.typewrite(["A", "esc", "enter","right"])