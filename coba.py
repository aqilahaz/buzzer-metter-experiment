import twint

#configuration
config = twint.Config()
config.Search = "bukan"
config.Custom["tweet"] = ["id", "username", "name", "user_id", "created_at", "geo", "likes_count", "hashtags"
,"conversation_id", "urls", "mentions", "tweet", "timezone", "place", "photos", "replies_count", "retweets_count"
, "link", "retweet", "quote_url", "video", "user_rt_id", "source", "retweet_date"]
config.Limit = 1000
config.Output = "bukan.csv"
config.Store_csv = True
# config.Since = "2020-11-20"
# config.Until = "2020-11-29"
#running search
twint.run.Search(config)
