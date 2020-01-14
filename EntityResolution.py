import pandas as pd
import itertools as it
import Levenshtein as lv
import sys

df  =  pd.read_csv("EntityResolution_attributeList.csv", delimiter=',')
df["fullName"] = df["First Name"] + " " + df["Last Name"]

# Merge dataframe to itself to get pairwise comparisons
df['fakeKey'] = 1
compareDf = df.merge(df, on='fakeKey',suffixes=["_1", "_2"]).reset_index(drop=True).drop('fakeKey', axis=1)
pairwiseDf = compareDf[compareDf['networkCanvasAlterID_1'] != compareDf['networkCanvasAlterID_2']]

# Calculate probability (using Jaro_winkler distance for now)
pairwiseDf["prob"] = pairwiseDf.apply(lambda x: lv.jaro_winkler(x["fullName_1"], x["fullName_2"]), axis=1)

# Output edgelist w/ probability
pairwiseDf[['networkCanvasAlterID_1','networkCanvasAlterID_2','prob']].to_csv(sys.stdout)
