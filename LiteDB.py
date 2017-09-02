# coding: utf8

import pymysql
import time
import LiteConfig

class DataManager:

	def __init__(self):
		try:
			self.conn = pymysql.connect(LiteConfig.dbHost, user=LiteConfig.dbUser, passwd=LiteConfig.dbPassword, db=LiteConfig.dbName, connect_timeout=5)
			self.cursor = self.conn.cursor()
		except:
			print "r"

	def setMessageRepliedTo(self,messageID):
		try:
			req = "INSERT INTO Answered VALUES (NULL,\'"+str(messageID)+"\',\'"+time.strftime('%Y-%m-%d %H:%M:%S')+"\')"
			self.cursor.execute(req)
			self.conn.commit()
			return True
		except:
			return False

	def isMessageRepliedTo(self,messageID):
		try:
			req = "SELECT EXISTS(SELECT 1 FROM Answered WHERE post_id = \'"+str(messageID)+"\')"
			self.cursor.execute(req)
			res = self.cursor.fetchone()
			return int(res[0])
		except:
			return -1
