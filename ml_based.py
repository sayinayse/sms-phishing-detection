import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("TurkishSMSCollection.csv", sep=';')

# First 2 columns will be enough
df = df.drop(columns = "GroupText", axis = 1)

# Let's chck how many messages we have and their distributions
print(df["Group"].value_counts())

#Veri dağılımını görselleştirme
plt.figure(figsize=(8, 6))
sns.countplot(x="Group", data=df)
plt.title("Distribution of SMS")
plt.xlabel("1:SPAM 2:NORMAL")
plt.ylabel("Count")
plt.show()
