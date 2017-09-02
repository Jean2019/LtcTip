# coding: utf8

import praw
import pdb
import re
import os

import LiteDB
import LiteConfig

DataManager = LiteDB.DataManager()

reddit = praw.Reddit(client_id=LiteConfig.rClient_id,
	client_secret=LiteConfig.rClient_secret,
	password=LiteConfig.rPassword,
	username=LiteConfig.rUsername,
	user_agent=LiteConfig.rUser_agent)


def sendHelp(recipient):
	print "> Sending Help Message"
	reddit.redditor(recipient).message(LiteConfig.helpSubject, LiteConfig.helpMessage)

def parseMessage(message):
	splitMessage = message.body.split(" ")

	if not splitMessage[0] == LiteConfig.botUsername:
		print "> ERROR - Wrong username ??? "  ### Log and return 0
	else:
		if splitMessage[1] not in LiteConfig.commandList:
			print "> WARNING - Wrong command " ### Log and return 0
		else:
			if splitMessage[1] == '!help' or splitMessage[1] == '!info':
				print "> Help requested"
				if not DataManager.isMessageRepliedTo(message.id):
					if(DataManager.setMessageRepliedTo(message.id)):
						sendHelp(str(message.author))


for item in reddit.inbox.mentions(limit=None):
	try:
		message = reddit.comment(item.id)
		print message.body
		parseMessage(message)
	except:
		pass

