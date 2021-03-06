from common import database
import calendar
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

def get_hook_list():
	hooks = []
	for hook in database.db.hooks.find():
		hooks.append(hook['hook'])
	return hooks

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

def get_category_list():
	list = ['current','recurrent','gold','special']
	return list

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

def get_style_ids(styles):
	idlist = []
	for style in styles:
		idlist.append(str(database.db.styles.find_one({'name':style})['uid']))
	return idlist

def get_months():
	months = []
	for month in calendar.month_name:
		months.append(month)
	return months

def get_month_number(month):
	months = get_months()
	number = str(months.index(month))
	return number.zfill(2)


