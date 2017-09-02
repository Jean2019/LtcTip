# coding: utf8
import praw
import pdb
import re
import os

###### DON'T FORGET TO ADD YOUR CREDENTIALS ########

reddit = praw.Reddit(client_id='',
	client_secret='',
	password='',
	username='',
	user_agent='Reddit Bot 1.0')

if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('test') ## Subreddit

for submission in subreddit.hot(limit=2):
	print("--- "+submission.title)
	post = reddit.submission(id=submission.id)

	post.comments.replace_more(limit=0)
	for comment in post.comments.list():
		print("    +++ "+comment.body)

		if(comment.body == "so you are top"): ## Trigger word
			if comment.id not in posts_replied_to:
				comment.reply("Final test")
				posts_replied_to.append(comment.id)

with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")
