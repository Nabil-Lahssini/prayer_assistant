# prayer_tool
The prayer_tool is an open-source library based on prayertimes.date API. [Check their API here](https://prayertimes.date/api)
It provides you a complete library to get the prayer times for the day or the whole month.

## How to get it ?
The prayer_tool is a python package that you can simply install using the following command
```
pip install prayer-tool
```
## How to use it ?
To use our library in your code, you need to import it and intialize it, that's all. It's easy !
```
from prayer_tool import prayer_times

## Intialize an instance of it
instance = prayer_times.PrayerTimes(city="Brussels", school=3, juristic=0)

## Get today's prayer's
today = instance.get_date()

# EXAMPLES
print(f"{today.fajr.name} : {today.fajr.time}")
# fajr : 04:42:00

print(f"{today.dhor.name} : {today.dhor.time}")
# dhor : 13:46:00
```
## Advanced requests
### Precise day
You can also get the schedule for a precise day.
Code example:
```
from prayer_tool import prayer_times
import datetime

#Declaring an instance
instance = prayer_times.PrayerTimes()

#The datetime object we need
date = datetime.datetime(year = 2021, month = 8, day = 23)

#Call the function and save the result
result = instance.get_date(date)

print(result.__str__())

##output:
Date : 2021-08-23 00:00:00 
fajr : 04:32:00
dhor : 13:45:00
asr : 17:37:00
maghreb : 20:48:00
icha : 22:48:00
```
### Date interval
You are also able to ask for the schedule in a date interval.
Code example:
```
from prayer_tool import prayer_times
import datetime

#Declaring an instance
instance = prayer_times.PrayerTimes(city="Paris")

#The datetime objects we need
start = datetime.datetime(year = 2021, month = 8, day = 23)
end = datetime.datetime(year = 2021, month = 8, day = 26)

#Call the function and save the result
result = instance.get_date(start, end)

for item in result:
    print(item.__str__() + "\n")

##output:
Date : 2021-08-23 00:00:00 
fajr : 04:32:00
dhor : 13:45:00
asr : 17:37:00
maghreb : 20:48:00
icha : 22:48:00

Date : 2021-08-24 00:00:00
fajr : 04:35:00
dhor : 13:45:00
asr : 17:36:00
maghreb : 20:46:00
icha : 22:45:00
...
```

## Customize the result
The prayers differ from city to city, school to school and so one. That's why the API lets you chose your preferences.
Here are the options:
```
SCHOOL : 
Id	Name	
0	Ithna Ashari
1	University of Islamic Sciences, Karachi	
2	Islamic Society of North America
3	Muslim World League (default)
4	Umm Al-Qura University, Mecca
5	Egyptian General Authority of Survey
7	Institute of Geophysics, University of Tehran
8	Morocco
9	Department of Islamic Advancement, Malaysia (JAKIM)	
10	Majlis Ugama Islam Singapura
11	Union des Organisations Islamiques de France
12	Turkey
```
```
JURISTIC :
Id	Juristic
0	Shafii (default)
1	Hanafi
```

## Extra
A voice assistant is also available for the more enthusiast programmers ! It tells you when the next prayer will occur.
You can use it by simply typing this command:
```
python -m prayer_tool -c <city> -l <language>
```
EXAMPLE for an arabic voice output for the next prayer in london.
```
python -m prayer_tool -c London -l ar
```