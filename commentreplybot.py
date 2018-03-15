import praw
import re
import os

REPLIED_POST_LIST = "repliedPostList.txt"
SUBREDDIT_TARGET = "crumbumsandbox"

reddit = praw.Reddit("bot1")

#plain text file to store submission ids
print(os.path)
if not os.path.isfile(REPLIED_POST_LIST):
    repliedPostList = []
else:
    with open(REPLIED_POST_LIST, "r") as f:
        repliedPostList = f.read()
        repliedPostList = repliedPostList.split("\n")
        repliedPostList = list(filter(None, repliedPostList))

#load new posts in subreddit and reply

subreddit = reddit.subreddit(SUBREDDIT_TARGET)

for submission in subreddit.new(limit=5):
    if submission.id not in repliedPostList:
        if re.search("this is how we do it", submission.title, re.IGNORECASE):
            submission.reply("It's Friday Nieeeght")
            print("ReplyBot replying to post " + submission.id + ": " + submission.title)
            repliedPostList.append(submission.id)

#save new id's to plain text file

with open(REPLIED_POST_LIST, "w") as f:
    for postId in repliedPostList:
        f.write(postId + "\n")