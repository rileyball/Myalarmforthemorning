'''
Title: Alarm Mark II
Author: Riley Carpenter
TODO: have the volume get louder when it goes off and quieter afterwards, if possible have it both run and end redshift when it is nightime, large text for the alarm section would be nice and also make it easier to read in the morning
'''
from pygame import mixer
import time
import os
import sys
import random
import getpass
import glob
import os
global secondtime
global seconds
global minutes
global hours
global days
global years
global decades
dir_path = os.path.dirname(os.path.realpath(__file__))
optionalsongs = (glob.glob(dir_path + "/Songs/*.wav*"))
'''
optionalsongs += (glob.glob(dir_path + "/Songs/*.mp3"))
if getpass.getuser() == "rileyball2":
    optionalsongs += (glob.glob("/home/rileyball2/Music/Pat the Bunny/SongsByJohnnyHoboAndTheFreightTrains/*.mp3")) #This just adds some music from my laptop to it so I don't have to drag a whole other folder
'''
background = (glob.glob(dir_path + "/Backgroundsounds/*.wav"))
#background += (glob.glob(dir_path + "/Backgroundsounds/*.mp3"))
if (os.path.exists(dir_path +"/Backgroundsounds")) == False:
    os.makedirs(dir_path + "/Backgroundsounds")
if (os.path.exists(dir_path +"/Songs")) == False:
    os.makedirs(dir_path + "/Songs")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#VOLUME CONTROL AREA

#VOLUME CONTROL AREA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hours3 = 5
Minutes3 = 5
endorno = ""
Currenttime = time.ctime()
Hours1 = int(Currenttime[11:13])
Minutes1 = int(Currenttime[14:16])
Seconds = int(Currenttime[17:19])
fiveminutecountdown = 300
startinghour = int(Currenttime[11:13])
soundisplaying = False
milliseconds = 0
seconds = 0
minutes = 0
hours = 0
days = 0
years = 0
decades = 0
class color: #This is for bold apparently??? IDK I found it on stack overflow
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#This is where I make the clearscreen function universal for all systems
global clearorcls
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
#This is where I make it so it's easier to tell what the time of day is
if startinghour >= 22 or startinghour <= 4:
    timeofday = "Bedtime"
elif startinghour >= 6 and startinghour <= 8:
    timeofday = "Morning"
elif startinghour >= 9 and startinghour <= 11:
    timeofday = "Day"
elif startinghour == 12:
    timeofday = "Noon"
elif startinghour >= 13 and startinghour <= 18:
    timeofday = "Afternoon"
elif startinghour >= 17 and startinghour <= 22:
    timeofday = "Night"
#The phrases that go off during the alarm? Set here
if timeofday == "Bedtime":
    phrases = ["Wake up Riley!!!!","It's time to wake up it's time to wake up","HEEEEYYY WAKE UP","RILEY RILEY RILEY WAKE UP","1 2 3 4 5 6 7 8 9 it is time to wake up","Riley more alarms are to come UNLESS you get up","OH WHEN SHALL I SEE JESUS you wanna not hear this again? Wake up","I'm so tired of telling you to wake up just wake up","A friend of the devil is somehow who doesn't wake up","Babe babe bae wake up"]
elif timeofday == "Morning":
    phrases = ["Your morning alarm is going off!!!!! I suggest you answer it!","This is your slightly later than morning alarm but still in the morning area!!!!","Good morning but like in a different way!!!!","It's time to cancel this alarm as it's going off but not in the way you wanted!!!","HELLLO TIME TO CONTINUE IN YOUR DAY"]
elif timeofday == "Day":
    phrases = ["You are usually at school like what why are you using this?","BEEEP BEEP BEEP is what a normal alarm says but I do not as I'm #NOTNORMAL","Hey user this is a really good alarm clock I wonder if their is a reason for that HMMMMMMMMMMM","OHH it's time for the ALARM GAME the goal of this game is to have your alarm go off, YOU WON!"]
