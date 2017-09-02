# coding: utf8

import time
import pymysql
import yaml

class DataManager:

	def __init__(self):
		ymlfile = open('config/config.yml', 'r')
		cfg = yaml.load(ymlfile)
		self.host = cfg['mysql']['dbHost']
		self.user = cfg['mysql']['dbUser']
		self.password = cfg['mysql']['dbPassword']
		self.db_name = cfg['mysql']['dbName']

		try:
			self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db=self.db_name, connect_timeout=5)
			self.cursor = self.conn.cursor()
		except:
			print("r")

	def set_message_replied_to(self,messageID):
		try:
			req = "INSERT INTO Answered VALUES (NULL,\'"+str(messageID)+"\',\'"+time.strftime('%Y-%m-%d %H:%M:%S')+"\')"
			self.cursor.execute(req)
			self.conn.commit()
			return True
		except:
			return False

	def is_message_replied_to(self,messageID):
		try:
			req = "SELECT EXISTS(SELECT 1 FROM Answered WHERE post_id = \'"+str(messageID)+"\')"
			self.cursor.execute(req)
			res = self.cursor.fetchone()
			return int(res[0])
		except:
			return -1
