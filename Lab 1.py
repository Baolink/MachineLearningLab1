#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("data.csv", index_col=0)

df


# In[2]:


df.describe()


# In[6]:


df.info()


# In[90]:


print(df.Age.mean())
print(df.Name[df.Age == df.Age.max()])
df.Wage = df.Wage.map(lambda x: x.lstrip('€ ').rstrip('K')).astype(int)
print(df.Wage.max())


# In[81]:


import matplotlib.pyplot as plt

plt.hist(df.Age, bins=20)
plt.xlabel('Age')
plt.ylabel('Amount of Player')
plt.title('Number of Players per Age Range')
plt.show()


# I noticed that most of the players are of age 20-30. Once players turn 30, there are fewer and fewer players.There aren't a single player that is of the age 45.I also noticed that there aren't a lot of players younger than 20,without no player being younger than 15.

# In[79]:


corrMatrix = df.corr()

corrMatrix


# A positive correlation is the Age to the Overall score, this makes sense because I assume as a player gets older they get more experience and become a better player their score would go up. A negative correlation is the Age to the Potential Score, this makes sense because as a player gets older their potential to do well lowers..A column I would use as input is Age because one's Age will determine their performance.A column I would use as a target is potential because as they get to a certain age their potetional will rise but once they also reach a certain age their body will get old and their poteional will decrease.

# In[19]:


import seaborn as sns

sns.heatmap(corrMatrix, annot=True, annot_kws={'size':1})


# In[12]:


plt.scatter(df.Age, df.Potential)
plt.xlabel("Players Age")
plt.ylabel("Players Potential Score")
plt.title("Players Age to their Potential Score")
plt.show()


# In[14]:


plt.scatter(df.Age, df.Overall)
plt.xlabel("Players Age")
plt.ylabel("Players Overall Score")
plt.title("Players Age to their Overall Score")
plt.show()

