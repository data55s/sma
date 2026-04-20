## 5. Content based social media analysis
import pandas as pd, matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
from collections import Counter

# Simple Data
data = ["I love this laptop! 😍", "Terrible battery life 😡", "Normal build quality", "Amazing speed! 🔥", "Bad screen"]
df = pd.DataFrame(data, columns=["Content"])

# Shortest Sentiment & Keyword Logic
df["Pol"] = df["Content"].apply(lambda t: TextBlob(t).sentiment.polarity)
df["Sent"] = df["Pol"].apply(lambda p: "Pos" if p > 0 else ("Neg" if p < 0 else "Neu"))
words = " ".join(data).lower().split()

# Print Summary
print(df[["Content", "Sent"]], "\nTop Words:", Counter(words).most_common(3))

# Quick Visuals
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
df["Sent"].value_counts().plot(kind="pie", ax=ax1, title="Sentiment")
ax2.imshow(WordCloud(background_color="white").generate(" ".join(words)))
ax2.axis("off")
plt.show()
