import alarms
import datetime
import manager
import pickle
try:
    with open('manager_data.pkl', 'rb') as manager_file:
        mngr = pickle.load(manager_file)
except FileNotFoundError:
        mngr = manager.manager()
except Exception:
        print("WARNING: Alarm file impossible to load.")
        mngr = manager.manager()
print("Program Test")
while True:
    
    command = input()
    
    if len(command) == 0:
        print('')
        
    elif command == "help":
        print("Commands:\nadd <name> <hour:minute> <repeat (Y/N)> <year/month/day> <songFile> \nlist {alarmNumber} \nedit <index> <atrib> <value>\nrem <index>")
    elif command.split()[0] == "add":
        try:
            clName = command.split()[1]
            clHour = command.split()[2].split(':')[0]
            clMinute = command.split()[2].split(':')[1]
            if command.split()[3] == 'Y':
                clRep = True
            elif command.split()[3] == 'N':
                clRep = False
            else:
                raise Exception("Invalid character(s) on Y/N")
            
            clYr = int(command.split()[4].split(r'/')[0])
            clMth = int(command.split()[4].split(r'/')[1])
            clDay = int(command.split()[4].split(r'/')[2])
            clSong = command.split()[5]
            clDt = datetime.datetime(clYr, clMth, clDay) + datetime.timedelta(hours = int(clHour), minutes = int(clMinute))
            clAlarm = alarms.alarm(clName, clDt, clRep, clSong, True, True)
            mngr.add_alarm(clAlarm)
            with open('manager_data.pkl', 'wb') as manager_file:
                pickle.dump(mngr, manager_file)
        except Exception as excp:
            print("Wrong usage of command: use like this:\nadd <name> <hour:minute> <repeat (Y or N)> <year/month/day> <songFile>")
            print("DEBUG: " + str(excp))

            
    elif command.split()[0] == "list" and len(command.split()) == 1:
        
        
        for i , alm in enumerate(mngr.alarms):
            print(str(i + 1) + '-' + alm.name)
        
    elif command.split()[0] == "list":
        
        try:
            mngr.alarms[int(command.split()[1]) - 1].list()
        except IndexError as excp:
            print('Invalid alarm number. Use the command "list" to get alarms')
        except Exception as excp:
            print('Wrong usage of command: use like this: list {alarmNumber}')
            print('DEBUG: ' + str(excp))
            
    elif command.split()[0] == "rem":

        try:
            mngr.remove_alarm(int(command.split()[1]) - 1)
            with open('manager_data.pkl', 'wb') as manager_file:
                pickle.dump(mngr, manager_file)
        except IndexError as excp:
            print('Invalid alarm number. Use the command "list" to get alarms')
        except Exception as excp:
            print('Wrong usage of command: use like this: rem {alarmNumber}')
            print('DEBUG: ' + str(excp))
            
    elif command.split()[0] == "edit":

        try:
            if command.split()[2] == "name":
                mngr.alarms[int(command.split()[1]) - 1].name = command.split()[3]
            elif command.split()[2] == "time":
                mngr.alarms[int(command.split()[1]) - 1].dateTime = mngr.alarms[int(command.split()[1]) - 1].dateTime.replace(hour = int(command.split()[3].split(':')[0]), minute = int(command.split()[3].split(':')[1]))
            elif command.split()[2] == "date":
                mngr.alarms[int(command.split()[1]) - 1].dateTime = mngr.alarms[int(command.split()[1]) - 1].dateTime.replace(year = int(command.split()[3].split(':')[0]), month = int(command.split()[3].split(':')[1]), day = int(command.split()[3].split(':')[2]))
            elif command.split()[2] == "repeat":
                mngr.alarms[int(command.split()[1]) - 1].repeat = not mngr.alarms[int(command.split()[1]) - 1].repeat
            elif command.split()[2] == "song":
                mngr.alarms[int(command.split()[1]) - 1].mus = command.split()[3]
            with open('manager_data.pkl', 'wb') as manager_file:
                pickle.dump(mngr, manager_file)
        except IndexError as excp:
            print('Invalid alarm number. Use the command "list" to get alarms')
            print('DEBUG: ' + str(excp))
        except Exception as excp:
            print('Wrong usage of command: use like this: edit <alarmNumber> <atrib> <value>')
            print('DEBUG: ' + str(excp))
    

                        
                        
                    
                
                    
            
