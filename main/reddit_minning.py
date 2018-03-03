import praw

reddit = praw.Reddit(client_id='U4jFfDgjN8jrGA',
                     client_secret='wQVdcmbBYeHr-KzrNSodMWso99w',
                     user_agent='Mozilla/5.0')

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.comments.list())
