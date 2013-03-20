from common.core_utils import *
#from pandas import Series, DataFrame
#import pandas as pd
from common import database

def chart_templates():
	index = get_template_list()
	t_play = [0.0]*len(index)
	t_buy = t_play

	data = {
		'play':t_play,
		'buy':t_buy,
	}
	chart = DataFrame(data,index=index,columns=['play','buy'])
	chart['producer'] = ''
	for event in database.db.events.find({'producer':{'$exists':True}}):
		if event['event'] == 'play':
			chart.play[event['template']] += 1
		if event['event'] == 'purchase':
			chart.buy[event['template']] += 1
		if not chart['producer'][event['template']]:
			chart['producer'][event['template']] = event['producer']
	chart['b2p_percent'] = (chart.buy/chart.play)*100
	chart.sort_index()
	chart.to_excel('files/templates_analysis.xls')
	return chart

def chart_voices():
	
	voices=get_voice_list()
	play=[0.0]*len(voices)
	buy=[0.0]*len(voices)
	data={
		'play':play,
		'buy':buy
	}
	frame=DataFrame(data,index=voices)
	for event in database.db.events.find():
		for voice in event['voices']:
			if voice is not None:
				if event['event'] =='play':
					frame.play[voice] += 1
				elif event['event'] == 'purchase':
					frame.buy[voice] += 1
	frame['b2p_percent'] = (frame.buy/frame.play)*100
	frame.to_excel('files/voice_analysis.xls')
	return frame


def chart_formats():
	index = get_format_list()
	f_play = [0.0]*len(index)
	f_buy = [0.0]*len(index)
	data = {
					'play':f_play,
					'buy' :f_buy
				}
	chart = DataFrame(data,index=index)
	for event in database.db.events.find():
		if event['format'] is not None:
			if event['event'] == 'play':
				chart.play[event['format']] += 1
			elif event['event'] == 'purchase':	
				chart.buy[event['format']] += 1
	chart['b2p_percent'] = chart.buy/chart.play*100
	chart.sort_index()
	chart.to_excel('files/format_analysis.xls')
	return chart


def chart_producers():
	index = get_producer_list()
	p_play = [0.0]*len(index)
	p_buy = [0.0]*len(index)
	data = {
		'play':p_play,
		'buy' :p_buy
	}

	chart = DataFrame(data,index=index)
	print chart
	for event in database.db.events.find():
		if event['producer'] is not None:
			if event['event'] == 'play':
				chart.play[event['producer']] += 1
			elif event['event'] == 'purchase':
				chart.buy[event['producer']] += 1
	chart['b2p_percent'] = chart.buy/chart.play*100
	chart.sort_index()
	chart.to_excel('files/producer_analysis.xls')
	return chart

def chart_voice_format():
	voices = get_voice_list()
	formats = get_format_list()
	data = []
	for voice in voices:
		v_chart = []
		for format in formats:
			play = 0.0
			buy = 0.0
			for event in database.db.events.find({'format':format,'voices':voice}):
				if event['event'] == 'play':
					play += 1
				elif event['event'] == 'purchase':
					buy +=1
			v_chart.append(play)
			v_chart.append(buy)
		data.append(v_chart)
	f_list = []
	k_list = []
	for format in get_format_list():
		f_list.append(format)
		f_list.append(format)
		k_list.append('play')
		k_list.append('buy')
	col = pd.MultiIndex.from_arrays([f_list,k_list],names=['format','type'])

	chart = DataFrame(data,columns=col,index=get_voice_list())
	chart.to_excel('files/voice_format_analysis.xls')
	return chart

def monthly_voice(month,year):
	voices = get_voice_list()
	play = [0.0]*len(voices)
	buy = [0.0]*len(voices)
	data = {
		'buy':buy,
		'play':play
	}
	frame = DataFrame(data,index=voices)
	for e in database.db.events.find({'date.year':(year),'date.month':str(month)}):
		for v in e['voices']:
			if v is not None:
				if e['event'] == 'play':
					frame.play[v] += 1 
				elif e['event'] == 'purchase':
					frame.buy[v] += 1

	frame.to_excel('files/monthly_voices.xls')
	return frame

def monthly_templates(month,year):
	index = get_template_list()
	t_play = [0.0]*len(index)
	t_buy = t_play

	data = {
		'play':t_play,
		'buy':t_buy,
	}
	chart = DataFrame(data,index=index,columns=['play','buy'])
	chart['producer'] = ''
	for event in database.db.events.find({'producer':{'$exists':True},'date.year':year,'date.month':month}):
		if event['event'] == 'play':
			chart.play[event['template']] += 1
		if event['event'] == 'purchase':
			chart.buy[event['template']] += 1
		if not chart['producer'][event['template']]:
			chart['producer'][event['template']] = event['producer']
	chart['b2p_percent'] = (chart.buy/chart.play)*100
	chart.sort_index()
	chart.to_excel('files/monthly_templates.xls')
	return chart

def monthly_format(month,year):
	index = get_format_list()
	f_play = [0.0]*len(index)
	f_buy = [0.0]*len(index)
	data = {
					'play':f_play,
					'buy' :f_buy
				}
	chart = DataFrame(data,index=index)
	for event in database.db.events.find({'date.year':year,'date.month':month}):
		if event['format'] is not None:
			if event['event'] == 'play':
				chart.play[event['format']] += 1
			elif event['event'] == 'purchase':	
				chart.buy[event['format']] += 1
	chart['b2p_percent'] = chart.buy/chart.play*100
	chart.sort_index()
	chart.to_excel('files/monthly_formats.xls')
	return chart

def monthly_producer(month,year):
	index = get_producer_list()
	p_play = [0.0]*len(index)
	p_buy = [0.0]*len(index)
	data = {
		'play':p_play,
		'buy' :p_buy
	}

	chart = DataFrame(data,index=index)
	print chart
	for event in database.db.events.find({'date.year':year,'date.month':month}):
		if event['producer'] is not None:
			if event['event'] == 'play':
				chart.play[event['producer']] += 1
			elif event['event'] == 'purchase':
				chart.buy[event['producer']] += 1
	chart['b2p_percent'] = chart.buy/chart.play*100
	chart.sort_index()
	chart.to_excel('files/monthly_producers.xls')
	return chart


def pay_voice(month,year):
	voices = get_voice_list()
	commission = [0.0]*len(voices)
	data = {
		 'commission':commission,
	}
	frame = DataFrame(data,index=voices)
	print year,month
	for event in database.db.events.find({'event':'purchase','date.year':year,'date.month':month}):
		l=1
		if event['voices']:
			l =len(event['voices'])
	 	com = (5.99*0.25)/l
	 	for voice in event['voices']:
	 		if voice is not None:
	 			frame.commission[voice] += com
	frame.to_excel('files/pay_voices.xls')
	return frame

def pay_producer(month,year):
	producers = get_producer_list()
	commission = [0.0]*len(producers)
	data = {
		 'commission':commission,
	}
	frame = DataFrame(data,index=producers)
	print year,month
	for event in database.db.events.find({'event':'purchase','date.year':year,'date.month':month}):
		if event['producer']:
	 		com = 5.99*0.25
	 		frame.commission[event['producer']] += com
	frame.to_excel('files/pay_producers.xls')
	return frame

