import requests, sys, os, getopt
from datetime import time, date, datetime
from gtts import gTTS
from playsound import playsound
from googletrans import Translator

##get translator instance
translator = Translator()

##Declaring needed variables
salat_list = ["Fajr", "Dhuhr", "Asr", "Maghreb", "Isha"] 
school = 3
current_time = datetime.now().timestamp()
#current_time = 1629310000.29174 
URL = "https://api.pray.zone/v2/times/today.json"
location = "Brussels"
dest = "fr"
help_string = '\nArguments:\n -c <city> (default -> Brussels) \n -l <language> (default -> fr)\n'

##Getting all the command line arguments
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv,"hc:l:",["city=","lang="])
except getopt.GetoptError:
    print (help_string)
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print (help_string)
        sys.exit()
    elif opt in ("-c", "--city"):
        location = arg
    elif opt in ("-l", "--lang"):
        dest = arg

##Creates the request with correct url and parameters
def requestBuilder():
    PARAMS = {'city': location, 'school': school}
    r = requests.get(url = URL, params= PARAMS)
    return r

##makes the get request and returns raw json
def getJson():
    request = requestBuilder()
    data = request.json()
    return data

##Format string hours to time object
def formatTime(tempSalat):
    (hour, second) = tempSalat.split(':')
    return time(int(hour), int(second))

##Returns timestamps from given time parameter
def getTimeStamps(time):
    tod = date.today()
    today = datetime(tod.year, tod.month, tod.day, time.hour, time.minute, time.second)
    return datetime.timestamp(today)

##Uses the raw JSON to create an array of timestamps
def parseJsonToTimestampArray():
    times = getJson()["results"]["datetime"][0]["times"]
    salat_array = [times["Fajr"], times["Dhuhr"], times["Asr"], times["Maghrib"], times["Isha"]]
    time_array = []
    for sal in salat_array:
        time_array.append(getTimeStamps(formatTime(sal)))
    return time_array

##Will compare current time with the salat to show the next one
def checkTime():
    times = parseJsonToTimestampArray()
    i = 0
    while i < 5:
        if current_time < times[i]:
            return datetime.fromtimestamp(times[i]), int(i)
        else:
            i += 1
    return 0, 0

##Translates the output
def getTranslation(ins, source, dest):
    translated = translator.translate(ins,src=source ,dest=dest)
    return translated

##Plays the sound
def play(text):
    dire = "./out.mp3"
    output = getTranslation(text, "fr", dest)
	#Use the translated text to generate an mp3 file with it
    gTTS(output.text, lang=dest).save(dire)
	#Plays the mp3 file
    playsound(dire)
    return dire

##Will generate a string and play it in the STT class
def speak():
    next_salat, number = checkTime()
    text = ""
    if next_salat != 0:
        difference = next_salat - datetime.fromtimestamp(current_time)
        sec = difference.total_seconds()
        result = ""
        minutes = int(sec/60)
        rest_minutes = int(sec/60 % 60)
        hours = int(minutes/60)
        if minutes >= 60:
            result = str(hours)+ " heures et "+  str(rest_minutes) +" minutes"
        else:
            result = str(minutes) + " minutes"
        text = f"La prière de {salat_list[number]} est dans {result}"
        
    else:
        text = "Toutes les prières sont déjà passées"
    return play(text)

def main():
    try:
        os.remove(speak())
    except:
        path = "./error.mp3"
        gTTS("An error occured, check for typos in the command line arguments or try again later", lang="en").save(path)
        playsound(path)
        os.remove(path)

if __name__ == "__main__":
   main()