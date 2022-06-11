#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [TMDB-MOVIES]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Intro</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# This data set contains information
# about 10,000 movies collected from
# The Movie Database (TMDb),
# including user ratings and revenue
# 
# 
# ### Question(s) for Analysis
# **Does the Budget of the movie effect its Revenue?**
# 
# **What is the top 5 Movies in (Revenue-Rank-Popularity) ?**
# 
# 

# In[41]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.

# # Reading the data

# In[42]:


df=pd.read_csv('tmdb-movies.csv')
df.head()


# In[43]:


df.describe()


# # Cleaning the Data

# In[44]:


df.drop(['id','imdb_id','cast','homepage','tagline','budget_adj','revenue_adj','keywords'],axis=1,inplace=True)


# In[45]:


df.head()


# In[46]:


df.shape


# In[47]:


df.info()


# In[48]:


df.info()


# In[49]:


df.isnull().sum()


# In[50]:


df.dropna(subset=['genres','production_companies','overview','director'],axis=0,inplace=True)


# In[51]:


df.isnull().sum()


# In[52]:


df.drop_duplicates(inplace=True)


# In[53]:


df.info()


# # Overview and analysis about the data 

# In[54]:


df.hist(figsize=(16,16));


# **Buget:Most of the movies have average budget of 1.5 Million**
# 
# **Release Year:More films have been made over time**
# 
# **Run Time:100s the average of run time count**
# 
# **Vote Average: Most of movies has average vote between 5-7**
# 
# **Vote Count:Most of movies has more than 1000 vote count**
# 
# 

# # Does the Budget of the movie effect its Revenue?

# In[55]:


plt.figure(figsize=[16,10])
df.revenue.hist(label='revenue')
df.budget.hist(label='budget')
plt.legend()
plt.title('Movies')
plt.xlabel('revenue')
plt.ylabel('budget')


# **There is no big relation between revenue and the budget of the movie!**

# # What is the top 5 Movies in (Revenue-Rank-Popularity) ?

# In[56]:


df.groupby('release_year')['revenue'].mean().sort_values(ascending=False)


# **Films of 2004 have the most revenue count**

# In[57]:



def top():
    top_votes=df.sort_values(by=x,ascending=False).head()
    return top_votes


# In[58]:


x='vote_average'
y=top()['original_title']
z=top()['vote_average']
plt.bar(y,z)
plt.title('Top 5 Movies')
plt.xlabel('Movie')
plt.ylabel('Rank')
plt.show()


# **Top fives vote count:**
# 
# 1-Pink Floyd:Pulse====[Music]====(8.7)
# 
# 2-Queen Rock Montreal====[Music]====(8.5)
# 
# 3-A Personal Journey With Martin Scorsese Through American Movies====[Documentary]====(8.5)
# 
# 4-The Art of Flight====[Adventure|Documentary]====(8.5)
# 
# 5-The Shawshank Redemption====[Drama|Crime]====(8.4)
# 

# In[59]:


x='revenue'
y=top()['original_title']
z=top()['revenue']
plt.bar(y,z)
plt.title('Top 5 Movies')
plt.xlabel('Movie')
plt.ylabel('Revenue')
plt.show()


# **Top Movies Revenue:**
# 
# 1-[Avatar]
# 
# 2-[Star Wars: The Force Awakens]
# 
# 3-[Titanic]
# 
# 4-[The Avengers]
# 
# 5-[Jurassic World]

# In[60]:


x='popularity'
y=top()['original_title']
z=top()['popularity']
plt.bar(y,z)
plt.title('Top 5 Movies')
plt.xlabel('Movie')
plt.ylabel('Popularity')
plt.show()


# **Top Popular Movies:**
# 
# 1-[Jurassic World]
# 
# 2-[Mad Max]
# 
# 3-[Interstellar]
# 
# 4-[Gurdians of the Galaxy]
# 
# 5-[Insurgent]

# # Conclusions
# **There is no big relation between revenue and the budget of the movie!**
# 
# **Films of 2004 have the most revenue count**
# 
# **New released Movies have the highest budget due to the progress in technology which greatly contributed to the development of filmmaking**
# 
# **Most popular Movies are the newest movies due to the big interst to movies nowdays and it also have the highest revenue**
# 

# # Limitation
# **There is alot of missing values and also wrong values (like 0 in revenue and budget) so i deleted alot of rows**
# 
# **Numbers are big and complicated and that made my analysis not so accurate**
# 
# **Some Columns are worthless so i dropped them**

# In[61]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:





# In[ ]:




