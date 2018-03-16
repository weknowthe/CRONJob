# pip install pyfcm, pytz

import pytz 
import urllib2
import calendar
from datetime import date
from random import randint
from datetime import datetime
from pyfcm import FCMNotification

tz  = pytz.timezone('Asia/Calcutta')
utc = datetime.utcnow() 
utc = pytz.utc.localize(utc, is_dst=None).astimezone(tz)
time =  utc.strftime("%H") # gmt/utc time
text = ""
textaum = ""

trigger_hours = ["00","01","02","03","04","05","06","07","12","09","08","11","13","15","18","19","20", "21","23","10","14","16",]
print (time)
print ("condition: " + str(time in trigger_hours))

if time in trigger_hours:
	my_date = date.today()
	folder  = calendar.day_name[my_date.weekday()][:3]
	random  = randint(1, 5)
		
	textbaseaum = "https://firebasestorage.googleapis.com/v0/b/aum-flashlight.appspot.com/o/AUM%2F"+str(random)+".txt?alt=media"
	imgurl   = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fimg%2F"+str(random)+".jpg?alt=media"
	textbase = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fmantra%2F"+str(random)+".txt?alt=media"
	try:
		for line in urllib2.urlopen(textbase):
			text += line
	except:
		print("invalid MR text url")
		quit()
	try:
		for line in urllib2.urlopen(textbaseaum):
				textaum += line
	except:
		print("invalid AUM text url")
		quit()

	try:
		urllib2.urlopen(imgurl)
	except:
		try:
			print("trying png")
			imgurl  = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fimg%2F"+str(random)+".png?alt=media"
			urllib2.urlopen(imgurl)
		except:
			try:
				print("trying jpeg")
				imgurl  = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fimg%2F"+str(random)+".jpeg?alt=media"
				urllib2.urlopen(imgurl)
			except:
				quit()

	data_message = {
		"message": text,
		"imageLink": imgurl
	}

	aum_data_message = {
		"message": textaum
	}

	message_title = "Today's Mantra..."

	push_service = FCMNotification(api_key="AAAAgJxP-K4:APA91bHO-ZG61ElfY5WSGtoBS8kNtNYpxfA2HIYIbWt4prC_QJJU40ouX0PypDKt_WDBUzEQGl85f5wjICOBCxFYcOxwKP37J7Xoduayw2ES7jo8WSLw1V-7zcC9UXjk8R1wP10n2KES")

	aum_push_service = FCMNotification(api_key="AAAAhwA8p_4:APA91bHZBZ6pUudRD3XjIXIB_TrXMHLZRn7uADWyYxufc9aDAZpzlqcq5jNHSJmHfVkkxih-1DMyDVMO75NM_PwwzbP0lu7Tq49vXFIDXFj8vEIdvGURU0u9-LuDZ5Rd5iKWqJzz9lmZ")

	topic_condition = "('PushTest' in topics )"
	aum_topic_condition = "('AUM' in topics )"

	#aum_result = aum_push_service.notify_topic_subscribers(message_body='', data_message=aum_data_message, condition=aum_topic_condition)
	result = push_service.notify_topic_subscribers(message_body='', data_message=data_message, condition=topic_condition)

	print(result)
	#print(aum_result)
