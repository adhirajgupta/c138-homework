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
total_bookmarks = []
total_comment = []
total_follow = []
for i in shared_articles["contentId"]:
    # print(i)
    temp_val = users_interactions.loc[users_interactions["contentId"] == i]
    views = temp_val.loc[users_interactions["eventType"] == "VIEW"]
    bookmarks = temp_val.loc[users_interactions["eventType"] == "BOOKMARK"]
    comment = temp_val.loc[users_interactions["eventType"] == "COMMENT CREATED"]
    follow = temp_val.loc[users_interactions["eventType"] == "FOLLOW"]
    total_views.append(views)
    total_bookmarks.append(bookmarks)
    total_comment.append(comment)
    total_follow.append(follow)

print(total_views)
print(total_bookmarks)
print(total_comment)
print(total_follow)