from datetime import datetime, timedelta
import time

from app.services.background.scheduler import Scheduler
from app.services.background.scheduled_task import ScheduledTask


scheduler = Scheduler()


def reminder():

    print("Reminder fired!")


scheduler.schedule(

    ScheduledTask(

        name="Assignment",

        execute_at=datetime.now()

        + timedelta(seconds=5),

        callback=reminder

    )

)

scheduler.start()

time.sleep(8)

scheduler.stop()