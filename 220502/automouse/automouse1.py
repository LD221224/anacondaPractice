import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())
#     time.sleep(0.1)
# 마우스 좌표 출력

pyautogui.moveTo(1296, 265, 0.2)
# 네이버 검색창 좌표
pyautogui.click()
time.sleep(0.5)

pyperclip.copy('서울 날씨')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

pyautogui.write(['enter'])
time.sleep(1)

start_x = 998
start_y = 277
end_x = 1750
end_y = 743

pyautogui.screenshot(r'220502\automouse\서울날씨.png', 
                     region=(start_x, start_y, end_x-start_x, end_y-start_y))