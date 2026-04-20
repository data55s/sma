# Auto-install
try:
    import pandas as pd, matplotlib.pyplot as plt
    from textblob import TextBlob
    from wordcloud import WordCloud
except:
    import os; os.system("pip install pandas matplotlib textblob wordcloud")
    import pandas as pd, matplotlib.pyplot as plt
    from textblob import TextBlob
    from wordcloud import WordCloud

from collections import Counter
import re

# Data
data=["I love this laptop! 😍","Terrible battery life 😡","Normal build quality","Amazing speed! 🔥","Bad screen"]
df=pd.DataFrame(data,columns=["Content"])

# Sentiment Analysis
df["Polarity"]=df["Content"].apply(lambda t: round(TextBlob(t).sentiment.polarity,2))
df["Sentiment"]=df["Polarity"].apply(lambda p:"Positive" if p>0 else("Negative" if p<0 else"Neutral"))

# Keywords
words=re.findall(r'\b\w+\b'," ".join(data).lower())
top=Counter(words).most_common(5)

# Clean Output
print("\n--- Sentiment Analysis Table ---")
print(df)
print("\n--- Top 5 Keywords ---")
for w,c in top: print(f"{w} : {c}")

# Visuals
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,4))
df["Sentiment"].value_counts().plot(kind="pie",autopct="%1.0f%%",ax=ax1,title="Sentiment Distribution")
ax2.imshow(WordCloud(background_color="white").generate(" ".join(words))); ax2.set_title("Keyword Cloud"); ax2.axis("off")
plt.show()
