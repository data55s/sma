# Auto-install
try:
    import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
except:
    import os; os.system("pip install pandas seaborn matplotlib")
    import pandas as pd, seaborn as sns, matplotlib.pyplot as plt

# Data
df=pd.DataFrame({
"Channel":["TechHub","GadgetBox","ReviewPro","ByteSize","TechHub"],
"Views":[10000,50000,25000,5000,15000],
"Likes":[500,2000,1200,100,800],
"Comments":[50,150,80,10,60]})

# Feature Engineering
df["Engagement %"]=(df.Likes+df.Comments)/df.Views*100
df["Like/View Ratio"]=df.Likes/df.Views

# Visualization Dashboard
fig,ax=plt.subplots(2,2,figsize=(12,8))

sns.barplot(x="Channel",y="Engagement %",data=df,estimator="mean",ax=ax[0,0])
ax[0,0].set_title("Engagement by Channel")

sns.scatterplot(x="Views",y="Likes",size="Comments",data=df,ax=ax[0,1])
ax[0,1].set_title("Views vs Likes")

sns.histplot(df["Engagement %"],kde=True,ax=ax[1,0])
ax[1,0].set_title("Engagement Distribution")

sns.heatmap(df.select_dtypes("number").corr(),annot=True,cmap="coolwarm",ax=ax[1,1])
ax[1,1].set_title("Correlation Matrix")

plt.tight_layout(); plt.show()
