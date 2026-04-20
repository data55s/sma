# Auto-install
try:
    import pandas as pd, matplotlib.pyplot as plt
    from textblob import TextBlob
except:
    import os; os.system("pip install pandas matplotlib textblob")
    import pandas as pd, matplotlib.pyplot as plt
    from textblob import TextBlob

from collections import Counter
import re

# Data
posts=["I love this product","Bad service","Great price!","Very slow delivery","Amazing experience"]

# 🔹 Advanced Analysis
df=pd.DataFrame(posts,columns=["Post"])
df["Polarity"]=df["Post"].apply(lambda x: round(TextBlob(x).sentiment.polarity,2))
df["Subjectivity"]=df["Post"].apply(lambda x: round(TextBlob(x).sentiment.subjectivity,2))
df["Sentiment"]=df["Polarity"].apply(lambda p:"Positive" if p>0 else("Negative" if p<0 else"Neutral"))

# 🔹 Keywords (cleaned)
words=re.findall(r'\b\w+\b'," ".join(posts).lower())
top=Counter(words).most_common(5)

# 🔹 Visual
df["Sentiment"].value_counts().plot(kind='bar',color=['green','red','gray'])
plt.title("Sentiment Distribution"); plt.xlabel("Sentiment"); plt.ylabel("Count")
plt.show()

# 🔹 Output
print("\n--- Detailed Sentiment Analysis ---")
print(df)

print("\n--- Top Keywords ---")
for w,c in top: print(f"{w} : {c}")

# 🔹 Insight
print("\n📊 Insight:")
print("- Positive sentiment indicates satisfaction")
print("- Negative sentiment highlights service issues")
print("- Keywords show main discussion topics")
