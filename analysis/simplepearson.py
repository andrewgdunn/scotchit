#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
simplepearson.py
~~~~

Reference from: http://tungwaiyip.info/2012/Collaborative%20Filtering.html

"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "MIT"
__email__ = "andrew.g.dunn@gmail.com"

import pandas as pd

# Use tsv because there are some names that have commas
raw = pd.read_csv('../reference/data/2014.12.10.tsv', sep='\t')

# Rid ourselves of data we don't need for the recommendation
raw.drop('Timestamp', axis=1, inplace=True)
raw.drop('Link To reddit Review', axis=1, inplace=True)
raw.drop('Region', axis=1, inplace=True)
raw.drop('Price', axis=1, inplace=True)
raw.drop('Date', axis=1, inplace=True)

# single word column names
raw.rename(columns={'Whisky Name': 'whisky',
					   'Reviewer Username': 'user',
					   'Rating': 'rating'}, inplace=True)

wp = raw.pivot_table(columns=['user'], index=['whisky'], values='rating')

rating_texacer = wp['Texacer']
sim_texacer = wp.corrwith(rating_texacer)

wc = raw[rating_texacer[raw.whisky].isnull().values & (raw.user != 'Texacer')]
wc['similarity'] = wc['user'].map(sim_texacer.get)
wc['similarity_rating'] = wc.similarity * wc.rating

recommendation = wc.groupby('whisky').apply(lambda s: s.similarity_rating.sum() / s.similarity.sum())
print recommendation.order(ascending=False)