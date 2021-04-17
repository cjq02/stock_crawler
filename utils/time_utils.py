import datetime
import time


class TimeDuration(object):
    'Time duration.'

    def __init__(self):
        pass

    def start(self):
        self.start_time = datetime.datetime.now()
        self.end_time = None

    def stop(self):
        if self.start_time is None:
            print("ERROR: start() must be called before stop().")
            return

        self.end_time = datetime.datetime.now()

    def getTillNow(self):
        delta = datetime.datetime.now() - self.start_time
        delta_gmtime = time.gmtime(delta.total_seconds())
        durationStr = time.strftime("%H:%M:%S", delta_gmtime)
        return durationStr

    def printDurationInfo(self):
        'String of duration with the format "%H:%M:%S".'
        if self.start_time is None or self.end_time is None:
            print("ERROR: start() and stop() must be called first.")
            return

        delta = self.end_time - self.start_time
        delta_gmtime = time.gmtime(delta.total_seconds())
        durationStr = time.strftime("%H:%M:%S", delta_gmtime)
        print('开始时间：{}'.format(self.start_time))
        print('结束时间：{}'.format(self.end_time))
        print('总耗时：{}'.format(durationStr))
