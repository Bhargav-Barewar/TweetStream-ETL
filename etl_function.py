import tweepy
import pandas as pd
from airflow.models import Variable
import s3fs


def etl_process():
    bearer2_token = Variable.get("bearer_token")

    client = tweepy.Client(bearer_token=bearer2_token)

    # Get user ID from username
    user = client.get_user(username='elonmusk')
    user_id = user.data.id

    username = user.data.username   # get username
    name = user.data.name    # get name

    response = client.get_users_tweets(
        id=user_id,
        max_results=100,
        tweet_fields=["created_at", "public_metrics"]
    )

    tweets_json = []
    if response.data:
        for tweet in response.data:
            tweets_json.append({
                "user_name": name,
                "user_username": username,
                "text": tweet.text,
                "favorite_count": tweet.public_metrics.get("like_count", 0),
                "retweet_count": tweet.public_metrics.get("retweet_count", 0),
                "created_at": tweet.created_at
            })

        # Convert to DataFrame
        df = pd.DataFrame(tweets_json)

        # Display first few rows
        print(df.head())

        # Optional: Save CSV to s3  # make sure to edit bucket name
        df.to_csv("s3://our-bucket-name-here/elonmusk_tweets.csv", index=False)
    else:
        print("No tweets found.")