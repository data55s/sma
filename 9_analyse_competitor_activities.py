## 9. Analyse competitor activities using Social Media Data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Competitor Data (Brand vs Competitor A & B)
data = {
    'Brand': ['You', 'Comp_A', 'Comp_B'],
    'Followers': [10000, 50000, 15000],
    'Total_Engage': [1200, 2000, 1800] # Likes + Comments
}
df = pd.DataFrame(data)
# Competitor Metric: Engagement Rate (True Influence)
df['Eng_Rate %'] = (df['Total_Engage'] / df['Followers']) * 100
# Quick Visual Battle
sns.barplot(x='Brand', y='Eng_Rate %', data=df, palette='magma')
plt.title("Who is Winning the Audience?")
plt.show()
print(df.sort_values('Eng_Rate %', ascending=False))
