import time
from blink1.blink1 import Blink1
import asyncio
from winsdk.windows.ui.notifications.management import UserNotificationListener
from winsdk.windows.ui.notifications import NotificationKinds

async def notify():
    b1 = Blink1()

    while True:
        # check status update every 3 second
        time.sleep(3)

        listener = UserNotificationListener.get_current()
        notifications = await listener.get_notifications_async(NotificationKinds.TOAST)
        
        if  1 <= len(notifications) <= 3:
            b1.fade_to_color(100, 'green')
        elif  3 <= len(notifications) <= 5:
            b1.fade_to_color(100, 'yellow')
        elif len(notifications) == 0:
            b1.stop()
            b1.fade_to_color(100,'black')

if __name__ == '__main__':
    asyncio.run(notify())
