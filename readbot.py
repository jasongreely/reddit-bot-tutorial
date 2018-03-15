import praw

subName = "crumbumsandbox"

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit(subName)

for submission in subreddit.hot(limit=5):
    title = submission.title
    text = ""
    if hasattr(submission, "selftext"):
        text = submission.selftext

    score = submission.score

    if title:
        print(title)

    if text:
        print(text)

    if score:
        print(score)
    print("======================\n")

