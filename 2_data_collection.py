# Auto-install if missing
try:
    from yt_dlp import YoutubeDL
except:
    import os; os.system("pip install yt-dlp pandas"); from yt_dlp import YoutubeDL

import pandas as pd

ydl_opts={"quiet":True,"no_warnings":True}

with YoutubeDL(ydl_opts) as y:
    r=y.extract_info("ytsearch30:Laptop Review",download=False)  # fetch more

data=[[v["title"],v["uploader"],v["view_count"],
       v.get("like_count"),v.get("comment_count"),
       v["upload_date"],v["duration"],v["webpage_url"]]
      for v in r["entries"] if v][:10]  # take only 10

df=pd.DataFrame(data,columns=[
"Title","Channel","Views","Likes","Comments","Upload Date","Duration","URL"])

df.to_csv("youtube_business_data.csv",index=False)
print(df.head(10))
