from common import database
import os

def station_frequency_position(format,voice):
	format_id = str(database.db.formats.find_one({'name':format})['uid'])
	voice_id = str(database.db.voices.find_one({'name':voice})['uid'])
	database.backup('templates')
	database.db.templates.update({"formatids":format_id,"posWords":{"$in":[" ",""]}},{"$addToSet": {"statVoiceids":voice_id,"freVoiceids":voice_id } },multi=True)
	database.db.templates.update({"formatids":format_id,"posWords":{"$nin":[" ",""]}},{"$addToSet": {"statVoiceids":voice_id,"freVoiceids":voice_id,"posVoiceids":voice_id } },multi=True)
	return True

def station_frequency(format,voice):
	format_id = str(database.db.formats.find_one({'name':format})['uid'])
	voice_id = str(database.db.voices.find_one({'name':voice})['uid'])
	database.backup('templates')
	database.db.templates.update({"formatids":format_id},{"$addToSet": {"statVoiceids":voice_id,"freVoiceids":voice_id } },multi=True)
	return True

def station(format,voice):
	format_id = str(database.db.formats.find_one({'name':format})['uid'])
	voice_id = str(database.db.voices.find_one({'name':voice})['uid'])
	database.backup('templates')
	database.db.templates.update({"formatids":format_id},{"$addToSet": {"statVoiceids":voice_id} },multi=True)
	return True

def frequency(format,voice):
	format_id = str(database.db.formats.find_one({'name':format})['uid'])
	voice_id = str(database.db.voices.find_one({'name':voice})['uid'])
	print format_id,voice_id
	database.backup('templates')
	database.db.templates.update({"formatids":format_id},{"$addToSet": {"freVoiceids":voice_id} },multi=True)
	return True

def position(format,voice):
	format_id = str(database.db.formats.find_one({'name':format})['uid'])
	voice_id = str(database.db.voices.find_one({'name':voice})['uid'])
	database.backup('templates')
	database.db.templates.update({"formatids":format_id,"posWords":{"$nin":[" ",""]}},{"$addToSet": {"posVoiceids":voice_id} },multi=True)
	return True

