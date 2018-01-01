import tweepy, time, sys
import config

def twitter_bot():
    # file from which to read tweets in
    argfile = str(sys.argv[1])

    # establish connection to twitter api
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # read in the tweets
    with open(argfile, "r") as file:
        tweets = file.readlines()
    
    for tweet in tweets:
        api.update_status(tweet)
        time.sleep(900) # update status every 25 minutes


if __name__ == "__main__":
    twitter_bot()
