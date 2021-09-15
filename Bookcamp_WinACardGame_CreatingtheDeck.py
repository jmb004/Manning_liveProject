#!/usr/bin/env python
# coding: utf-8

# In[21]:


# import modules
import seaborn as sns


# In[64]:


# for loop that produces a Python list called unshuffled_deck that represents a 52-card deck.
counter= 0
unshuffled_deck= []
suits= range(1,5)

# Represent each card in the list with a numerical value
for suit in suits:
    
    # for 2 - 10 assign value, 10 for J-K, 11 for Ace for 4 suits. #suit = 2,3,4,5,6,7,8,9,10,10,10,10,11
    unshuffled_deck.append(2)
    unshuffled_deck.append(3)
    unshuffled_deck.append(4)
    unshuffled_deck.append(5)
    unshuffled_deck.append(6)
    unshuffled_deck.append(7)
    unshuffled_deck.append(8)
    unshuffled_deck.append(9)
    unshuffled_deck.extend((10,10,10,10))
    unshuffled_deck.append(11)


# In[65]:


# view the deck list of cards
unshuffled_deck


# In[74]:


# Visualize the histogram of the list of the deck.
sns.histplot(unshuffled_deck, discrete=True)

