from yt_dlp import YoutubeDL
import pandas as pd

# Fetch YouTube data
with YoutubeDL({"quiet": True}) as y:
    r = y.extract_info("ytsearch20:Laptop Review", download=False)

# Extract required fields safely
data = [[
    v.get("title"),
    v.get("uploader"),
    v.get("view_count"),
    v.get("like_count"),
    v.get("comment_count"),
    v.get("upload_date"),
    v.get("duration"),
    v.get("webpage_url")
] for v in r.get("entries", []) if v]

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Title","Channel","Views","Likes",
    "Comments","Upload Date","Duration","URL"
])

# Save + Display
df.to_csv("youtube_business_data.csv", index=False)
print(df.head())
