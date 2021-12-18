from plyer import notification
import time
import subprocess

NOTIFICATION_COUNTER = 0

while True:
    # sleep for 20 minutes before notification
    time.sleep(1200)

    # show notification
    notification.notify(
        title='Sleep checker',
        message='Are you awake or asleep',
        app_name="",
        app_icon=r"C:\Users\Jeffrey Alahira\Documents\Python\sleep_checker\sleep.ico",
        timeout=60,
    )

    # count number of times notification shows
    NOTIFICATION_COUNTER += 1

    # hibernate system if notification shows three times
    if(NOTIFICATION_COUNTER) == 3:
        subprocess.run(['shutdown', '-h'])
        exit()
