import pandas as pd
import csv
import plotly_express as px

# Reading the csv files
shared_articles = pd.read_csv("shared_articles.csv")
users_interactions = pd.read_csv("users_interactions.csv")

print("shared_articles shape =",shared_articles.shape)

# Removing the content removed eventType
index_names = shared_articles[shared_articles["eventType"] == "CONTENT REMOVED"].index
shared_articles.drop(index_names,inplace=True)
print("shared_articles shape =",shared_articles.shape)



# Matching each contentId from shared articles to the user interactions file
# Then looking for different eventTypes and storing them in different arrays 
total_views = []
total_bookmarks = []
total_comment = []
total_follow = []
total_likes = []
for i in shared_articles["contentId"]:
    temp_val = users_interactions.loc[users_interactions["contentId"] == i]
    views = temp_val.loc[users_interactions["eventType"] == "VIEW"]
    bookmarks = temp_val.loc[users_interactions["eventType"] == "BOOKMARK"]
    comment = temp_val.loc[users_interactions["eventType"] == "COMMENT CREATED"]
    follow = temp_val.loc[users_interactions["eventType"] == "FOLLOW"]
    likes = temp_val.loc[users_interactions["eventType"] == "LIKE"]
    total_views.append(views)
    total_bookmarks.append(bookmarks)
    total_comment.append(comment)
    total_follow.append(follow)
    total_likes.append(likes)


# print(total_views)
# print(total_bookmarks)
# print(total_comment)
# print(total_follow)



# print(len(total_follow))
# print(len(total_likes))
# print(len(total_comment))




# The code inside the triple quotes add columns of views,bookmarks etc. to shared articles data frame 

views = []
for i in range(len(total_views)):
    views.append(len(total_views[i]["eventType"]))
shared_articles["views"] = views
bookmarks = []
for i in range(len(total_bookmarks)):
    bookmarks.append(len(total_bookmarks[i]["eventType"]))
shared_articles["bookmarks"] = bookmarks
likes = []
for i in range(len(total_likes)):
    likes.append(len(total_likes[i]["eventType"]))
shared_articles["likes"] = likes
follow = []
for i in range(len(total_follow)):
    follow.append(len(total_follow[i]["eventType"]))
shared_articles["follow"] = follow
comment = []
for i in range(len(total_comment)):
    comment.append(len(total_comment[i]["eventType"]))
shared_articles["comments"] = comment

    

# print(actions)



# Adding all the event types and adding a final column
# final = pd.read_csv("final.csv")
total_actions = []
for i in range(len(total_bookmarks)):
    sum = 0
    sum+= len(total_comment[i]) + len(total_follow[i]) + len(total_bookmarks[i])+len(total_views[i]) + len(total_likes[i])
    total_actions.append(sum)


shared_articles["total_actions"] = total_actions

shared_articles.to_csv("final2.csv")
