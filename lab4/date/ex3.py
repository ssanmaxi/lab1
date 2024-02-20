from datetime import datetime, timedelta
a = datetime.now()
a = a.replace(microsecond=0)
print(a)
