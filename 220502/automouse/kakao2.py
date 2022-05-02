import pyautogui
import pyperclip
import time
import schedule


def send_message():
    picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao1.png')
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao2.png')
        print(picPosition)
        
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'220502\automouse\kakao3.png')
        print(picPosition)
        
    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('이 메시지는 자동으로 보내는 메시지 입니다.')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.0)

    pyautogui.write(['enter'])
    time.sleep(1.0)

    pyautogui.write(['escape'])
    time.sleep(1.0)
    
# 매 10초마다 send_message 함수 실행 스케줄 등록
# schedule.every(10).seconds.do(send_message)
# 매주 월요일 9시 10분마다 실행
# schedule.every().monday.at('09:10').do(send_message)
# 매일 16시 37분마다 실행
schedule.every().day.at('16:37').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
    