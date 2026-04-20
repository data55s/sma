## 4. Exploratory Data Analysis with visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Simplest Data Dictionary
data = {
    "Channel": ["TechHub", "GadgetBox", "ReviewPro", "ByteSize", "TechHub"],
    "Views": [10000, 50000, 25000, 5000, 15000],
    "Likes": [500, 2000, 1200, 100, 800],
    "Comments": [50, 150, 80, 10, 60]
}
df = pd.DataFrame(data)
# Calculate Metric
df['Engagement %'] = (df['Likes'] + df['Comments']) / df['Views'] * 100
# Fast Plotting
plt.figure(figsize=(10, 4))
# Plot A: Engagement Rate by Channel
plt.subplot(1, 2, 1)
sns.barplot(x="Engagement %", y="Channel", data=df, estimator="mean")
# Plot B: Correlations
plt.subplot(1, 2, 2)
sns.heatmap(df.select_dtypes('number').corr(), annot=True, cbar=False)
plt.tight_layout(); plt.show()
