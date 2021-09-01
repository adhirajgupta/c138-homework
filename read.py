import re
import pandas as pd
import csv

shared_articles = pd.read_csv("shared_articles.csv")
users_interactions = pd.read_csv("users_interactions.csv")

print("shared_articles shape =",shared_articles.shape)
# print("users_interactions shape =",users_interactions.shape)
# print("\n")
# print("users_interactions head =",users_interactions.head(10))

# for i in range(0,3122):
#     if shared_articles["eventType"].iloc[i] == "CONTENT REMOVED":
#         print(1)

index_names = shared_articles[shared_articles["eventType"] == "CONTENT REMOVED"].index
shared_articles.drop(index_names,inplace=True)


def toLowerCase(title):
    return toLowerCase(title)

shared_articles["title"].apply(toLowerCase)
print(shared_articles["title"])