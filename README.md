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
import prayer_tool

## Intialize an instance of it
instance = prayer_tool.Prayer_times(CITY="Brussels", SCHOOL=3, JURISTIC=0)

## Get today's prayer's
today = instance.today()

# EXAMPLES
print(f"{today.fajr.name} : {today.fajr.time}")
# fajr : 04:42:00

print(f"{today.dhor.name} : {today.dhor.time}")
# dhor : 13:46:00
```

You can also get the schedule for the whole month
```
import prayer_tool

## Intialize an instance of it
instance = prayer_tool.Prayer_times(CITY="Brussels", SCHOOL=3, JURISTIC=0)

## returns an array of the daily prayer
this_month = instance.this_month()

## usage example
for day in this_month:
    print(f"{today.fajr.name} : {today.fajr.time}")

# 03:25:00
# 03:29:00
# 03:33:00
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