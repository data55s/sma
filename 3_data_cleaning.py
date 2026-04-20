## 3. Data Cleaning & Storage of Social Media Data
from cleantext import clean
import pandas as pd
from pymongo import MongoClient

df = pd.DataFrame({
    "user":["john_doe","alice_99","mike_123","sara_k"],
    "tweet":[
        "I love AI!!! #MachineLearning http://example.com",
        "Worst service ever!!! #badexperience",
        "Python is awesome :) #coding #AI",
        "Delivery was late and bad #fail"
    ],
    "location":["Mumbai","Delhi",None,"Pune"]
})

df["cleaned_tweet"] = df["tweet"].apply(clean)   # ✅ fixed (no wrong params)
df["location"] = df["location"].fillna("Unknown")

col = MongoClient("mongodb://localhost:27017/")["social_media_db"]["cleaned_posts"]
col.delete_many({})
col.insert_many(df[["user","cleaned_tweet","location"]].to_dict("records"))

print(df)