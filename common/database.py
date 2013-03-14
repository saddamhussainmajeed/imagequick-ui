from common.pymongo import MongoClient
connection = MongoClient()
db = connection.imagequick_dev

def connect(host,port):
	global connection,db
	connection = MongoClient(host=host,port=port)
	db = connection.imagequick_dev
