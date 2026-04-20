
# Auto-install
try:
    import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
except:
    import os; os.system("pip install pandas seaborn matplotlib")
    import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

# Data
df=pd.DataFrame({
'Brand':['You','Comp_A','Comp_B'],
'Followers':[10000,50000,15000],
'Total_Engage':[1200,2000,1800]})

# Metrics
df['Eng_Rate %']=(df.Total_Engage/df.Followers)*100
df['Eng_per_1K']=df.Total_Engage/(df.Followers/1000)

# Clean Dashboard (no warning fix)
fig,ax=plt.subplots(1,2,figsize=(10,4))
sns.barplot(x='Brand',y='Eng_Rate %',hue='Brand',data=df,palette='magma',legend=False,ax=ax[0])
ax[0].set_title("Engagement Rate Comparison")

sns.barplot(x='Brand',y='Eng_per_1K',hue='Brand',data=df,palette='coolwarm',legend=False,ax=ax[1])
ax[1].set_title("Engagement per 1K Followers")

plt.tight_layout(); plt.show()

# Output
print("\n--- Competitor Analysis Table ---")
print(df.sort_values('Eng_Rate %',ascending=False))

top=df.sort_values('Eng_Rate %',ascending=False).iloc[0]
print(f"\n🏆 Top Performer: {top['Brand']} ({round(top['Eng_Rate %'],2)}%)")

print("\n📊 Insight:")
print("- High followers ≠ high engagement")
print("- Focus on content quality to improve engagement rate")
