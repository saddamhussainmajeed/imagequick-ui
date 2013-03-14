from common import database
import datetime

def get_voice_list():
	voicelist = []
	for voice in database.db.voices.find():
		voicelist.append(voice['name'])
	return voicelist

def get_template_list():
	
	templatelist = []
	for template in database.db.events.find():
		templatelist.append(template['template'])
	return list(set(templatelist))

def get_producer_list():
	producer_list = []
	for template in database.db.templates.find():
		producer_list.append(template['producer'])
	return list(set(producer_list))

def get_format_list():
	formatlist = []
	for format in database.db.formats.find():
		formatlist.append(format['name'])
	return formatlist

def strip_date(dt):
	class t_stamp:
		def  __init__(self,d):
			self.year = datetime.datetime.fromtimestamp(int(d)).strftime('%Y')
			self.month = datetime.datetime.fromtimestamp(int(d)).strftime('%m')
	date = t_stamp(dt)
	return date
