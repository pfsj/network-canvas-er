
radar  = pd.read_csv("radarResults.csv",delimiter=',')

feature_cols = ['fnJwDist','fnLevenDist','lnJwDist','lnLevenDist']
X = radar[feature_cols] # Features
y = radar.truth         # Target variable

# Train data on RADAR Data
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X,y)
radar["prob"]=logreg.predict(X)

# Eval RADAR Data
cnf_matrix = metrics.confusion_matrix(radar.truth, radar.prob)
cnf_matrix

# Predict new data
X_pred = pairwiseUnique[feature_cols]
pairwiseUnique["prob"]=logreg.predict(X_pred)
