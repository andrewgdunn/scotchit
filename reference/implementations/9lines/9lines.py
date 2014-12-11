# Found http://tungwaiyip.info/2012/Collaborative%20Filtering.html
# Uses dataset from: http://grouplens.org/datasets/movielens/

rating = pd.read_csv('movie_rating.csv')
rp = rating.pivot_table(cols=['critic'],rows=['title'],values='rating')

rating_toby = rp['Toby']
sim_toby = rp.corrwith(rating_toby)

rating_c = rating[rating_toby[rating.title].isnull().values & (rating.critic != 'Toby')]
rating_c['similarity'] = rating_c['critic'].map(sim_toby.get)
rating_c['sim_rating'] = rating_c.similarity * rating_c.rating

recommendation = rating_c.groupby('title').apply(lambda s: s.sim_rating.sum() / s.similarity.sum())
recommendation.order(ascending=False)

