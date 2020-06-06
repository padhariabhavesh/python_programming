"""
@author:Bhavesh Padharia
"""

#desktop notification 


# from gi.repository import Notify
# Notify.init("App Name")
# Notify.Notification.new("Hi bhavesh").show() #input message 
#
#

from gi.repository import Notify

# One time initialization of libnotify
Notify.init("My Program Name")

# Create the notification object
summary = "Wake up!"  #input message 
body = "Meeting at 3PM!"  #input message 
notification = Notify.Notification.new(
    summary,
    body, # Optional
)

# Actually show on screen
notification.show()



