import alarms
import datetime
import manager
import keyboard
import pickle

try:
    mngr = pickle.load(open('manager_data.pkl', 'rb'))
except FileNotFoundException:
    print("Alarms file not found. Please run editRun.py to create it. Type anything to exit.")
    input()
    raise SystemExit
except Exception as excp:
    print("Error loading alarms file. Type anything to exit")
    print("DEBUG: " + str(excp))
    input()
    raise SystemExit
while True:
    mngr = pickle.load(open('manager_data.pkl', 'rb'))
    for i , a in enumerate(mngr.alarms):
                    if a.activate:
                        if a.repeat:              
                            if a.dateTime.minute + (a.dateTime.hour*60) == datetime.datetime.now().minute + (datetime.datetime.now().hour*60):
                                print("Alarm " + a.name + " triggered: Press (a) to stop it." )
                                mngr.trigger(i)
                                while True:
                                    if keyboard.is_pressed('a'):
                                        mngr.stop()
                                        
                                
                        elif a.dateTime.date() == datetime.datetime.now().date() and a.dateTime.minute + a.dateTime.hour*60 == datetime.datetime.now().minute + datetime.datetime.now().hour*60:
                                mngr.trigger(i)
                                print("Alarm " + a.name + " triggered: Press (a) to stop it." )
                                while True:
                                    if keyboard.is_pressed('a'):
                                        mngr.stop()
                                    
