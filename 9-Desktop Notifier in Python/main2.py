import time
import notify2
from topnews import top_stories

# path to notification window icon
ICON_PATH = "put full path to icon image here"

# fetch news items
news_items = top_stories()

# initialise the d-bus connection
notify2.init("News Notifier")

# create Notification object
n = notify2.Notification(None, icon = ICON_PATH)

# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# set timeout for a notification
n.set_timeout(10000)

for news_item in news_items:

	# update notification data for Notification object
	n.update(news_item['title'], news_item['description'])

	# show notification on screen
	n.show()

	# short delay between notifications
	time.sleep(15)
