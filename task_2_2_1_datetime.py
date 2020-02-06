import datetime

input_date = (int(i) for i in input().split())
my_date = datetime.date(*input_date)
days = datetime.timedelta(int(input()))

result = my_date + days

print(result.year, result.month, result.day, sep=' ')
