# Auto-install
try:
    from cleantext import clean; import unidecode
except:
    import os; os.system("pip install clean-text pymongo pandas unidecode"); from cleantext import clean

import pandas as pd,re,datetime as dt
from pymongo import MongoClient

df=pd.DataFrame({
"user":["john_doe","alice_99","mike_123","sara_k"],
"tweet":[
"I love AI!!! #MachineLearning http://example.com",
"Worst service ever!!! #badexperience",
"Python is awesome :) #coding #AI",
"Delivery was late and bad #fail"],
"location":["Mumbai","Delhi",None,"Pune"]})

# 🔹 Advanced Cleaning
df["cleaned_tweet"]=df["tweet"].apply(lambda x: clean(x,no_urls=True,no_punct=True,lower=True))
df["hashtags"]=df["tweet"].apply(lambda x: re.findall(r"#\w+",x))
df["mentions"]=df["tweet"].apply(lambda x: re.findall(r"@\w+",x))

# 🔹 Feature Engineering
df["char_len"]=df["cleaned_tweet"].str.len()
df["word_count"]=df["cleaned_tweet"].str.split().str.len()
df["hashtag_count"]=df["hashtags"].str.len()

# 🔹 Handling Missing + Filtering
df["location"]=df["location"].fillna("Unknown")
df=df[df["cleaned_tweet"].str.len()>3].drop_duplicates("cleaned_tweet")

# 🔹 Storage (MongoDB with metadata)
try:
    col=MongoClient("mongodb://localhost:27017/")["social_media_db"]["cleaned_posts"]
    col.delete_many({})
    col.insert_many([{**r,"timestamp":dt.datetime.now()} for r in df.to_dict("records")])
except: pass

print(df)
