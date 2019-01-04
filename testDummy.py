import alarms
import manager
import datetime
import copy

standardTime = 300

a = alarms.alarm("Retardo", datetime.datetime.now(), True, "battle.ogg",50,True, False)

mng= manager.manager()

mng.add_alarm(a)

for i in range(0, 5):

    mng.alarms[0].population.alarms[0].wakeTime = copy.copy(standardTime)
    
    if mng.alarms[0].population.alarms[0].mus == "joker.ogg":

        mng.alarms[0].population.alarms[0].wakeTime -= 30

    if mng.alarms[0].population.alarms[0].usePuzzle == True:

        mng.alarms[0].population.alarms[0].wakeTime -= 30

    mng.alarms[0].population.alarms[0].wakeTime -= mng.alarms[0].population.alarms[0].volume - 50

    print(mng.alarms[0].population.alarms[0].wakeTime)

    mng.execute_genetic(0)

            
        

    

