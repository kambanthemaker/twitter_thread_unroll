import tweepy
import json
import sys
import os
import re
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)
auth = tweepy.AppAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
maxTweets = 1000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permit
def get_replies(tweet, screen):
    print("to:%s AND from:%s" % (screen, screen))
    replies = api.search(q="to:%s AND from:%s" % (screen, screen), count=50,
                                    since_id=tweet.id , max_id=None,  tweet_mode='extended')
    res = []
    for rep in replies:
        if rep.in_reply_to_status_id == tweet.id:
            res.append(rep)
            break
        else:
            pass
    if res:
        return res[0]
    else:
        pass
    return None
tweetIDs = [1271547041747832833]
for tweetID in tweetIDs:
    if tweetID:
        tweets = api.statuses_lookup([tweetID],  tweet_mode='extended')
        for tweet in tweets:
            replies = [tweet]
            profileImage = tweet.user.profile_image_url
            last_id = tweet.id
            dataExists = True
            reply = tweet
            while reply:
                print("Get replies for ", reply.id)
                reply = get_replies(reply, tweet.user.screen_name)
                if reply:
                    replies.append(reply)
print(replies)
