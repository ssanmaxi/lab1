from datetime import datetime, timedelta
a = datetime(2023, 1, 1, 12, 0, 0)
b = datetime(2023, 1, 2, 15, 30, 0)
td = b - a
diff = td.total_seconds()
print(diff)
