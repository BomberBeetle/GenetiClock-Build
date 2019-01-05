import alarms
import manager
import datetime
import copy
import random
import time

standardTime = 100

a = alarms.alarm("Oh.", datetime.datetime.now(), True, "battle.ogg",50,True, False)

mng= manager.manager()

mng.add_alarm(a)

waketimes = 0

#cycles to do
cycles = 10000

#number of days in each cycle
days = 6
for i in range(0, cycles+1):

    randPuzzle = bool(random.getrandbits(1))

    randVolume = random.randint(0, 101)

    randSong = mng.avaibleSongs[random.randint(0,len(mng.avaibleSongs) - 1)]
    
    mng.alarms[0] = alarms.alarm("Test", datetime.datetime.now, True, mng.avaibleSongs[random.randint(0,len(mng.avaibleSongs) - 1)], random.randint(0, 101),True,bool(random.getrandbits(1)) )

    for j in range(0, days+1):
        

        mng.alarms[0].population.alarms[0].wakeTime = copy.copy(standardTime)
    
        if mng.alarms[0].population.alarms[0].mus == randSong:

            mng.alarms[0].population.alarms[0].wakeTime -= 33

        if mng.alarms[0].population.alarms[0].usePuzzle == randPuzzle:

            mng.alarms[0].population.alarms[0].wakeTime -= 33

        mng.alarms[0].population.alarms[0].wakeTime -= (mng.alarms[0].population.alarms[0].volume - randVolume)/3  

        if j == days:
            
           waketimes += mng.alarms[0].population.alarms[0].wakeTime
           
        else:
            
            mng.execute_genetic(0)



print("Final: " , 100 - waketimes/cycles, "% eff")


    

    



        
        

    

