# coding=utf-8
import datetime
import copy
import alarms
import time
import multiprocessing
from pygame import mixer
import os
import random
import operator

class manager:
   
    def __init__(this):
        this.alarms = []
        this.tr = 0
        this.run = True
        
        #define o tipo de sinalizacao de  diretorio baseado no OS
        if os.name == "Windows":
            this.dirSlash = "\\"
        else:
            this.dirSlash = "/"
            
        #pega as musikas disponivess
        this.refresh_songs()

    def trigger(this, index):
        mixer.init();
        
        #se a musica n existe ele pega uma aleatoria
        if not os.path.exists("mp3" + this.dirSlash +this.alarms[index].mus):
            this.refresh_songs()
            this.alarms[index].mus = this.avaibleSongs[random.randint(0,len(this.avaibleSongs) - 1)]
            this.alarms[index].population.alarms[0].mus = this.avaibleSongs[random.randint(0,len(this.avaibleSongs) - 1)]
        mixer.music.set_volume(this.alarms[index].volume/10)
        mixer.music.load("mp3" + this.dirSlash + this.alarms[index].mus) #carrega a musica
        mixer.music.play(-1) #toca a musica em looooooop
        this.tr = index #coloca o index do alarme que ta tocano
            
    def stop(this):
        mixer.music.stop() #PARA TUDO MIGAAA!!!
        wakeTime = ((datetime.datetime.now().minute*60 + datetime.datetime.now().second) - (this.alarms[this.tr].dateTime.minute*60 + this.alarms[this.tr].dateTime.second))

        #calcula o tempo pra acordar (em s) baseado no tempo atual - tempo de ativação (importante pra quando eu for implementer o beregonelson genetico) 
        this.alarms[this.tr].population.alarms[0].wakeTime = wakeTime        

        # puta que pariu
        #time.sleep(60 - datetime.datetime.now().second)
        if this.alarms[this.tr].useGenetic == True:
            this.execute_genetic(this.tr)

    def add_alarm(this, alarm):
        this.alarms.append(copy.copy(alarm))
        #enfia um alarme
        
    def remove_alarm(this, index):
        this.alarms.pop(index)
        #tira um alarme
        
    def watcher(this, q):
        mngr = q.get()
        while mngr.run:
            for i , a in enumerate(mngr.alarms):
                if a.activate:
                    if a.repeat:              
                        if a.dateTime.minute + (a.dateTime.hour*60) == datetime.datetime.now().minute + (datetime.datetime.now().hour*60):
                            this.trigger(i)
                            while True:
                                
                                if keyboard.is_pressed('a'):
                                    this.stop()
                                    break
                            
                    elif a.dateTime.date() == datetime.datetime.now().date() and a.dateTime.minute + a.dateTime.hour*60 == datetime.datetime.now().minute + datetime.datetime.now().hour*60:
                            this.trigger(i)
                            while True:
                                
                                if keyboard.is_pressed('a'):
                                    this.stop()
                                    break

    def refresh_songs(this):
        
        this.avaibleSongs = []
        
        for root, dirs, files in os.walk("mp3"):
            
            for filename in files:
                
                if filename.split(".")[1].lower() == "mp3" or filename.split(".")[1].lower() == "ogg" or filename.split(".")[1].lower() == "wav" or filename.split(".")[1].lower() == "xm" or filename.split(".")[1].lower() == "mod":

                    this.avaibleSongs.append(filename)

    def execute_genetic(this, index):
        
        #Sort by fitness
        this.alarms[index].population.alarms.sort(key = lambda x: x.wakeTime)        

        #Breeding
        parent1 = copy.copy(this.alarms[index].population.alarms[0])
        parent2 = copy.copy(this.alarms[index].population.alarms[1])
        breedVolume = bool(random.getrandbits(1))
        breedMus = bool(random.getrandbits(1))
        breedPuzzle = bool(random.getrandbits(1))
        timesSwitched = 0
        
        if breedVolume:

            parent1.volume, parent2.volume = parent2.volume, parent1.volume
            timesSwitched += 1

        if breedMus:
                
            parent1.mus, parent2.mus = parent2.mus, parent1.mus
            timesSwitched += 1

        if breedPuzzle:

            parent1.usePuzzle, parent2.usePuzzle = parent2.usePuzzle, parent1.usePuzzle
            timesSwitched += 1

        parent1.wakeTime = parent2.wakeTime*((33*timesSwitched)/100) + parent1.wakeTime*((33*3 - timesSwitched)/100)
        parent2.wakeTime = parent1.wakeTime*((33*timesSwitched)/100) + parent2.wakeTime*((33*3 - timesSwitched)/100)

        #Mutation
        this.mutate(parent1)
        this.mutate(parent2)
        this.alarms[index].population.alarms[len(this.alarms[index].population.alarms) - 1] = parent1
        this.alarms[index].population.alarms[len(this.alarms[index].population.alarms) - 2] = parent2


        #re-sort para colocar o alarme ativo da população como o mais fit (menor wakeTime)
        this.alarms[index].population.alarms.sort(key = lambda x: x.wakeTime)

        
        #set do alarme ativo para o mais fit
        this.alarms[index].mus = this.alarms[index].population.alarms[0].mus
        this.alarms[index].volume = this.alarms[index].population.alarms[0].volume
        this.alarms[index].usePuzzle = this.alarms[index].population.alarms[0].usePuzzle
        
        #succ
        
        
    def get_wakeTime(this, alarm):

        return alarm.wakeTime

    #Fitness prediction function (too aggresive)        
    def set_fitness(this, index):
        
        for x in range( 2, len(this.alarms[index].population.alarms)):
            
            if this.alarms[index].population.alarms[x].mus == this.alarms[index].population.alarms[0].mus:
                
                this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[0].wakeTime)/3
                try:
                    
                    this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[0].wakeTime)/(3*((abs(this.alarms[index].population.alarms[x].volume - this.alarms[index].population.alarms[0].volume))/100))

                except ZeroDivisionError:
                    
                    this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[0].wakeTime)/3

            elif this.alarms[index].population.alarms[x].mus == this.alarms[index].population.alarms[1].mus:

                this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[1].wakeTime)/3
                try:
                    

                    this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[1].wakeTime)/(3*((abs(this.alarms[index].population.alarms[x].volume - this.alarms[index].population.alarms[1].volume))/100))
                except ZeroDivisionError:
                    
                    this.alarms[index].population.alarms[x].wakeTime -= (this.alarms[index].population.alarms[x].wakeTime - this.alarms[index].population.alarms[1].wakeTime)/3
            
            if this.alarms[index].population.alarms[x].usePuzzle == this.alarms[index].population.alarms[0].usePuzzle:

                this.alarms[index].population.alarms[x].wakeTime -= this.alarms[index].population.alarms[0].wakeTime/3

            elif this.alarms[index].population.alarms[x].usePuzzle == this.alarms[index].population.alarms[1].usePuzzle:

                this.alarms[index].population.alarms[x].wakeTime -= this.alarms[index].population.alarms[1].wakeTime/3

    def mutate(this, alarm):

        mutateVolume = random.randint(0, 101)
        mutateMus = random.randint(0, 101)
        mutatePuzzle = random.randint(0, 101)

        if mutateVolume < 35:
                
            alarm.volume += (mutateVolume)*random.choice([-1,1])     

        if mutateMus < 35:

            alarm.mus = this.avaibleSongs[random.randint(0,len(this.avaibleSongs) -1)]

        if mutatePuzzle < 35:

            alarm.usePuzzle = bool(random.getrandbits(1))
        

                

                

                
        

