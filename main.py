import praw
import yaml

import LiteDB
import tipbot_action

db = LiteDB.DataManager()

class TipBot(object):
	
	def __init__(self):
		ymlfile = open('config/config.yml', 'r')
		cfg = yaml.load(ymlfile)
		self.username = cfg['reddit']['username']
		self.password = cfg['reddit']['password']
		self.client_id = cfg['reddit']['client_id']
		self.client_secret = cfg['reddit']['client_secret']
		self.user_agent = cfg['reddit']['user_agent']
		self.command_list = cfg['command_list']

	def login(self):
		self.reddit = praw.Reddit(client_id = self.client_id,
			client_secret = self.client_secret,
			user_agent = self.user_agent,
			username = self.username,
			password = self.password)
	
	# Parse inbox messages
	def parse_message(self, message):
		split_message = message.body.split(" ")
		
		if not split_message[0].lower() == '/u/' + self.username.lower():
			print "> ERROR - Wrong username ??? "  ### Log and return 0
		else:
			if split_message[1] not in self.command_list:
				print "> WARNING - Wrong command" ### Log and return 0
			else:
				if split_message[1] == '!help' or split_message[1] == '!info':
					print "> Help requested"
					
					if not db.is_message_replied_to(message.id):
						if(db.set_message_replied_to(message.id)):
							send_help(str(message.author))

	#TODO: Parse comments from threads
	def parse_comment(self, comment):
		print 'parsing comment:' + comment

	def check_inbox(self):
		# try to fetch some messages
		messages = list(self.reddit.inbox.all(limit=None))
		messages.reverse()

		# process messages
		for m in messages:
			# Sometimes messages don't have an author
			if not m.author:
				m.mark_read()
				continue
			# TODO: Ignore duplicate messages
			# if m.id == an id that is already in db
				# m.mark_read()
				# continue
			# Ignore self messages
			if m.author and m.author.name.lower() == '/u/' + self.username.lower():
				m.mark_read()
				continue

			action = None
			if m.was_comment:
				# TODO: Attempt to evaluate as comment / mention
				action = self.parse_comment(m)
			else:
				# Attempt to evaluate as inbox message
				action = self.parse_message(m)

			# Perform action, if found
			if action:
				action.do()

			m.mark_read()
	
	def main(self):
		self.login()
		# Once the bot is set up on a server we can set a loop
		# To call 'check_inbox()' every 30 secs
		self.check_inbox()

ltc_tip_bot = TipBot()
ltc_tip_bot.main()