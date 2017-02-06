import praw


def reddit_search(sub, start):
    results = {}
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(sub)

    for d in start:
        for b in subreddit.submissions(d, d + 86400):
            results[b.title] = b.url

    return results