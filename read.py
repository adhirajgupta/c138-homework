import pandas as pd
import csv

shared_articles = pd.read_csv("shared_articles.csv")
users_interactions = pd.read_csv("users_interactions.csv")

print("shared_articles shape =",shared_articles.shape)

index_names = shared_articles[shared_articles["eventType"] == "CONTENT REMOVED"].index
shared_articles.drop(index_names,inplace=True)


def toLowerCase(title):
    return toLowerCase(title)

shared_articles["title"].apply(toLowerCase)
print(shared_articles["title"])
