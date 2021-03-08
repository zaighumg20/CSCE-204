#Author: Talha Gill


from datetime import time

#Add all the activities and time in reminders dictionary
reminders = {
            'Drop kids off at school':time(7,50),'Lunch with friends':time(12,30),
            'Pick up kids from school':time(15,30),'Dinner':time(20,0),
            'Read books':time(19,00),'Cricket practice':time(15,0),
            'Gym':time(18,0),'Bake food for sale':time(10,0),
            'Piano practice':time(16,0),'Bed Time':time(22,0),
            'Play games':time(21,0)
            }

#add all reminders in sorted order to today_reminders
today_reminders = dict(sorted(reminders.items(), key=lambda item: item[1]))

#count of activities start from 1
activity_number=1

#loop to iterate through today_reminders
#and store key values in activity and Time variable
for activity,Time in today_reminders.items():
    #Print each activity
    print(activity_number,'.  ',activity,' - ',Time.strftime("%I:%M %p"))
    activity_number+=1