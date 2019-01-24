from datetime import datetime


time = "12 Oct 2016 23:59:59"


datetime_object = datetime.strptime(time, '%d %b %Y %H:%M:%S')
print(datetime_object)
