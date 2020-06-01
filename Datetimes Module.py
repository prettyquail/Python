>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> help(datetime.date)
Help on class date in module datetime:

class date(builtins.object)
 |  date(year, month, day) --> date object
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(...)
 |      Formats self with strftime.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __reduce__(...)
 |      __reduce__() -> (cls, state)
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  ctime(...)
 |      Return ctime() style string.
 |  
 |  isocalendar(...)
 |      Return a 3-tuple containing ISO year, week number, and weekday.
 |  
 |  isoformat(...)
 |      Return string in ISO 8601 format, YYYY-MM-DD.
 |  
 |  isoweekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 1 ... Sunday == 7
 |  
 |  replace(...)
 |      Return date with new specified fields.
 |  
 |  strftime(...)
 |      format -> strftime() style string.
 |  
 |  timetuple(...)
 |      Return time tuple, compatible with time.localtime().
 |  
 |  toordinal(...)
 |      Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.
 |  
 |  weekday(...)
 |      Return the day of the week represented by the date.
 |      Monday == 0 ... Sunday == 6
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromisocalendar(...) from builtins.type
 |      int, int, int -> Construct a date from the ISO year, week number and weekday.
 |      
 |      This is the inverse of the date.isocalendar() function
 |  
 |  fromisoformat(...) from builtins.type
 |      str -> Construct a date from the output of date.isoformat()
 |  
 |  fromordinal(...) from builtins.type
 |      int -> date corresponding to a proleptic Gregorian ordinal.
 |  
 |  fromtimestamp(timestamp, /) from builtins.type
 |      Create a date from a POSIX timestamp.
 |      
 |      The timestamp is a number, e.g. created via time.time(), that is interpreted
 |      as local time.
 |  
 |  today(...) from builtins.type
 |      Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  day
 |  
 |  month
 |  
 |  year
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  max = datetime.date(9999, 12, 31)
 |  
 |  min = datetime.date(1, 1, 1)
 |  
 |  resolution = datetime.timedelta(days=1)
 
 
 ---------------------------------------------------------------------------------------------------------------------
 ---------------------------------------------------------------------------------------------------------------------
 >>> gvr=datetime.date(1956,1,5)
>>> print(gvr)
1956-01-05
>>> print(gvr.year)
1956
>>> print(gvr.month)
1
>>> print(gvr.day)
5
>>> mill=datetime.date(2000,1,1)
>>> dt=datetime.timedelta(100)
>>> print(mill+dt)
2000-04-10
>>> print(gvr.strftime("%A,%B %d,%Y"))
Thursday,January 05,1956
>>> message="GVR was born on {:%A,%B,%d,%Y},"
>>> print(message.format(gvr))
GVR was born on Thursday,January,05,1956,
>>> launch_date=datetime.date(2017,3,30)
>>> launch_time=datetime.time(22,27,0)
>>> launch_datetime=datetime.datetime(2017,3,30,22,27,0)
>>> print(launch_date)
2017-03-30
>>> print(launch_time)
22:27:00
>>> print(launch_datetime)
2017-03-30 22:27:00
>>> now=datetime.datetime.today()
>>> print(now)
2020-06-01 12:25:11.153250

>>> moon_landing="7/20/1969"
>>> moon_landing_datetime=datetime.datetime.strptime(moon_landing,"%m/%d/%Y")
>>> print(moon_landing_datetime)
1969-07-20 00:00:00
