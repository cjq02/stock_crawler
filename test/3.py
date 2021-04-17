import time

from utils.time_utils import TimeDuration

duration = TimeDuration()
duration.start()
time.sleep(5)
duration.stop()
