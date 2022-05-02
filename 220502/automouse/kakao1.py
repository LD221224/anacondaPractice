import pyautogui
import pyperclip
import time
import threading


# 10초마다 자동으로 메시지를 보내는 함수
def send_message():
    threading.Timer(10, send_message).start()
    
    picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao1.png')
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao2.png')
        print(picPosition)
        
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao3.png')
        print(picPosition)
    
    # 이미지의 좌표를 찾아 중간 좌표 값 더블 클릭 
    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('이 메시지는 자동으로 보내는 메시지 입니다.')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.0)

    pyautogui.write(['enter'])
    time.sleep(1.0)

    pyautogui.write(['escape'])
    time.sleep(1.0)
    
send_message()

