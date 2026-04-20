## 2. Data Collection for Social Media Platform
from yt_dlp import YoutubeDL
import pandas as pd

with YoutubeDL({"quiet": True}) as y:
    r = y.extract_info("ytsearch20:Laptop Review", download=False)

data = [[v["title"], v["uploader"], v["view_count"],
         v["like_count"], v["comment_count"],
         v["upload_date"], v["duration"], v["webpage_url"]]
        for v in r["entries"]]

df = pd.DataFrame(data, columns=[
    "Title","Channel","Views","Likes",
    "Comments","Upload Date","Duration","URL"
])

df.to_csv("youtube_business_data.csv", index=False)
print(df.head())
