from common import database

def get_voice_list():
	voicelist = []
	for voice in database.db.voices.find():
		voicelist.append(voice['name'])
	return voicelist

def get_style_list():
	stylelist = []
	for style in database.db.styles.find():
		stylelist.append(style['name'])
	return stylelist

def get_template_list():
	templatelist = []
	for template in database.db.templates.find():
		templatelist.append(template['name'])
	return templatelist

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

def get_format_ids(formats):
	idlist = []
	for format in formats:
		idlist.append(str(database.db.formats.find_one({'name':format})['uid']))
	return idlist

def get_voice_ids(formats):
	idlist = []
	for format in formats:
		idlist.append(str(database.db.voices.find_one({'name':format})['uid']))
	return idlist