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
trigger_hours = ["08", "11" , "13", "15", "18", "19", "20", "21"]
print (time)
print ("condition: " + str(time in trigger_hours))
if time in trigger_hours:
        my_date  = date.today()
        folder   = calendar.day_name[my_date.weekday()][:3]
        random   = randint(1, 5)
        textbase = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fmantra%2F"+str(random)+".txt?alt=media"
        imgurl   = "https://firebasestorage.googleapis.com/v0/b/mantrarepeater.appspot.com/o/images%2F"+folder.lower()+"%2Fimg%2F"+str(random)+".jpg?alt=media"
        try:
                for line in urllib2.urlopen(textbase):
                        text += line
        except:
                print("invalid text url")
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
        message_title = "Today's Mantra..."
        push_service = FCMNotification(api_key="AAAAgJxP-K4:APA91bHO-ZG61ElfY5WSGtoBS8kNtNYpxfA2HIYIbWt4prC_QJJU40ouX0PypDKt_WDBUzEQGl85f5wjICOBCxFYcOxwKP37J7Xoduayw2ES7jo8WSLw1V-7zcC9UXjk8R1wP10n2KES")
        topic_condition = "('imageSupport' in topics )"
        result = push_service.notify_topic_subscribers(message_body='', data_message=data_message, condition=topic_condition)
        print(result)
