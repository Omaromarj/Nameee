from datetime import date, datetime
import requests
import random

def clock():
    hours = datetime.now().hour
    min = datetime.now().minute


def Today():
    dare = str(date.today()).split('-')
    year1 = int(dare[0])
    month1 = int(dare[1])
    day1 = int(dare[2])
    return [date(year1, month1, day1), str(year1)+"?"+str(month1)+"?"+str(day1)]

def numOfDays(date1, date2):
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days
def reat():
    pass
    #return open('data.txt','r').read()
def rite(text):
    pass
    #open('data.txt', 'w').write(text)

def sendmsg(text):
    token = '6927669748:AAG_MR1hu94BVNr7qlVLJiFCmiUz4QuUaTc'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parms = {'chat_id': '1424751796', 'text': text}
    print(requests.post(url, data=parms).text)
    
def main():
    a=input("you failed ?")
    if a == "yes":
        a = True
        last_nut = Today()
        print("...")
    else:
        a = False
        #last = reat().splitlines()[1].split("?")
        daay = 16
        moonth = 12
        yeaar = 2024
        print(last)
        last_nut = [date(yeaar, moonth, daay), str(yeaar)+"?"+str(moonth)+"?"+str(daay)]
        
    the_between = numOfDays(last_nut[0], Today()[0])
    daytext = f"{the_between}"
    else:
        msg = [f'keep it up {daytext} days 💪🏿!', f"يا بطل يا بطل استمرر {daytext} يوم 😍"]
        msg = random.choice(msg) 
        #rite(daytext+"+\n"+last_nut[1])
        sendmsg(msg)
        
        
        #print(the_between)
main()