elif timeofday == "Noon":
    phrases = ["You started at noon and you end here, congratulations you bastard","I don't know why I set noon as a time like you probably aren't setting it off at noon.. Unless you are"]
elif timeofday == "Afternoon":
    phrases = ["It's the afternoon!! When you have homemade snacks and nice delicious foods and your alarm goes off","Afternoon time!","ALARM ALARM ALARM IT IS IN THE AFTERNOON","Hey buddy your alarm is going off","Hey!!!! Do the thing!"]
elif timeofday == "Night":
    phrases = ["Goodnight! But like in a different way goodnight!","Hey it's the nighttime! AND your alarm is going off!! SOOO weird!!!!!!"]
if timeofday == "Night":
    soundsorno = input("Hey I saw that this is Night so I wanted to know if you want to play the city sounds? Y/N ")
else:
    soundsorno = ""
def playsound(soundfile): #This is how you play the music
    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play(-1)
def gettime(): #This gets the current time but I put this in so late I never used it lol
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
def alarmsystem(Hours2, Minutes2): #Main alarm loop
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    years = 0
    decades = 0
    global soundisplaying
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    if soundisplaying == True: #Checks if sound is playing because if it is and you stop sound it will break
        mixer.music.stop()
        soundisplaying = False
    if timeofday == "Bedtime" and background != []: #Insures that the background sound won't play if it doesn't exist
        soundisplaying = True
        playsound(random.choice(background))
    elif soundsorno == "Y" or soundsorno == "Yes" or soundsorno == "y" or soundsorno == "yes" and background != []:
        playsound(random.choice(background))
        soundisplaying = True
    while Hours1 != Hours2 or Minutes1 != Minutes2:
        os.system(clearorcls)
        if secondtime == True:
            print(fiveminutecountdown)
            fiveminutecountdown -= 1
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        Hours1 = str(Hours1)
        if Minutes1 < 10:
            Minutes1 = str("0" + str(Minutes1))
        else:
            Minutes1 = str(Minutes1)
        Hours2 = str(Hours2)
        if Minutes2 < 10:
            Minutes2 = str("0" + str(Minutes2))
        else:
            Minutes2 = str(Minutes2)
        print("\033[1m" + Hours1 + ":" + Minutes1,"is not",Hours2 + ":" + Minutes2,"therefore the alarm is not going off" + "\033[0m")
        print("")
        print("")
        print("")
        print("")
        #This is the area that controls the stopwatch that counts how long you've had the alarm on
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes +=1
        elif minutes == 60:
            minutes = 0
            hours += 1
        elif hours == 24:
            hours = 0
            days != 1
        elif days == 365:
            days = 0
            years += 1
        elif years == 10:
            years = 0
            decades += 1
        while decades >= 1:
            print("You've been running this alarm for a straight decade??? HOw???")
        if years == 1:
            year = "year"
        else:
            year = "years"
        if days == 1:
            day = "day"
        else:
            day = "days"
        if hours == 1:
            hour = "hour"
        else:
            hour = "hours"
        if minutes == 1:
            minute = "minute"
        else:
            minute = "minutes"
        if seconds == 1:
            second = "second"
        else:
            second = "seconds"
        if milliseconds == 1:
            millisecond = "millisecond"
        else:
            millisecond = "milliseconds"
        if years >= 1:
            fulltime = ["The amount of time that has passed is",years,year,hours,hour,minutes,minute,seconds,second]
        elif days >= 1:
            fulltime = ["The amount of time that has passed is",days,day,hours,hour,minutes,minute,seconds,second]
        elif hours >= 1:
            fulltime = ["The amount of time that has passed is",hours,hour,minutes,minute,seconds,second]
        elif minutes >= 1:
            fulltime = ["The amount of time that has passed is",minutes,minute,seconds,second]
        else:
            fulltime = ["The amount of time that has passed is",seconds,second]
        print(*fulltime,sep = " ")
        #End of that area that does the stopwatch
        Hours1 = int(Hours1)
        Minutes1 = int(Minutes1) #Reset everything to integer from string
        Hours2 = int(Hours2)
        Minutes2 = int(Minutes2)
        time.sleep(1)
    else:
        os.system(clearorcls)
        if soundisplaying == True:
            mixer.music.stop()
        print(random.choice(phrases))
        if optionalsongs != []:
            soundisplaying = True
            musictoplay = random.choice(optionalsongs)
            playsound(musictoplay)
        endorno = input("Press enter to stop the music and snooze for 5 minutes or type stop ")
        if endorno == "stop":
            if getpass.getuser() == "rileyball2": #My user account, this is so I can set my own nicknames here, if you want to you can modify this
                name2 = ["Riles","Riley Carpenter","Riley Mitchel Carpenter","Rileybug","Rileyball","Rile","Michelle","Riley Michelle Carpenter","Diane","Comrade","Conrad","my really cool nonbinary pal"] #Bunch of nickity names for me
                name = random.choice(name2)
            else:
                name = getpass.getuser()
            if timeofday == "Bedtime":
                print("Good morning",name)
            elif timeofday == "Day":
                print("Goodbye and semi-Good morning",name)
            elif timeofday == "Noon":
                print("Good probably not noon anymore but was noon",name)
            elif timeofday == "Afternoon":
                print("Good afternoon",name)
            elif timeofday == "Night":
                print("Goodbye and semi-good night",name)
            else:
                print("Goodbye",name)
            time.sleep(1)
            sys.exit()
