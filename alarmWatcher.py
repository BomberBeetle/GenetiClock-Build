import datetime
import manager
import alarms
import keyboard
import time
class alarmWatcher:
    run = True
    def __init__(this, manager):
        this.mng = manager

    def watcher(this):
        while this.run:
            for i , a in enumerate(this.mng.alarms):
                if a.activate:
                    if a.repeat:              
                        if a.dateTime.minute + (a.dateTime.hour*60) == datetime.datetime.now().minute + (datetime.datetime.now().hour*60):
                            this.mng.trigger(i)
                            while True:
                                if keyboard.is_pressed('a'):
                                    this.mng.stop()
                                    break
                            
                    elif a.dateTime.date() == datetime.datetime.now().date() and a.dateTime.minute + a.dateTime.hour*60 == datetime.datetime.now().minute + datetime.datetime.now().hour*60:
                            this.mng.trigger(i)
                            while True:
                                if keyboard.is_pressed('a'):
                                    this.mng.stop()
                                    break
