import keyboard as kb
import datetime
import manager
import copy
import random

class alarm:
    
    def __init__(this, name, dateTime,repeat, mus,volume,useGenetic, usePuzzle):

        populationSize = 5
        
        #ATRIBS
        this.name = name
        this.dateTime = dateTime
        this.repeat = repeat
        this.mus = mus
        this.volume = volume
        this.useGenetic = useGenetic
        this.usePuzzle = usePuzzle
        this.activate = True
        this.wakeTime = 160
        
        #POPULATION MAKER FOR GENETIC
        transfer = copy.copy(this)
        transfer.wakeTime = 200
        this.population = manager.manager()
        this.population.add_alarm(transfer)
        
        for i in range(0, populationSize):
            
            transfer.volume = this.volume + random.randint(-15, 15) 
            transfer.mus = this.population.avaibleSongs[random.randint(0,len(this.population.avaibleSongs) - 1)]
            transfer.usePuzzle = bool(random.getrandbits(1))
            this.population.add_alarm(transfer)
        

    def list(this): #metodo legacy, para testes
        print("Name: " + this.name)
        if this.repeat:
            print("Date: (Repeating Alarm)")
        else:
            print("Date: " + this.dateTime.strftime("%m/%b/%Y"))
        print("Time: " + this.dateTime.strftime("%H:%M"))
        print("Music: " + this.mus)
        print("AI Enabled: " + str(this.useGenetic))
        print("Puzzle Enabled: " + str(this.usePuzzle))
        print("Activated: " + str(this.activate))
    
    def get_wakeTime(this):

        return this.wakeTime

        
        
    
    
