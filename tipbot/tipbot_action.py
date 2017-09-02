import praw

# Variables
help_subject = "Help Message"
help_message = "Hello, to send Litecoin ..."

def send_help(reddit_instance, recipient):
		print "> Sending Help Message"
		reddit_instance.redditor(recipient).message(help_subject, help_message)

#def send_info():

#def register():

#def send_tip():

#def withdraw():