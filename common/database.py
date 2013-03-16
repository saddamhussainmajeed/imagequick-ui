from common.pymongo import MongoClient
from subprocess import call
import datetime
import os

connection = MongoClient()
db = connection.imagequick_dev

def connect(host,port):
	global connection,db
	connection = MongoClient(host=host,port=port)
	db = connection.imagequick_dev

def backup(collection):
	back_directory = 'files/backups/db_'+ datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
	cmd_backup = ['mongodump','-h',connection.host,'-d','imagequick_dev','-c',collection,'-o',back_directory]
	call(cmd_backup)

