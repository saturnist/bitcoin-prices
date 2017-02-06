import praw

def reddit_search(sub, start):
    results = {}
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(sub)

    for b in subreddit.submissions(start, start + 86400):
        results[b.title] = b.url

    return results