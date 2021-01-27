import pyautogui
import subprocess
from datetime import datetime
import pyscreeze
import time

def sign_in(meetingID, Password):
    subprocess.call(["/usr/bin/open", "/Applications/Zoom.app"])
    time.sleep(10)
    join_btn=pyautogui.locateCenterOnScreen('join_btn.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(2)

    meeting_id=pyautogui.locateCenterOnScreen('meeting_id.png')
    pyautogui.moveTo(meeting_id)
    pyautogui.click()
    pyautogui.typewrite(meetingID)
    time.sleep(2)

    check_boxs=pyautogui.locateAllOnScreen('check_box.png')
    for check_box in check_boxs:
        pyautogui.moveTo(check_box)
        pyautogui.click()
        time.sleep(2)
    
    join_meeting=pyautogui.locateCenterOnScreen('join_meeting.png')
    pyautogui.moveTo(join_meeting)
    pyautogui.click()
    time.sleep(2)

    password=pyautogui.locateCenterOnScreen('password.png')
    pyautogui.moveTo(password)
    pyautogui.click()
    pyautogui.typewrite(Password)
    pyautogui.press('enter')

meetingID=input("Enter Your Meeting ID: ")
Password=input("Enter Your Password: ")
time=input("Enter Your time: ")
timeData=datetime.now()
currentTime=timeData.strftime("%H:%M")
if time==currentTime:
    sign_in(meetingID, Password)

else:
    while not time==currentTime:
        timeData=datetime.now()
        currentTime=timeData.strftime("%H:%M")
        if time==currentTime:
            sign_in(meetingID, Password)
