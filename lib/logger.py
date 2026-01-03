from datetime import datetime
from time import asctime, sleep


class Logger:
    def __init__(self, class_name: str) -> None:
        self.class_name = class_name

    def info(self, msg: str) -> None:
        print(f'INFO {asctime()} {self.class_name} {msg}')
        for _ in range(9):
            # now = datetime.now().strftime('%a %d-%b-%Y %H:%M:%S')
            # now = datetime.now().strftime('%H:%M:%S')
            # now = datetime.now().isoformat(timespec='seconds')
            now = datetime.now()
            timestamp = (
                f"{now.year:04d}-{now.month:02d}-{now.day:02d}T"
                f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
            )
            print("MANUAL:", timestamp)
            print(timestamp)
            sleep(1)


l = Logger('Logger')
l.info('This is a test!')

print('== =>')

'''
print(":", ord(":"))
print("|", ord("|"))

s = "00:05:23"
print(s)
for c in s:
    print(c, ord(c))
'''

