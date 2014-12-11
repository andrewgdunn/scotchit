#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
munge.py
~~~~
Consumes the reddit scotch archive and produces three files. One that contains
numerical identifies for user, whisky, and corresponding review. Two more that
contain the identifier to name references for both user and whisky.

Created to feed recommendation engines that need simpler data (mahout example)
"""
__author__ = ["Andrew G. Dunn"]
__copyright__ = __author__
__license__ = "MIT"
__email__ = "andrew.g.dunn@gmail.com"

import pandas as pd

raw = pd.read_csv('reddit.r.scotch.tsv', sep='\t')

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

# Drop all rows that have NaN for the rating
raw = raw.dropna(subset=['rating'])

# what are the unique names for both whisky, and users
whisky_names = raw['whisky'].unique()
user_names = raw['user'].unique()

whisky_df = pd.DataFrame(columns={'index', 'name'})
user_df = pd.DataFrame(columns={'index', 'name'})

for index, name in enumerate(whisky_names):
	raw.replace(name, index, inplace=True)
	whisky_df.loc[len(whisky_df)+1] = [index, name]

for index, name in enumerate(user_names):
	raw.replace(name, index, inplace=True)
	user_df.loc[len(user_df)+1] = [index, name]

raw.to_csv('raw.csv')
whisky_df.to_csv('whisky_names.tsv', sep='\t')
user_df.to_csv('user_names.tsv', sep='\t')