import pymongo
from pymongo import MongoClient

from twilio.rest import Client

account_sid = "AC119d94b6eacc964688650e234128de36"
auth_token = "4e404ebd0a7668e79f660cc42e066a80"
client = Client(account_sid, auth_token)

def msgpy(event=None,context=None):
	# get day and month 
  from datetime import datetime
  currentDay = datetime.now().day
  currentMonth = datetime.now().month

  # conversion of day and month
  month='%02d' % currentMonth
  day='%02d' % currentDay

  # connect with database
  clientdb = MongoClient('mongodb+srv://real:real9876@cluster1.69dsb.mongodb.net/realproject?retryWrites=true&w=majority')

  mydb = clientdb["realproject"]
  mycol = mydb["details"]

  # retrive and check data
  ar=[]
  for x in mycol.find():
    ar.append(list(x.values()))  


  for i in ar:
	   tim=i[2].split('-')	
	   if tim[1]==month and tim[2]==day:
		    nm = i[0]
  
  message = client.messages.create(
                                body=f"Happy Birthday {nm}",
                                from_='whatsapp:+14155238886',
                                to='whatsapp:+917200023073'
                           )