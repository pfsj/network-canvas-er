import pandas as pd
import numpy as np
import sys
import recordlinkage

df  =  pd.read_csv("EntityResolution_attributeList.csv", delimiter=',',index_col='networkCanvasAlterID')

# Merge dataframe to itself to get pairwise comparisons
indexer = recordlinkage.Index()
indexer.full()
index_list = indexer.index(df)
comp_pairs = recordlinkage.Compare()
comp_pairs.string('First Name', 'First Name', method='jarowinkler',label='fnJwDist')
comp_pairs.string('Last Name', 'Last Name', method='jarowinkler',label='lnJwDist')
comp_pairs.string('First Name', 'First Name', method='levenshtein',label='fnLevenDist')
comp_pairs.string('Last Name', 'Last Name', method='levenshtein',label='lnLevenDist')
pairwise = comp_pairs.compute(index_list, df)

pairwise["prob"] = features.mean(axis=1)

# Output edgelist w/ probability
pairwise[['prob']].to_csv(sys.stdout,index=True)
