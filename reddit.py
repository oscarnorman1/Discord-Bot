import praw, json

def redditBot(subreddit):
    reddit = praw.Reddit(
        client_id="2TJn67NY9a7ty7vJMWtCzQ",
        client_secret="QoyfQVVThcdHMOTGobntzPt1timhwA",
        password="Xiqafc123Xiq",
        user_agent="Test script by Oscar Norman",
        username="Zlynan",
        check_for_async=False
    )
    print(reddit.user.me())

    subreddit = reddit.subreddit(subreddit)
    print("SUBREDDIT: {}".format(subreddit))
    subreddit_hot = subreddit.hot(limit=10)
    print("17")

    all_comments = []
    title = ''
    ups = ''

    bestSubmission = ''

    for bestSubmission in subreddit_hot:
        if not bestSubmission.stickied:
            bestSubmission = bestSubmission
            break

    #print('Title: {}, Ups: {}, Downs: {}'.format(submission.title, submission.ups, submission.downs))
    title = bestSubmission.title
    ups = bestSubmission.ups

    submission_comments = bestSubmission.comments.list()
    print('submission_comments size: {}'.format(len(submission_comments)))
    real_comments = [comment for comment in submission_comments if isinstance(comment, praw.models.Comment)]
    all_comments += real_comments
    print(len(all_comments))

    all_comments.sort(key=lambda comment: comment.score, reverse=True)
    top_comments = all_comments[:5]
    print(len(all_comments))

    values = {
        'title': title,
        'ups': ups,
        'one': str(top_comments[0].body),
        'oneUps': str(top_comments[0].score),
        'two': str(top_comments[1].body),
        'twoUps': str(top_comments[1].score),
        'three': str(top_comments[2].body),
        'threeUps': str(top_comments[2].score),
        'four': str(top_comments[3].body),
        'fourUps': str(top_comments[3].score),
        'five': str(top_comments[4].body),
        'fiveUps': str(top_comments[4].score)
    }

#    for top in top_comments:
#        print('Comment: {}, Ups: {}'.format(top.body, top.ups))

    return json.dumps(values)


