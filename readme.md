scotchit
========
> Better Whisky Drinking Through Data Science[^0]

A modest collection of different analysis utilities to make recommendations to
the users of [/r/scotch](http://www.reddit.com/r/Scotch).

There are other data sets that are 'publically' available that might provide
taxonomies, or further contextual data for augumenting the recommenders.
Scrapers for those data sets will be included, althogh without explicit
permission we won't include the data from the sources in the repository.

# Known Datasets

## /r/scotch archive
[/r/scotch archive](https://docs.google.com/spreadsheets/d/1X1HTxkI6SqsdpNSkSSivMzpxNT-oeTbjFFDdEkXD30o)

Tended by the community at [/r/scotch](http://www.reddit.com/r/scotch). Form is
a bit free field so there are some data processing challenges, however has
over 10,000 responses.

## 86 Distilleries by Dr. Wisehart
[86 Distilleries](https://www.mathstat.strath.ac.uk/outreach/nessie/nessie_whisky.html)

Compiled by professor Wisehart for his publications:[@wishart2006whisky],
[@wishart2009flavour]. Dr. Wisehart has moved beyond University of St Andrews
and with him a lot of contextual information about the data set. Christopher
Ingraham of [@wonkviz:scotch] mirrored some of the background on methadology. In
fear of loosing that, we'll mirror some here:

> _Most distilleries produce several brands that are differentiated by length of time in cask, special conditioning or finishing, e.g. to impart flavours such as oak, sherry, port or Madeira to the whisky. As our objective was to develop a classification of malts that are readily available to consumers, we felt we should select a benchmark malt whisky from each distillery. We firstly excluded rare malts and any premium brands that are specially aged, cask conditioned or finished. We also decided not to cover distilleries that had been demolished or are not currently in production_

> _Not all of our 10 authors reviewed the same distillation from each distillery, as some limit their tasting notes to house style only. Where more than one distillation is produced we selected the most widely available brand, usually of 10-15 years maturation in cask. New distilleries that currently offer young malts (Arran and Drumguish) were included for future reference, as they evolve. Vatted malts (blends of pure malts), and malt whiskies produced in Ireland, Japan, New Zealand and Wales were excluded. We thus arrived at 86 single malt whiskies of around 10-15 years maturation, most of which are widely available in the United Kingdom._

> _A vocabulary of 500 aromatic and taste descriptors was thus compiled from the tasting notes in the 8 books. These were grouped into 12 broad aromatic features: Body (Light-Heavy), Sweetness (Dry-Sweet), Smoky (Peaty), Medicinal (Salty), Feinty (Sulphury), Honey (Vanilla), Spicy (Woody), Winey (Sherry), Nutty (Oaky-Creamy), Malty (Cerealy), Fruity (Estery) and Floral (Herbal)._

Many use this data set to create visualizations[^1] or even analysis[^2].

## Whisky-Monitor by Malt Maniacs
[Whisky-Monitor](http://www.whisky-monitor.com)

Tended by the Malt Maniacs community. Similar to the /r/scotch archive, but has
much more rigorous approach to organizing the 'released' bottles from
distillaries. Typically has more contextual information also.

# Interesting Articles or Analysis

[K-Means Clustering 86 Single Malt Scotch Whiskies](http://blog.revolutionanalytics.com/2013/12/k-means-clustering-86-single-malt-scotch-whiskies.html)
Uses K-Means clustering to surmise regional variations in taste profiles from
the 86 distilleries data set.

[Better Whisky Drinking Through Data Science](http://www.nanigans.com/2014/03/20/better-whisky-drinking-through-data-science/)
Uses the t-distributed Stochastic Neighborhood Embedding (t-SNE) technique with
the 86 distilleries data set.

[Building Recommender Systems in Python](http://nbviewer.ipython.org/gist/glamp/20a18d52c539b87de2af)
Recommendation Engine in python. Not using scotch data, but is using Beer data!


[^0]: http://www.nanigans.com/2014/03/20/better-whisky-drinking-through-data-science/
[^1]: http://wonkviz.tumblr.com/post/72159021235/whiskey-flavor-profiles
[^2]: http://blog.revolutionanalytics.com/2013/12/k-means-clustering-86-single-malt-scotch-whiskies.html