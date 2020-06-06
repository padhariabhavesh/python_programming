# from gi.repository import Notify
# Notify.init("App Name")
# Notify.Notification.new("Hi bhavesh").show()
#
#

from gi.repository import Notify

# One time initialization of libnotify
Notify.init("My Program Name")

# Create the notification object
summary = "Wake up!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    summary,
    body, # Optional
)

# Actually show on screen
notification.show()



