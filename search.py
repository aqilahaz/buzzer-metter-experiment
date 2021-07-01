import twint

c = twint.Config()
c.Username = "eny86315895"
#date and time
# c.Custom["tweet"] = ["id", "username", "name", "user_id", "created_at", "geo", "likes_count", "hashtags"
# ,"conversation_id", "urls", "mentions", "tweet", "timezone", "place", "photos", "replies_count", "retweets_count"
# , "link", "retweet", "quote_url", "video", "user_rt_id", "source", "retweet_date"]
c.Output = "Favorites.csv"
c.Store_csv = True
# c.Limit = 10
# c.Custom["user"] = ["bio","followers","following","retweets","profile-full"]
# c.Since = "2020-9-12"
# c.Until = "2020-11-12"
c.User_full = True

# twint.run.Search(c)
# twint.run.Profile(c)
twint.run.Search(c)
