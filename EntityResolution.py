import pandas as pd
import numpy as np
import sys
import recordlinkage

# Currently reads in
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

erAlgorithm = "simple"
algorithmError = "Please specify an appropriate algorithm"
if erAlgorithm == "simple": # Use simple mean of all string distances
    pairwise["prob"] = pairwise.mean(axis=1)
elif erAlgorithm == "logReg": # Use logistic regression
    features = ['fnJwDist','fnLevenDist','lnJwDist','lnLevenDist']
    from joblib import dump, load
    from sklearn.linear_model import LogisticRegression
    logRegModel = load('pugLogRegression.joblib')
    pairwise['prob'] = logRegModel.predict_proba(pairwise[features])[:,1]
elif erAlgorithm == "decisionTree":     # Use degression tree
    features = ['fnJwDist','fnLevenDist','lnJwDist','lnLevenDist']
    from joblib import dump, load
    from sklearn.tree import DecisionTreeRegressor
    treeModel = load('pugDecisionTree.joblib')
    pairwise['prob'] = treeModel.predict(pairwise[features])
else:
    print(algorithmError)

# Output edgelist w/ probability
pairwise[['prob']].to_csv(sys.stdout,index=True)