def nexttime():
    secondtime = True
    fiveminutecountdown = 300
    Currenttime = time.ctime()
    Hours1 = int(Currenttime[11:13])
    Minutes1 = int(Currenttime[14:16])
    Seconds = int(Currenttime[17:19])
    if Minutes1 >= 55:
        print("The alarm will go off at",Hours1 + 1,":",00)
        Hours3 = Hours1 + 1
        Minutes3 = 0
        alarmsystem(Hours3,Minutes3)
    elif Minutes1 == 10:
        print("The alarm will go off at",Hours1,":",15)
        Hours3 = Hours1
        Minutes3 = 15
        alarmsystem(Hours3,Minutes3)
    else:
        Currenttime = time.ctime()
        Hours1 = int(Currenttime[11:13])
        Minutes1 = int(Currenttime[14:16])
        Seconds = int(Currenttime[17:19])
        if Minutes1 >= 50:
            checkminutes = Minutes1 - 50
        elif Minutes1 >= 40:
            checkminutes = Minutes1 - 40
        elif Minutes1 >= 30:
            checkminutes = Minutes1 - 30
        elif Minutes1 >= 20:
            checkminutes = Minutes1 - 20
        elif Minutes1 >= 10:
            checkminutes = Minutes1 - 10
        else:
            checkminutes = Minutes1
        for i in range(0,10):
            if i < 5 and i == checkminutes:
                timetogo = 5 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i == 5 and i == checkminutes:
                timetogo = 5
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
            elif i > 5 and i == checkminutes:
                timetogo = 10 - i
                Minutes1 = int(Minutes1)
                print("The alarm will go off at",Hours1,":",Minutes1 + timetogo)
                Hours3 = Hours1
                Minutes3 = Minutes1 + timetogo
                alarmsystem(Hours3,Minutes3)
secondtime = False
hoursandminutes = input("What time do you want to get up (type like this: 22:14) ")
if hoursandminutes[1] != ":":
    firsthour = int(hoursandminutes[0:2])
else:
    firsthour = int(hoursandminutes[0])
if hoursandminutes[1] != ":":
    firstandhalfsecondminute = (hoursandminutes[3:5])
else:
    firstandhalfsecondminute = (hoursandminutes[2:4])
if len(firstandhalfsecondminute) != 2:
    firstminute = int(firstandhalfsecondminute)
else:
    firstminute = int(firstandhalfsecondminute)
alarmsystem(firsthour,firstminute)
while 1 == 1:
    nexttime()
