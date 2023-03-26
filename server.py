import pyautogui
import sched, time
from datetime import datetime

def take_snip(job):
  job.enter(0.5, 1, take_snip, (job,))
  snip = pyautogui.screenshot()
  snip.save("static/snip.webp")

if __name__ == '__main__':
  job = sched.scheduler(time.time, time.sleep)
  job.enter(0.5, 1, take_snip, (job,))
  job.run()