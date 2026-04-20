## 10. Social Media text analysis model
import pandas as pd, matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter
# Simple Data (Posts)
posts = ["I love this product", "Bad service", "Great price!", "Very slow delivery", "Amazing experience"]
# Analyze: Sentiment (Positive/Negative) & Word Count
sentiment = ["Positive" if TextBlob(p).polarity > 0 else "Negative" for p in posts]
words = Counter(" ".join(posts).lower().split()).most_common(3)
# Quick Visual & Output
pd.Series(sentiment).value_counts().plot(kind='bar', color=['green', 'red'])
plt.title("Text Sentiment Analysis"); plt.show()
print(f"Sentiment: {sentiment}\nTop Topics: {words}")
