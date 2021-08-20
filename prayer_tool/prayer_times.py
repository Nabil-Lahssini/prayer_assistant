from datetime import time, date
import requests

from prayer import Prayer


##Declaring needed variables
URL_TODAY = "https://api.pray.zone/v2/times/today.json"
URL_THIS_MONTH = "https://api.pray.zone/v2/times/this_month.json"





def request_builder(city, school, juristic, timeformat, URL):
    """Creates the request with correct url and parameters"""
    params = {'city': city, 'school': school, 'juristic':juristic, 'timeformat': timeformat}
    request = requests.get(url = URL, params=params)
    return request

def format_time(temp_salat):
    """Format string hours to time object"""
    (hour, minut) = temp_salat.split(':')
    return time(int(hour), int(minut))

def get_today_prayer(request):
    """Returns today prayer"""
    data = request.json()
    times = data["results"]["datetime"][0]["times"]
    return parse_day_prayer(times)

def parse_day_prayer(day_object):
    prayer = Prayer(format_time(day_object["Fajr"]), format_time(day_object["Dhuhr"]), 
        format_time(day_object["Asr"]), format_time(day_object["Maghrib"]), 
        format_time(day_object["Isha"]), date.today())
    return prayer

def get_month_prayer(request):
    month_list = []
    data = request.json()
    month = data["results"]["datetime"]
    for day in month:
        month_list.append(parse_day_prayer(day["times"]))
    return month_list

class Instance:
    def __init__(self,CITY="Brussels", SCHOOL=3, JURISTIC=0, TIMEFORMAT=0):
        self.CITY = CITY
        self.SCHOOL = SCHOOL
        self.JURISTIC = JURISTIC
        self.TIMEFORMAT = TIMEFORMAT
        
    def today(self):
        request = request_builder(self.CITY, self.SCHOOL, self.JURISTIC, self.TIMEFORMAT, URL_TODAY)
        return get_today_prayer(request)

    def this_month(self):
        request = request_builder(self.CITY, self.SCHOOL, self.JURISTIC, self.TIMEFORMAT, URL_THIS_MONTH)
        return get_month_prayer(request)


ins = Instance()
month = ins.this_month()
print(month[0].show())