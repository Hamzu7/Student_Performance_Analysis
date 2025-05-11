#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv("Expanded_data_with_more_features.csv")
data = data.drop("Unnamed: 0", axis=1)
data


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.isna().sum()


# In[8]:


data = data.drop("TransportMeans", axis=1)


# In[9]:


data["EthnicGroup"].fillna(data["EthnicGroup"].mode()[0], inplace=True)


# In[10]:


data["ParentEduc"].fillna(data["ParentEduc"].mode()[0],inplace=True)


# In[11]:


data["ParentMaritalStatus"].fillna(data["ParentMaritalStatus"].mode()[0],inplace=True)
data["IsFirstChild"].fillna(data["IsFirstChild"].mode()[0], inplace= True)


# In[12]:


data["PracticeSport"].fillna("No info", inplace=True)
data["TestPrep"].fillna("Unknown", inplace=True)
data["NrSiblings"].fillna(data["NrSiblings"].median(), inplace=True)


# In[13]:


data["WklyStudyHours"] = data.groupby("TestPrep")["WklyStudyHours"].transform(
lambda x: x.fillna(x.mode()[0]))


# In[14]:


data.isna().sum()


# In[15]:


data.duplicated().sum()


# In[16]:


data[data.duplicated(keep=False)]


# In[17]:


data.drop_duplicates(inplace=True)


# In[18]:


data.duplicated().sum()


# In[19]:


data["Gender"].count()


# In[20]:


plt.figure(figsize=(5,5))
ax = sns.countplot(data = data, x = "Gender")
ax.bar_label(ax.containers[0])
plt.show()


# From the above chart we have analysed that:
# The number of females in the data is more than the number of males.

# In[21]:


gb = data.groupby("ParentEduc").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb


# In[22]:


plt.figure(figsize=(4,4))
sns.heatmap(gb, annot=True)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# From the above chart we have concluded that the education of the parents have a good impact on their score.

# In[23]:


gb1 = data.groupby("ParentMaritalStatus").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb1


# In[24]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1, annot=True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# from the above chart we have concluded that there is no/negligible impact on the students score due to their parent's marital status.

# In[25]:


sns.boxplot(data = data, x="MathScore")
plt.show()


# In[26]:


sns.boxplot(data = data, x = "ReadingScore")
plt.show()


# In[27]:


sns.boxplot(data = data, x = "WritingScore")
plt.show()


# In[28]:


data["EthnicGroup"].unique()


# In[30]:


groupA = data.loc[(data["EthnicGroup"] == "group A")].count()
groupB = data.loc[(data["EthnicGroup"]) == "group B"].count()
groupC = data.loc[(data["EthnicGroup"]) == "group C"].count()
groupD = data.loc[(data["EthnicGroup"]) == "group D"].count()
groupE = data.loc[(data["EthnicGroup"]) == "group E"].count()

l = ["group A","group B","group C","group D","group E"]
my_list = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(my_list)
plt.pie(my_list, labels = l,autopct="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[31]:


gb2 = data.groupby("TestPrep").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb2


# In[32]:


plt.figure(figsize=(5,5))
sns.heatmap(gb2,annot=True)
plt.title("Test preparation status")
plt.show()


# The data clearly shows that students who completed the test preparation course performed significantly better across all subjects compared to those who did not participate.
# 
# Math Score: 69.55 vs 64.95
# 
# Reading Score: 73.73 vs 67.05
# 
# Writing Score: 74.70 vs 65.09
# 
# This suggests that test preparation has a strong positive impact on academic performance, especially in Reading and Writing.

# In[33]:


gb3 = data.groupby("LunchType").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb3


# In[34]:


plt.figure(figsize=(5, 5))
sns.heatmap(gb3, annot=True, cmap="Blues")
plt.title("Effect of Lunch Type on Student Scores")
plt.show()


# The analysis indicates that students who receive a standard lunch score significantly higher in Math (70.71), Reading (72.18), and Writing (71.53) compared to students who receive free or reduced lunch, whose average scores are notably lower across all subjects.
# This suggests that better nutrition and food quality may positively impact students' academic performance.

# In[35]:


gb4 = data.groupby("PracticeSport").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb4


# In[36]:


plt.figure(figsize=(5,5))
sns.heatmap(gb4, annot=True, cmap="Blues")
plt.title("Effect of Regular Sports on Student Scores")
plt.show()


# The analysis reveals that students who participate in sports regularly have higher average scores across all subjects (Math, Reading, and Writing) compared to those who never play sports or play sometimes.
# 
# Math Score: Regularly playing sports leads to the highest Math score (67.84), followed by sometimes (66.27) and never (64.17).
# 
# Reading Score: Regularly playing sports results in the highest Reading score (69.94), with sometimes (69.24) and never (68.34) slightly lower.
# 
# Writing Score: Again, regularly participating in sports gives the highest Writing score (69.60), compared to sometimes (68.07) and never (66.52).
# 
# This suggests that regular physical activity might positively influence academic performance, helping students to achieve better results in their studies.

# In[37]:


gb5 = data.groupby("WklyStudyHours").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb5


# In[39]:


plt.figure(figsize=(5,5))
sns.heatmap(gb5, annot=True, cmap="Blues")
plt.title("Impact of Weekly Study Hours on Academic Scores")
plt.show()


# The analysis shows that students who study more hours weekly (>10 hours) tend to have higher average scores in Math, Reading, and Writing, compared to those studying less (<5 hours). Thus, more study hours correlate with better academic performance.

# In[41]:


gb6 = data.groupby("IsFirstChild").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
gb6


# In[42]:


plt.figure(figsize=(5,5))
sns.heatmap(gb6, annot=True, cmap="Blues")
plt.title("Impact of Being the First Child on Academic Scores")
plt.show()


# First children score slightly higher than non-first children in Math, Reading, and Writing, but the difference is minimal. Being the first child does not have a major impact on scores.

# In[45]:


data["Total"] = data["MathScore"] + data["ReadingScore"] + data["WritingScore"]
top_10_Student = data.sort_values("Total", ascending=False).head(10)
top_10_Student


# In[46]:


sns.boxplot(x='NrSiblings', y='Total', data=data)
plt.title('Number of Siblings vs Total Score')
plt.show()

