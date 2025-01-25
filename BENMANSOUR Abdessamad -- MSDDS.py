#!/usr/bin/env python
# coding: utf-8

# ## CONTROL

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ## Question 1

# In[15]:


df = pd.read_csv('Data/Produits.csv')
df


# ## Question 2

# In[29]:


profitlist=df['total_profit']
monthlist =df['month_number']


# In[129]:


plt.figure(figsize=(10,5))
plt.plot(monthlist,profitlist)
plt.title('Benefice de l\'entreprise')
plt.xticks(monthlist)
plt.yticks([100000,200000,300000,400000,500000])
plt.xlabel('Numèro du mois')
plt.ylabel('Bénefice en dollars')
plt.show()


# ## Question 3

# In[130]:


plt.figure(figsize=(10,5))
plt.plot(monthlist,profitlist,c='red',ls='--',lw=3, marker="o", markerfacecolor="black", label='donnes sur les bénefices de l\' années dernière')
plt.title('Benefice de l entreprise')
plt.xticks(monthlist)
plt.yticks([100000,200000,300000,400000,500000])
plt.xlabel('Numero du mois')
plt.ylabel('Bénefice en dollars')
plt.legend(loc="lower right")
plt.show()


# ## Question 4

# In[50]:


cremlist=df['facecream']
nettvisagelist=df['facewash']
dentifricelist=df['toothpaste']
savonbainlist=df['bathingsoap']
shampolist=df['shampoo']
hydratantlist=df['moisturizer']


# In[131]:


plt.figure(figsize=(10,5))
plt.plot(monthlist,cremlist,label='donnes sur les ventes du crème de visage',lw=3, marker='o')
plt.plot(monthlist,nettvisagelist,label='donnes sur les ventes du nettoyant visage',lw=3, marker='o')
plt.plot(monthlist,dentifricelist,label='donnes sur les ventes du dentifrice',lw=3, marker='o')
plt.plot(monthlist,savonbainlist,label='donnes sur les ventes du savan du bain',lw=3, marker='o')
plt.plot(monthlist,shampolist,label='donnes sur les ventes du shampoo ',lw=3, marker='o')
plt.plot(monthlist,hydratantlist,label='donnes sur les ventes du crème hidrattante',lw=3, marker='o')
plt.title('Données de ventes')
plt.xticks(monthlist)
plt.xlabel('Numero du mois')
plt.ylabel('Unite de ventre en nombre')
plt.legend()
plt.show()


# ## Question 5

# In[107]:


plt.figure(figsize=(10,5))
plt.scatter(monthlist,dentifricelist,label='donnes sur les ventes du dentifrice',lw=3, marker='.')
plt.title('Données de ventes de dentifrice')
plt.xticks(monthlist)
plt.xlabel('Numéro du mois')
plt.ylabel('Nombre d\'unités vendues')
plt.legend()
plt.grid()
plt.show()


# ## Question 6

# In[138]:


plt.figure(figsize=(10,5))
plt.bar(monthlist-0.12,cremlist,align='center',width=0.25)
plt.bar(monthlist+0.12,nettvisagelist,align='center',width=0.25)
plt.xticks(monthlist)
plt.grid()
plt.show()


# ## Question 7

# In[108]:


plt.figure(figsize=(10,5))
plt.bar(monthlist,savonbainlist)
plt.title('Données de ventes de savon bain')
plt.xticks(monthlist)
plt.xlabel('Numéro du mois')
plt.ylabel('Unités de ventes en nombre')
plt.grid()
plt.show()


# ## Question 8

# In[137]:


plt.figure(figsize=(10,5))
profitlist.hist()
plt.title('Données sur les bénefices')
plt.xticks([150000,175000,200000,225000,250000,300000,350000])
plt.yticks([0,1,2,2,4,5])
plt.xlabel('Fourchette de benefice en dollars')
plt.ylabel('benefice en dollars')
plt.show()


# ## Question 9

# In[135]:


plt.figure(figsize=(15,8))
y=[cremlist.sum(),nettvisagelist.sum(),dentifricelist.sum(),savonbainlist.sum(),shampolist.sum(),hydratantlist.sum()]
mylabeles=['Crème pour visage', 'Nettoyage pour visage','Dentifrice','Savon de bain','Shampoo','Crème hydrattante']
plt.pie(y,labels=mylabeles, autopct='%1.1f%%', shadow=True)
plt.title('Données de ventes ')
plt.legend(loc="lower right")
plt.show()


# In[ ]:




