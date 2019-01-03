import alarms
import datetime
import manager
al = alarms.alarm("???" ,datetime.datetime.now(), True, "test.mp3", False, False)
mng =  manager.manager()
mng.add_alarm(al)
mng.alarms[0].list()
mng.trigger(0)
input('yo ')
mng.stop()
print(mng.alarms[0].wakeTime)
mng.remove_alarm(0)
if len(mng.alarms) == 0 :
    print('it just works.')
else:
    print('MUDA MUDA MUDA MUDA')
