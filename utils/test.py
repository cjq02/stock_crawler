#!/usr/bin/env python
  
import time

import time_utils

duration = time_utils.TimeDuration()
duration.start()
time.sleep(5)
duration.stop()
duration.printDurationInfo()
