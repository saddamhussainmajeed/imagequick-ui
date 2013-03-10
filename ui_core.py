from pymongo import MongoClient

connection = MongoClient()
db = connection.imagequick_dev

def get_voice_list():
	voicelist = []
	for voice in db.voices.find():
		voicelist.append(voice['name'])
	return voicelist

def get_template_list():
	templatelist = []
	for template in db.templates.find():
		templatelist.append(template['name'])
	return templatelist

def get_producer_list():
	producer_list = []
	for template in db.templates.find():
		producer_list.append(template['producer'])
	return list(set(producer_list))

def get_format_list():
	formatlist = []
	for format in db.formats.find():
		formatlist.append(format['name'])
	return formatlist