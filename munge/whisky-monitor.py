#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
whisky-monitor.py
~~~~
script to scrape the first table of whisky-monitor

TODO:
 - second table has individual reviews (rather than computed average)

"""

__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "MIT"
__email__ = "andrew.g.dunn@gmail.com"

import pandas as pd
import requests
from lxml import html
from clint.textui import progress

# Works!
def get_page(url):
	page = requests.get(url)
	tree = html.fromstring(page.text)

	# top of the page
	try:
		name = tree.xpath('//div[@id="distilleryName"]/h1/text()')[0].split()
		distillery, bottle = name[0], ' '.join(name[1:])
	except IndexError:
		return None

	desc = tree.xpath('//div[@id="distilleryName"]/span/text()')[0][1:-1]

	# top of page average rating
	try:
		avg_rating = tree.xpath('//div[@id="distilleryName"]/span/span/text()')[0]
	except IndexError:
		avg_rating = 0

	# first table
	table = tree.find('.//table')
	i = iter(td.text for td in table.findall('.//td')[1:])
	data = dict(zip(i, i))

	# some text is international, we need to encode utf-8
	return [distillery, bottle.encode('utf-8'), data['Issued'],
			data['Alcohol By Volume'], avg_rating, desc.encode('utf-8')]


if __name__ == '__main__':
	df = pd.DataFrame(columns=('distillery', 'bottle', 'date', 'abv', 'rating', 'desc'))

	base_url = 'http://www.whisky-monitor.com/bottle.jsp?bid='

	# Using a progress bar
	# There is about 17,200 records to move through, some are null
	for i in progress.bar(range(1, 17200)):
		request_url = base_url + str(i)
		payload = get_page(request_url)
		if payload:
			df.loc[len(df)+1] = payload

		# save periodically
		if i % 500 == 0:
			df.to_csv('scotch.tsv', sep='\t')

	# save when finished
	df.to_csv('scotch.tsv', sep='\t')