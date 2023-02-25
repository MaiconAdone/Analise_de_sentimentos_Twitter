import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "sBGcss0sh6VE4Gxw2QLE2vid2"
# api secret key
api_secret_key = "IO7zJIa5hDmYEcj8PPE90AHayQPy7G5wDJT2Em3DQi9CAs5jie"
# access token
access_token = "1599497803784388611-zARmbS1s6gPUnwQnndsJCeKtSeosE2"
# access token secret
access_token_secret = "tBT9UXw2JqDgPVeLKpx5VDPmhPPIRvvPOytrxY8msoOot"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                #'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)