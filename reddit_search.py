import praw


def reddit_search(sub, start):
    blacklist = [ 'reddit.com', 'redd.it', 'i.reddituploads.com']
    results = {}
    reddit = praw.Reddit()
    subreddit = reddit.subreddit(sub)

    for d in start:
        for b in subreddit.submissions(d, d + 86400):
            if any(reddit_url in b.url for reddit_url in blacklist):
                continue
            else:
                results[b.title] = b.url

    return results
