date1 = list(map(int,input().split()))
date2 = list(map(int,input().split()))
month = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31,
         6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31,
         11 : 30, 12 : 31}
years = date2[0] - date1[0]
days = 0
sec = 0
days += years*365
if date1[1] < date2[1]:
    for i in range (date1[1],date2[1]):
        days += month[i]
else:
    for i in range (date2[1],date1[1]):
        days -= month[i]
days -= date1[2]
flag_full_day = True
for i in range (3,6):
    if date1[i] > date2[i]:
        flag_full_day = False
        break
if flag_full_day:
    days += date2[2]
    sec = (date2[3]-date1[3])*3600 + (date2[4]-date1[4]) * 60 + (date2[5]-date1[5])
else:
    days += date2[2]-1
    sec = 24 * 3600 - (date1[3]*3600 + date1[4] * 60 + date1[5]) + (date2[3]*3600 + date2[4] * 60 + date2[5])

print(days,sec)
