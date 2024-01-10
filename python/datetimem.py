import datetime as dt
#from requests import request



#sanani ko'rish
today = dt.date.today()
print(today)

#vaqtni ko'rsatish
now = dt.datetime.now()
print(now)


#soatni ko'rsatish
hour1 = dt.datetime.now()
print(hour1.time())


#ertangi vaqtni saqlash
bugun = dt.datetime.now()
ertaga = dt.date(2023, 12, 1)
print(ertaga)


#sanalar orasida farq 
bugun = dt.date.today()
contest = dt.date(2023, 12, 25)
farq = contest - bugun
print(farq)