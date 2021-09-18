#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import modules
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# create a deck of cards with Ace at 11
unshuffled_deck= []
for i in [2,3,4,5,6,7,8,9,10,10,10,10,11]:
    unshuffled_deck = unshuffled_deck + (4 * [i])


# In[ ]:


# check deck
unshuffled_deck


# # Black Jack

# In[4]:


# Assign 0 to the NumPy random seed to make the results
np.random.seed(0)


# In[5]:


# Create an empty list called “turn"
turn = []


# In[39]:


np.random.permutation(unshuffled_deck)


# In[ ]:


# fill it up to start a for loop with 100,000 iterations
for h in range(100000):
    print(h)
    
    # In every loop, do the following:
    
    # shuffle the deck
    display("Shuffling deck.")
    shuffled_deck = np.random.permutation(unshuffled_deck) 
    
    # Pick the first 2 cards in the list as an initial hand to simulate taking the top 2 off the deck.
    display("Getting first two cards...")
    initial_hand = shuffled_deck[0:2]
    
    display("initial hand", initial_hand)
    
    # If the sum of the initial hand equals 22,
    if sum(initial_hand) == 22 and 11 in initial_hand:
        
        #  alter the first 11 with 1.
        hand = np.array([np.where(initial_hand == 11, 1, initial_hand)[0], initial_hand[-1]])
        
        display("hand equal to 22, changed 11 to 1", hand)
        
        while sum(hand) < 16:
            
            display(hand)
            
            hand = np.append(initial_hand, np.random.choice(shuffled_deck))
            
            display("Sum after changing 11 to 1 from 22 was less than 16. Hit.", hand)
            
            result = sum(hand)
            
            display("Result of hit.", result)
            
            turn.append(result)
        
    # If the sum of the hand is lower than 16
    while sum(initial_hand) < 16:
        
        display("Initial hand less than 16. See sum:", sum(initial_hand))
        
        # continue picking cards from the deck until the sum reaches or exceeds 16. (while = False)
        hand = np.append(initial_hand, np.random.choice(shuffled_deck))
        
        display("Initial hand less than 16. Hit gave me a new hand:", hand)
        
    # until the sum reaches or exceeds 16.
    if sum(hand) >= 16:
            
        display("After hit, sum is greater than or equal to 16. Adding to turn list this hand:", hand)
                    
        # get total sum of the hand
        result = sum(hand)
                
        # Add the total sum of the hand to the turn list as a result.
        turn.append(result)
              
    # if the sum of hand exceeds 21
    if sum(initial_hand) > 21:
        
        display("Initial had sum is greater than 21. Checking for an eleven")
            
        # check if there is an 11 in the hand and 
        if 11 in initial_hand:
            
            display("Initial hand over 21. 11 is present. Changing Ace to 1.")
                
            # alter it with 1
            hand = np.array([np.where(initial_hand == 11, 1, initial_hand)[0], initial_hand[-1]])
            
            display("First Ace changed to 1 in intitial hand over 21. Checking sum.")
                
            # After the altering, if the sum drops below 16,
            while sum(hand) < 16:
                    
                #go to the previous step and continue picking cards
                hand = np.append(hand, np.random.choice(shuffled_deck))
                
                display("Initial had sum is greater than 21. Checked and changed 11 if present. Checking for greater than or equal to 16.")
                    
            # until the sum reaches or exceeds 16.
            if sum(hand) >= 16:
                    
                # get total sum of the hand
                result = sum(hand)
                
                display("Initial was over 21. Changed 11 to 1. Above 16. Adding to turn.")
                
                # Add the total sum of the hand to the turn list as a result.
                turn.append(result)
                
        # get total sum of the hand
        display("Initial was above 21 but no 11 present. Adding to turn.")
        result = sum(initial_hand)
                
        # Add the total sum of the hand to the turn list as a result.
        turn.append(result)


# In[ ]:


# Visualize the histogram of the list.
plt.plot(turn)
plt.axhline(0.5, color='k')
plt.xlabel('Number of Turns')
plt.ylabel('Sum of the hand')
plt.show()


# In[ ]:


*full solution*

```
import numpy as np
import seaborn as sns

np.random.seed(0)

turn = []
for i in range (100000):
    i = 2
    shuffled_deck = np.random.permutation(unshuffled_deck)
    hand = shuffled_deck[-i:]
    if sum(hand) == 22:
        hand[np.where(hand == 11)[0][0]] = 1
    while sum(hand) < 16:
        i = i + 1
        hand = np.append(hand, shuffled_deck[-i])
        if sum(hand) > 21 and len(np.where(hand == 11)[0]) > 0:
            hand[np.where(hand == 11)[0][0]] = 1
    turn.append(sum(hand))

sns.histplot(turn, discrete=True)

