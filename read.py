import pandas as pd
import csv

# Reading the csv files
shared_articles = pd.read_csv("shared_articles.csv")
users_interactions = pd.read_csv("users_interactions.csv")

print("shared_articles shape =",shared_articles.shape)

# Removing the content removed eventType
index_names = shared_articles[shared_articles["eventType"] == "CONTENT REMOVED"].index
shared_articles.drop(index_names,inplace=True)
print("shared_articles shape =",shared_articles.shape)



total_views = []
for i in shared_articles["contentId"]:
    # print(i)
    temp_val = users_interactions.loc[users_interactions["contentId"] == i]
    total_views.append(temp_val)

print(len(total_views))