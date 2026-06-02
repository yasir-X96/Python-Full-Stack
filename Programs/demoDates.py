from datetime import date, datetime

# today=date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday())# 0=monday

#create a specific date
# release_date=date(2026,10,25)
# print(release_date)

#current time and date
# now=datetime.now()
# print(now) # 25/05/2026----2026-05-25

# now =datetime(2026,5,25,21,30,40,12345)

# #strftime()
# print(now.strftime("%d/%m/%y"))
# print(now.strftime("%d/%m/%y"))

employees = {
     101:{"name":"samhita","Doj":"2018-06-14"},
    102: {"name": "shashank", "Doj": "2019-06-14"},
    103: {"name": "Bharat", "Doj": "2026-04-14"}
 }

emp_id=int(input("Enter the Id::"))

employee=employees[emp_id]

joining_date=datetime.strptime(employee["Doj"],"%Y-%m-%d")

today=datetime.today()
experience= today.year - joining_date.year

if(today.month,today.day)<(joining_date.month,joining_date.day):
    experience=experience-1

print(f"experience is::{experience}")

#age calculator