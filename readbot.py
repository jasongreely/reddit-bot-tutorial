import praw

subName = "nfl"

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit(subName)

for submission in subreddit.hot(limit=5):
    print(submission.title)
    print(submission.text)
    print(submission.score)
    print("======================\n")

