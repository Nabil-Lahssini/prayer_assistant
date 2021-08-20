from datetime import time
import requests
from datetime import datetime
from prayer import Prayer
from day import Day


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
    salat = time(hour=int(hour), minute=int(minut))
    return salat

def get_today_prayer(request):
    """Returns today prayer"""
    data = request.json()
    times = data["results"]["datetime"][0]["times"]
    dates = data["results"]["datetime"][0]["date"]["gregorian"]
    return parse_day_prayer(times, dates)

def string_to_date(date_str):
    """Parse date string in date object"""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj

def parse_day_prayer(day_object, dates):
    day_date = string_to_date(dates)
    prayer = Day(format_time(day_object["Fajr"]), format_time(day_object["Dhuhr"]), 
        format_time(day_object["Asr"]), format_time(day_object["Maghrib"]), 
        format_time(day_object["Isha"]), day_date)
    return prayer

def get_month_prayer(request):
    month_list = []
    data = request.json()
    month = data["results"]["datetime"]
    for day in month:
        month_list.append(parse_day_prayer(day["times"], day["date"]["gregorian"]))
    return month_list

class Prayer_times:
    """Prayer times API implementation class

    You have to create an instance of Prayer_times to use this API

    :param CITY: The city from where you need the calendar.
                         For example ``Brussels``
    :type service_urls: string

    :param SCHOOL: Every school have a different calculation, we use 3 by default (Muslim World League).
                         For example 3
    :type SCHOOL: int

    :param JURISTIC: 0 for Shafii (or the standard way), 1 for Hanafi. If you leave this empty, it defaults to Shafii.
                         For example 0
    :type JURISTIC: int
    """
    def __init__(self,CITY="Brussels", SCHOOL=3, JURISTIC=0):
        self.CITY = CITY
        self.SCHOOL = SCHOOL
        self.JURISTIC = JURISTIC
        self.TIMEFORMAT = 0
        
    def today(self):
        request = request_builder(self.CITY, self.SCHOOL, self.JURISTIC, self.TIMEFORMAT, URL_TODAY)
        return get_today_prayer(request)

    def this_month(self):
        request = request_builder(self.CITY, self.SCHOOL, self.JURISTIC, self.TIMEFORMAT, URL_THIS_MONTH)
        return get_month_prayer(request)

